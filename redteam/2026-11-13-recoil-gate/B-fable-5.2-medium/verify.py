#!/usr/bin/env python3
"""BRIEF.md の検算。python3 verify.py > results.txt で全問の数値を出す。
単位: 長さ d/2... ではなく SI。記号計算は sympy、数値は numpy。"""
import numpy as np
import sympy as sp

# ---------- 定数（BRIEF §1.2 の値をそのまま使う） ----------
c0 = 2.99792458e8
nu = 5.0007e18
om = 2 * np.pi * nu
lamC = 2.42631e-12
E0 = 510.99895e3 * 1.602176634e-19      # m_e c^2 [J]
G = 6.67430e-11
alpha = 7.2973525693e-3
hbar = 1.054571817e-34

th = sp.symbols('theta', real=True)
d, E, x0, w = sp.symbols('d E_0 x_0 omega', positive=True)
c, s = sp.cos(th), sp.sin(th)
# cos^4(th/2) = (1+cos)^2/4, sin^4(th/2) = (1-cos)^2/4 (下で数値でも確かめる。半角のままだと sympy が遅い)
TA = E * (1 + c) ** 2 / 4
TB = E * (1 - c) ** 2 / 4
K = E * s ** 2 / 2


def section(t):
    print("\n" + "=" * 72 + "\n" + t + "\n" + "=" * 72)


def num(expr):
    """記号 d=E0=omega=1, x0=0 を代入して numpy 関数にする (記号が残ると object 配列になり極端に遅い)。"""
    e = sp.sympify(expr).subs({d: 1, E: 1, w: 1, x0: 0})
    assert e.free_symbols <= {th}, e.free_symbols
    f = sp.lambdify(th, e, 'numpy')
    return lambda x: f(x) * np.ones_like(x, dtype=float)


def harmonics(expr, nmax=12):
    """expr(theta) の Fourier 係数 (cos, sin) を FFT で取り、有理数に丸めて返す。
    (記号積分は遅いので使わない。三角多項式なので FFT は丸め誤差まで厳密。)"""
    M = 256
    tg = np.arange(M) * 2 * np.pi / M
    f = num(expr)(tg)
    Fh = np.fft.rfft(f) / M
    out = {}
    for n in range(0, nmax + 1):
        a = (1 if n == 0 else 2) * Fh[n].real
        b = -2 * Fh[n].imag if n else 0.0
        if abs(a) > 1e-12 or abs(b) > 1e-12:
            out[n] = (sp.nsimplify(round(a, 12), rational=True), sp.nsimplify(round(b, 12), rational=True))
    return out


section("0. エネルギーの和")
_t = np.linspace(0, 2 * np.pi, 1001)
print("半角表示との差 max:", abs(np.cos(_t / 2) ** 4 - (1 + np.cos(_t)) ** 2 / 4).max(), abs(np.sin(_t / 2) ** 4 - (1 - np.cos(_t)) ** 2 / 4).max())
print("T_A+T_B+K - E0 =", sp.simplify(TA + TB + K - E))
print("T_A-T_B =", sp.simplify(TA - TB), " ; T_A+T_B =", sp.simplify(sp.expand_trig(TA + TB)))

# ---------- Q1 ----------
section("Q1. 核を固定 (x_m = 0)")
g_base = -c                                 # x_gamma = x_m + (d/2) g
Dc2_fixed = TA * (-d / 2) + TB * (d / 2) + K * (d / 2) * g_base
print("c^2 D(theta) =", sp.factor(sp.simplify(Dc2_fixed)))
print("  Fourier:", harmonics(Dc2_fixed / (E * d)), " x E0 d")
print("c^2 dD/dtheta =", sp.factor(sp.simplify(sp.diff(Dc2_fixed, th))))
# 光子球を自由に置けるとして D=C を解く
C = sp.symbols('C', real=True)
xg_need = sp.simplify((C + (d / 2) * E * c) / K)
print("D=C/c^2 に必要な x_gamma =", xg_need)
print("  分子の theta=0, pi での値:", sp.simplify((C + (d / 2) * E * c).subs(th, 0)),
      ",", sp.simplify((C + (d / 2) * E * c).subs(th, sp.pi)), " (両方 0 にできない -> 発散)")

# ---------- Q2 ----------
section("Q2. 核対の反跳")
xm = sp.Function('xm')(th)


def solve_xm(g):
    """x_gamma = x_m + (d/2) g(theta) のとき D 一定を与える x_m - x0。"""
    return sp.simplify((d / 2) * (c - s ** 2 * g / 2))


xm_base = solve_xm(g_base)
print("x_m - x0 =", sp.factor(xm_base), "=", sp.simplify(sp.fu(xm_base)))
print("  Fourier (x d):", harmonics(xm_base / d))
dxm = sp.simplify(sp.diff(xm_base, th))
print("dx_m/dtheta =", sp.factor(sp.trigsimp(dxm)), " -> 検算: +(3d/4)sin^3 との和 =",
      sp.simplify(dxm + sp.Rational(3, 4) * d * s ** 3))
Dc2 = TA * (x0 + xm_base - d / 2) + TB * (x0 + xm_base + d / 2) + K * (x0 + xm_base + d / 2 * g_base)
print("c^2 D =", sp.simplify(sp.expand(Dc2).subs(s**2, 1 - c**2)), " (定数)")
xg_base = sp.simplify(xm_base + d / 2 * g_base)
print("x_gamma - x0 =", sp.simplify(sp.fu(xg_base)), " Fourier (x d):", harmonics(xg_base / d))
print("x_A - x0 at theta=0:", sp.simplify((xm_base - d / 2).subs(th, 0)),
      "; x_B - x0 at theta=pi:", sp.simplify((xm_base + d / 2).subs(th, sp.pi)))

tt = np.linspace(0, 2 * np.pi, 200001)
f_xm = num(xm_base / d)
f_v = num(sp.diff(xm_base, th) / d)
f_vg = num(sp.diff(xg_base, th) / d)
print("x_m 範囲 (x d): [%.6f, %.6f]" % (f_xm(tt).min(), f_xm(tt).max()))
print("max|dx_m/dtheta|/d = %.6f, max|dx_gamma/dtheta|/d = %.6f" % (abs(f_v(tt)).max(), abs(f_vg(tt)).max()))
for name, dd in (("lambda_C/2", lamC / 2), ("lambda_C", lamC)):
    vn = abs(f_v(tt)).max() * dd * om
    vg = abs(f_vg(tt)).max() * dd * om
    vrel = dd * om / 2
    print("d=%-10s 核 v_max = %.4e m/s = %.5f c ; 光子球 v_max = %.4e = %.5f c ; 核から見た光子球 = %.5f c"
          % (name, vn, vn / c0, vg, vg / c0, vrel / c0))
print("参考: nu*lambda_C/c = %.6f, h nu = %.3f keV" % (nu * lamC / c0, 6.62607015e-34 * nu / 1.602176634e-16))

# ---------- Q3 ----------
section("Q3. 自明でない検査")
XA, XB, XG = xm_base - d / 2, xm_base + d / 2, xg_base
vA = w * sp.diff(XA, th); vG = w * sp.diff(XG, th)
p_pair = sp.simplify((TA + TB) * vA)                 # x c^2
p_gam = sp.simplify(K * vG)
dTA, dTB = w * sp.diff(TA, th), w * sp.diff(TB, th)
p_tr = sp.simplify(-dTA * (XG - XA) + dTB * (XB - XG))   # A->gamma, gamma->B のエネルギー流 x 距離
print("c^2 p_pair  =", sp.factor(sp.trigsimp(p_pair)))
print("c^2 p_gamma =", sp.factor(sp.trigsimp(p_gam)))
print("c^2 p_naive = pair+gamma =", sp.factor(sp.trigsimp(p_pair + p_gam)))
print("c^2 p_transfer =", sp.factor(sp.trigsimp(p_tr)))
print("合計 =", sp.simplify(p_pair + p_gam + p_tr))
for nm, e in (("p_pair", p_pair), ("p_gamma", p_gam), ("p_naive", p_pair + p_gam), ("p_transfer", p_tr)):
    print("  Fourier %-10s (x E0 w d):" % nm, harmonics(e / (E * w * d)))
F_pair = sp.simplify(w * sp.diff(p_pair, th))
print("核対に働く力 x c^2: Fourier (x E0 w^2 d):", harmonics(F_pair / (E * w ** 2 * d)))

# 数値の独立検査: D を固定核の式からではなく位置の数表から作り、差分で dD/dt を取り、naive と比べる
N = 4096
t = np.arange(N) * 2 * np.pi / N
cc, ss = np.cos(t), np.sin(t)
ta, tb, kk = np.cos(t / 2) ** 4, np.sin(t / 2) ** 4, 0.5 * ss ** 2
xmN = (9 * cc - np.cos(3 * t)) / 16                 # d=1, E0=1, omega=1
xa, xb, xgN = xmN - .5, xmN + .5, xmN - .5 * cc
Dn = ta * xa + tb * xb + kk * xgN
dd_ = lambda f: np.real(np.fft.ifft(1j * np.fft.fftfreq(N, 1 / N) * np.fft.fft(f)))
naive = (ta + tb) * dd_(xmN) + kk * dd_(xgN)
transfer = -dd_(ta) * (xgN - xa) + dd_(tb) * (xb - xgN)
print("数値: max|D - mean| = %.2e ; max|dD/dt| = %.2e" % (abs(Dn - Dn.mean()).max(), abs(dd_(Dn)).max()))
print("数値: max|naive| = %.6f (=1/2 が期待値) ; max|naive+transfer| = %.2e" % (abs(naive).max(), abs(naive + transfer).max()))

# 光子球の運動量を E/c (向きは核から見た進行方向) としたとき
for name, dv in (("lambda_C/2", lamC / 2), ("lambda_C", lamC)):
    beta = om * dv / c0
    p_c = np.sign(ss) * kk                           # x E0/c
    p_rest = beta * ((ta + tb) * dd_(xmN) + transfer)  # x E0/c
    res = p_rest + p_c
    # このとき P=0 に必要な核対の速度 (x c): (T_A+T_B) v/c^2 = -(K/c) - transfer
    mid = N // 4
    v_need = -(p_c[mid] + beta * transfer[mid]) / (ta[mid] + tb[mid])
    ke = 0.5 * (ta + tb) * (beta * dd_(xmN)) ** 2 + 0.5 * kk * (beta * dd_(xgN)) ** 2
    print("d=%-10s p_gamma=K/c のとき 残る運動量 max = %.4f E0/c ; theta=pi/2 で要る核速度 = %.3f c ; "
          "基準解の反跳運動エネルギー(非相対論) max = %.5f E0 = %.3f keV"
          % (name, abs(res).max(), v_need, ke.max(), ke.max() * 510.999))

# 電荷が核に乗る場合の電気双極子 (設定外の読み。参考)
print("参考(設定外): 電荷 e が核対と一緒に動くなら p_e = e (x_m - x0)。Larmor:")
for name, dv in (("lambda_C/2", lamC / 2), ("lambda_C", lamC)):
    acc2 = om ** 4 * dv ** 2 * (81 + 81) / 2 / 256     # <a^2>, x_m=(d/16)(9cos-cos3)
    PL = (2 / 3) * alpha * hbar / c0 ** 2 * acc2
    print("  d=%-10s P_EM = %.3e W, E0/P = %.2e s" % (name, PL, E0 / PL))

# ---------- Q4 ----------
section("Q4. 置き方への依存")
print("一般式: x_gamma の重心 = x_m + (d/2) g(theta) なら  x_m - x0 = (d/2)[cos - (sin^2/2) g]  (常に存在・一意)")
cases = {
    "基準 g=-cos": -c,
    "(i) 一様分布 (重心 g=0)": sp.Integer(0),
    "(ii-b) 核エネルギーの重心 g=-2cos/(1+cos^2)": -2 * c / (1 + c ** 2),
}
for nm, g in cases.items():
    xmg = solve_xm(g)
    f = num(xmg / d); fv = num(sp.diff(xmg, th) / d)
    xv = f(tt) * np.ones_like(tt); vv = fv(tt) * np.ones_like(tt)
    F = np.fft.rfft(f(t) * np.ones(N)) / N * 2
    hs = ", ".join("%d:%.5f" % (n, abs(F[n])) for n in range(1, 12) if abs(F[n]) > 1e-9)
    print("%s\n   x_m-x0 = %s\n   範囲 [%.4f, %.4f] d ; max|dx_m/dtheta| = %.4f d -> v_max = %.5f c (lambda_C/2), %.5f c (lambda_C)\n   高調波振幅(x d): %s"
          % (nm, sp.simplify(sp.fu(xmg)), xv.min(), xv.max(), abs(vv).max(),
             abs(vv).max() * om * lamC / 2 / c0, abs(vv).max() * om * lamC / c0, hs))
# (ii-a) 等速往復 (三角波)
tw = np.where(t <= np.pi, -1 + 2 * t / np.pi, 3 - 2 * t / np.pi)
xm_tri = 0.5 * (cc - ss ** 2 * tw / 2)
v_tri = dd_(xm_tri)
F = np.fft.rfft(xm_tri) / N * 2
print("(ii-a) 等速往復 g=三角波\n   範囲 [%.4f, %.4f] d ; max|dx_m/dtheta| = %.4f d -> v_max = %.5f c, %.5f c ; 光子球の核に対する速さ = d w/pi = %.5f c, %.5f c"
      % (xm_tri.min(), xm_tri.max(), abs(v_tri).max(), abs(v_tri).max() * om * lamC / 2 / c0,
         abs(v_tri).max() * om * lamC / c0, om * lamC / 2 / np.pi / c0, om * lamC / np.pi / c0))
print("   高調波振幅(x d):", ", ".join("%d:%.2e" % (n, abs(F[n])) for n in range(1, 16) if abs(F[n]) > 1e-9))
Dtri = ta * (xm_tri - .5) + tb * (xm_tri + .5) + kk * (xm_tri + .5 * tw)
print("   max|D-mean| = %.2e ; 偶数次の最大 = %.2e" % (abs(Dtri - Dtri.mean()).max(), max(abs(F[2:40:2]))))
print("移送項を消す置き方: g = (dT_B - dT_A)/(dT_A + dT_B) =", sp.simplify((sp.diff(TB, th) - sp.diff(TA, th)) / (sp.diff(TA, th) + sp.diff(TB, th))), " (|g|>=1: 核の外)")

# ---------- Q5 ----------
section("Q5. 二階モーメント")
J = sp.simplify(TA * XA ** 2 + TB * XB ** 2 + K * XG ** 2)
print("J =", sp.factor(sp.trigsimp(J)))
print("J - E0 d^2 sin^4(1+sin^2)/16 =", sp.simplify(J - E * d ** 2 * s ** 4 * (1 + s ** 2) / 16))
hJ = harmonics(J / (E * d ** 2))
print("Fourier (x E0 d^2):", hJ)
amp = {n: abs(float(a)) * n ** 3 for n, (a, b) in hJ.items() if n > 0}
tot = sum(v ** 2 for v in amp.values())
for n, v in amp.items():
    print("  %d omega: J''' 振幅 = %.6f E0 d^2 w^3, 出力の取り分 = %.4f %%" % (n, v, 100 * v ** 2 / tot))
mean_sq = tot / 2
# 一様分布の場合 (幅 d の一様: 分散 d^2/12)
XAu, XBu = solve_xm(0) - d / 2, solve_xm(0) + d / 2
Ju = sp.simplify(TA * XAu ** 2 + TB * XBu ** 2 + K * (solve_xm(0) ** 2 + d ** 2 / 12))
hJu = harmonics(Ju / (E * d ** 2))
print("一様分布の J =", sp.factor(sp.trigsimp(Ju)), " Fourier:", hJu)
ampu = {n: abs(float(a)) * n ** 3 for n, (a, b) in hJu.items() if n > 0}
totu = sum(v ** 2 for v in ampu.values())
print("  取り分:", {n: round(100 * v ** 2 / totu, 3) for n, v in ampu.items()}, " <J'''^2> 比(一様/基準) = %.4f" % (totu / tot))
print("\n出力: P = (2G/15c^5) <(d^3 I/dt^3)^2>, I = J/c^2  (軸対称な線状源, Q_ij Q_ij = (2/3) I^2)")
for name, dv in (("lambda_C/2", lamC / 2), ("lambda_C", lamC)):
    I3 = mean_sq * (E0 / c0 ** 2 * dv ** 2 * om ** 3) ** 2
    P = 2 * G / (15 * c0 ** 5) * I3
    print("  d=%-10s <I'''^2> = %.4e ; P_GW = %.4e W = %.3e eV/s ; E0/P = %.3e s = %.2e yr ; 一周期あたり %.3e E0"
          % (name, I3, P, P / 1.602176634e-19, E0 / P, E0 / P / 3.156e7, P / nu / E0))
