#!/usr/bin/env python3
"""
幹 T1（2026-09-24 版）T1.23–T1.25 の再現スクリプト ── ジューコフスキー変換と 0-Sphere

記号: ζ = z + a²/z（板の面 ζ = ξ + iη）、ζ̃ = z − a²/z、θ は T1 の角
（𝒯_A = cos²(θ/2), D = cos θ）。a はジューコフスキーの半径（異常磁気モーメントは a_e）。
本幹の方針により β_ZB の値は一度も使わない。
必要: sympy, numpy, mpmath
"""
import sympy as sp
import numpy as np
import mpmath as mp

rng = np.random.default_rng(20260924)
ok = lambda r, tol=1e-12: "OK" if abs(r) < tol else "NG"

z = sp.symbols('z')
a = sp.symbols('a', positive=True)
th, psi, ph = sp.symbols('theta psi phi', real=True)
zeta = z + a**2/z
zt = z - a**2/z

print("=== §1 平方完成の恒等式 ζ² − ζ̃² = (2a)²（T1.24）")
print("   ζ² − ζ̃² =", sp.simplify(zeta**2 - zt**2))
zz = sp.symbols('zz')
print("   逆変換＝平方完成: z² − ζz + a² の解 =", sp.solve(sp.Eq(zz**2 - sp.Symbol('zeta')*zz + a**2, 0), zz))

print("=== §2 二核を焦点にすると二乗（T1.23）")
s = (z - a)/(z + a)
print("   (ζ−2a)/(ζ+2a) − s² =", sp.simplify((zeta - 2*a)/(zeta + 2*a) - s**2))

print("=== §3 円の上: ξ = 2aD、s = i·tan(θ/2)、(ζ−2a)/(ζ+2a) = −𝒯_B/𝒯_A")
A = 1.7
T = rng.uniform(0.05, 2*np.pi - 0.05, 2000)
Z = A*np.exp(1j*T); ZE = Z + A**2/Z
r1 = np.max(np.abs(ZE - 2*A*np.cos(T)))
r2 = np.max(np.abs((Z - A)/(Z + A) - 1j*np.tan(T/2)))
TA, TB = np.cos(T/2)**2, np.sin(T/2)**2
r3 = np.max(np.abs((ZE - 2*A)*TA + (ZE + 2*A)*TB))/(4*A)   # 分母を払って比べる（θ → π で 𝒯_A → 0 のため）
print(f"   ξ−2aD {r1:.1e} {ok(r1)} / s − i tan {r2:.1e} {ok(r2,1e-9)} / S + 𝒯_B/𝒯_A（分母を払う） {r3:.1e} {ok(r3)}")

print("=== §4 タレスの定理: 𝒯_A = |z+a|²/(2a)², 𝒯_B = |z−a|²/(2a)²")
r4 = np.max(np.abs(np.abs(Z + A)**2/(4*A**2) - TA)); r5 = np.max(np.abs(np.abs(Z - A)**2/(4*A**2) - TB))
r6 = np.max(np.abs(np.abs(Z + A)**2 + np.abs(Z - A)**2 - 4*A**2))
print(f"   {r4:.1e} {ok(r4)} / {r5:.1e} {ok(r5)} / 和 = (2a)² {r6:.1e} {ok(r6,1e-11)}")

print("=== §5 D の正則な延長と臨界点、KE = ⅛|dζ/dz|²")
u = sp.symbols('u')
J = (u + 1/u)/2
print("   J(e^{iθ}) − cos θ =", sp.simplify(sp.expand_complex(J.subs(u, sp.exp(sp.I*th))) - sp.cos(th)))
print("   J'(u) = 0 の解 =", sp.solve(sp.Eq(sp.diff(J, u), 0), u), "（臨界集合 S⁰、延長しても増えない）")
dz = 1 - A**2/Z**2
r7 = np.max(np.abs(0.5*np.sin(T)**2 - np.abs(dz)**2/8))
print(f"   KE − ⅛|dζ/dz|² {r7:.1e} {ok(r7)}")

print("=== §6 表裏の入れ替え z ↦ a²/z は円の上で共役 ＝ θ → −θ ＝ b → −b（反射、電荷共役）")
r8 = np.max(np.abs(A**2/Z - np.conj(Z)))
print(f"   a²/z − z̄ {r8:.1e} {ok(r8)};  (cos(−θ/2), sin(−θ/2)) = (a, −b)")
print("   メビウス χ→−χ は振幅比 b/a を変えない ⇒ ジューコフスキー円の一段下に住む")

print("=== §7 モノドロミー √(ζ²−4a²)（a = 1）")
def cont(path):
    v0 = mp.sqrt(path[0]**2 - 4); v = v0
    for w in path[1:]:
        c = mp.sqrt(w**2 - 4); v = c if abs(c - v) < abs(-c - v) else -c
    return v/v0
N = 4000
one = [2 + 0.5*mp.e**(2j*mp.pi*k/N) for k in range(N + 1)]
both = [3*mp.e**(2j*mp.pi*k/N) for k in range(N + 1)]
print("   一核のまわり:", mp.nstr(cont(one), 6), " 二核をまとめて:", mp.nstr(cont(both), 6))

print("=== §8 1+1 次元ディラック（カイラル表示, c = 1）: R/L = z/a、ζ = E、ζ̃ = p")
p, m = sp.symbols('p m', real=True)
H = sp.Matrix([[p, m], [m, -p]])        # α = σ_z, β = σ_x
E = sp.sqrt(p**2 + m**2)
v = sp.Matrix([(E + p)/m, 1])
print("   Hv − Ev =", list(sp.simplify(H*v - E*v)))
Zs, As = (E + p)/2, m/2
print("   R/L − z/a =", sp.simplify((E + p)/m - Zs/As), "; ζ(z) − E =", sp.simplify(Zs + As**2/Zs - E),
      "; ζ̃(z) − p =", sp.simplify(Zs - As**2/Zs - p))
print("   固有値 =", H.eigenvals(), "（p = 0 で ±m、回避交差のギャップ 2m）")

print("=== §9 平面波（実の z = a e^ψ）: ⟨β⟩ = 1/γ = sech ψ、⟨α⟩ = v = tanh ψ、ブロッホ角 = gd ψ")
Ps = rng.uniform(-3, 3, 500); R = np.exp(Ps)
r9 = np.max(np.abs(2*R/(1 + R**2) - 1/np.cosh(Ps))); r10 = np.max(np.abs((R**2 - 1)/(R**2 + 1) - np.tanh(Ps)))
gd = 2*np.arctan(np.tanh(Ps/2))
r11 = np.max(np.abs(np.cos(gd) - 1/np.cosh(Ps))) + np.max(np.abs(np.sin(gd) - np.tanh(Ps)))
print(f"   {r9:.1e} {ok(r9)} / {r10:.1e} {ok(r10)} / gd {r11:.1e} {ok(r11)}")

print("=== §10 相対位相 φ: 状態 cos(θ/2)|+⟩ + e^{iφ} sin(θ/2)|−⟩ ⇒ s = e^{iφ} tan(θ/2)")
for phv, name in [(0, "φ = 0（実係数、T1.12 の形）"), (np.pi/2, "φ = +π/2（T2 の畳み方 a + ib）"),
                  (np.pi, "φ = π"), (-np.pi/2, "φ = −π/2"), (np.pi/4, "φ = π/4（参考）")]:
    c, sn = np.cos(T/2), np.sin(T/2)
    Rr, Ll = c + np.exp(1j*phv)*sn, c - np.exp(1j*phv)*sn   # |±⟩ = (1, ±1)/√2 のカイラル成分
    zr = Rr/Ll                                            # z/a
    sv = (zr - 1)/(zr + 1)
    ze = zr + 1/zr                                        # ζ/a
    rs = np.max(np.abs(sv - np.exp(1j*phv)*np.tan(T/2)))
    on_axis = np.max(np.abs(ze.imag)); on_circle = np.max(np.abs(np.abs(zr) - 1))
    print(f"   {name}: s 残差 {rs:.1e}; max|Im ζ| = {on_axis:.2e}; max||z/a|−1| = {on_circle:.2e}")
print("   （φ = 0, π は実軸なので |z/a| ≠ 1 で正しい。φ = ±π/2 だけが円＝板に乗る。φ = π/4 は ξ 軸を外れる）")
zc = (1 + 1j)/(1 - 1j)
print("   同位相 a = b（T2.4 の δ = π/2）を a|+⟩ + ib|−⟩ で読むと z/a =", zc, " ζ/a =", zc + 1/zc, "（板の中央）")

print("=== §11 ⟨H⟩/mc² = ⟨β⟩ と TPE の差（K4 の攻め口、B2 の下で）")
c2, s2 = sp.cos(th/2)**2, sp.sin(th/2)**2
print("   ⟨β⟩ = 𝒯_A − 𝒯_B − cos θ =", sp.simplify(c2 - s2 - sp.cos(th)),
      "; TPE_A − TPE_B − cos θ =", sp.simplify(c2**2 - s2**2 - sp.cos(th)))
print("   ⇒ ξ = mc²·D、TPE_A − TPE_B = E₀·D。両者を同一視すると E₀ = mc²（#38 の側）")

print("=== §12 a → 0 の極限（点粒子）")
print("   lim_{a→0} ζ =", sp.limit(zeta, a, 0), "（恒等写像。板は原点一点に潰れる）")

print("=== §13 エネルギーの二点と空間の二点: d = λ_C のとき d × 4a = 2hc")
mec2 = mp.mpf('0.51099895069')           # MeV（CODATA 2022）
lamC = mp.mpf('2.42631023538e-12')       # m
hc = mp.mpf('1.239841984e-12')           # MeV·m
print("   4a = 2mc² =", mp.nstr(2*mec2, 8), "MeV;  λ_C × 2mc² =", mp.nstr(lamC*2*mec2, 9), " 2hc =", mp.nstr(2*hc, 9),
      " 比 =", mp.nstr(lamC*2*mec2/(2*hc), 10))
print("   ħc/(2mc²) =", mp.nstr(hc/(2*mp.pi)/(2*mec2), 6), "m（= λ̄_C/2）")

print("=== §14 幹 T4 への接合: ξ → X（反跳閉包 T4.4）は単調、縮尺 ∝ KE、平坦性は二次×二次")
D = sp.symbols('D')
X = D*(3 - D**2)/2                       # X/(d/2)
print("   X/(d/2) − cos θ(1 + ½ sin²θ) =", sp.simplify(X.subs(D, sp.cos(th)) - sp.cos(th)*(1 + sp.sin(th)**2/2)))
print("   dX/dD ÷ KE =", sp.simplify(sp.diff(X, D)/((1 - D**2)/2)), "（KE = ½(1 − D²)、核で零）")
print("   X(cos θ) の展開 =", sp.series(X.subs(D, sp.cos(th)), th, 0, 6), "⇒ (d/2)·(−3/8)θ⁴ = −(3/16)dθ⁴（T4.6）")
print("   D = 0, 0.5, 0.9, 1 →", [float(X.subs(D, x)) for x in (0, sp.Rational(1, 2), sp.Rational(9, 10), 1)])

print("=== §15 クッタ条件（流体の読み、K14）")
U, al, G = sp.symbols('U alpha_w Gamma', real=True)
dW = U*(sp.exp(-sp.I*al) - a**2*sp.exp(sp.I*al)/z**2) + sp.I*G/(2*sp.pi*z)
GA = sp.solve(sp.expand_complex(dW.subs(z, a)), G)[0]
GB = sp.solve(sp.expand_complex(dW.subs(z, -a)), G)[0]
print("   核 A を滑らかに: Γ =", GA, "; そのとき核 B で dF/dz =", sp.simplify(sp.expand_complex(dW.subs({z: -a, G: GA}))), "≠ 0（dζ/dz = 0 なので速度は発散）")
print("   核 B を滑らかに: Γ =", GB, "; α_w = 0 なら Γ =", GA.subs(al, 0))

print("=== §16 二核（±a）と極（0, ∞）はリーマン球面上で 90°（T1.17 の第二の直交）")
def sphere(w):   # 単位円 |z/a| = 1 を赤道とする立体射影
    w = complex(w); d = 1 + abs(w)**2
    return np.array([2*w.real/d, 2*w.imag/d, (abs(w)**2 - 1)/d])
south, kA, kB = sphere(0), sphere(1), sphere(-1)
print("   極と核 A の角 =", np.degrees(np.arccos(south @ kA)), "度 / 核 A と核 B の角 =", np.degrees(np.arccos(kA @ kB)), "度")

print("=== §17 板の上の配分（E₀ = 1）")
for Dv in (1, sp.Rational(1, 2), 0, -sp.Rational(1, 2), -1):
    c2v = (1 + Dv)/2; s2v = (1 - Dv)/2
    print(f"   D = {str(Dv):>4}: TPE_A = {c2v**2}, TPE_B = {s2v**2}, KE = {2*c2v*s2v}, 和 = {c2v**2 + s2v**2 + 2*c2v*s2v}")
