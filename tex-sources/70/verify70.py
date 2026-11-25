#!/usr/bin/env python3
"""
SESSION-2026-10-31-nucleon-five-term-verification.py
====================================================
〔max探索｜2026-10-31｜Opus 5.5・Effort = Max〕

2026-10-31 の壁練「核子への五項モデル ── (cos² + sin²)ⁿ = 1 の鎖と QCD への接点」
（trunks/SESSION-2026-10-31-nucleon-five-term.md）の検算をすべて一つにまとめた再現
スクリプト。sympy / mpmath を使う。各項目は値と OK / NG を印字する。

記号（幹 T1 の T1.1）: 占有層 c = 𝒯_A = cos²(θ/2), s = 𝒯_B = sin²(θ/2), c + s = 1。
差 D = c − s = cos θ。電子の恒等式 E2: c² + 2cs + s² = 1（TPE_A = c², KE = 2cs, TPE_B = s²）。
θ は内部時間（README §0.1）。位相平均は θ ∈ [0, 2π) の一様平均。

項目
  H1  恒等式の全数列挙（cos⁸ まで）と、対称・節／継ぎ目のみ・交互の五項の鎖（cos¹² まで）
  H2  P4 ＝ スピン 2 のコヒーレント状態の完全性、E2 ＝ スピン 1、cos⁶ 系 ＝ スピン 3/2
  H3  三つの置き場の恒等式を二乗して M = m₁ + m₂ で束ねる（中央の節 ＝ KE² ＋ 2·TPE_A·TPE_B）
  H4  節 N・継ぎ目 L の閉じた形（D の式）と、二つの読み P4 = E², C5 = TPE + KE·E、二つの系列
  H5  位相平均と 3:1
  H6  倍音（端の差の調和性 ＝ T1.9 の第二規準）
  H7  力学の読み（位置に依る慣性）
  H8  赤道 θ = π/2 の値
  H9  T1.24 の D₀ = 1/γ に #61 の γ_p を入れた値（読み）
  H10 三核（S² 上の実振幅）の平均
  H11 look-elsewhere（QCD の数との 5% 一致は偶然でいくつ出るか）
  H12 中性子の寿命をうなり（T1.6）と読むのに要る離調
  H13 旧 K7 の異議（中央二項は A↔B で移り合う）の再読
  H14 端の節を二光束と読む可視度（T1.8）と中性子干渉計のコントラスト

実行:  python3 -I SESSION-2026-10-31-nucleon-five-term-verification.py
"""
from itertools import combinations, product
import math
import random

import mpmath as mp
import sympy as sp
from sympy.physics.quantum.spin import Rotation

mp.mp.dps = 30
th = sp.symbols('theta', real=True)
cs_c, D_ = sp.symbols('c D', real=True)
cc, ss = sp.symbols('cc ss', nonnegative=True)
C = (1 + sp.cos(th)) / 2      # = cos²(θ/2)、全角で書く
S = (1 - sp.cos(th)) / 2      # = sin²(θ/2)

OK = lambda b: "OK" if b else "NG"
ALL_OK = []


def check(label, cond):
    ALL_OK.append(bool(cond))
    print(f"    [{OK(cond)}] {label}")


def avg(expr):
    """θ ∈ [0, 2π) の一様平均（内部時間の平均）"""
    return sp.nsimplify(sp.integrate(sp.expand(expr), (th, 0, 2 * sp.pi)) / (2 * sp.pi))


def toD(poly_cs):
    return sp.expand(poly_cs.subs({cc: (1 + D_) / 2, ss: (1 - D_) / 2}, simultaneous=True))


def to_th(poly_cs):
    return poly_cs.subs({cc: C, ss: S}, simultaneous=True)


E2c = [cc**2, 2*cc*ss, ss**2]
P4c = [cc**4, 4*cc**3*ss, 6*cc**2*ss**2, 4*cc*ss**3, ss**4]
C5c = [cc**2, 2*cc**3*ss, 4*cc**2*ss**2, 2*cc*ss**3, ss**2]
E2, P4, C5 = ([to_th(t) for t in L] for L in (E2c, P4c, C5c))

print("=" * 78)
# ------------------------------------------------------------------------- H1
print("H1  恒等式 Σ a·c^i s^j = 1（a は正の整数）の全数列挙")


def columns(monos, deg):
    cols = {}
    for m in monos:
        p = sp.Poly(sp.expand(cs_c**m[0] * (1 - cs_c)**m[1]), cs_c)
        v = [0] * (deg + 1)
        for (e,), val in p.terms():
            v[e] = int(val)
        cols[m] = v
    return cols


def solutions(Ssub, cols, deg):
    M = sp.Matrix([[cols[m][e] for m in Ssub] for e in range(deg + 1)])
    b = sp.Matrix([1] + [0] * deg)
    try:
        sol, params = M.gauss_jordan_solve(b)
    except ValueError:
        return []
    bounds = [2 ** (m[0] + m[1]) for m in Ssub]   # c = 1/2 で評価すると各 a ≤ 2^次数
    if params.shape[0] == 0:
        v = list(sol)
        return [tuple(int(x) for x in v)] if all(x.is_integer and x > 0 for x in v) else []
    syms = list(params)
    idx = [next(q for q in range(len(Ssub)) if sol[q] == t) for t in syms]
    out = []
    for combo in product(*[range(1, bounds[q] + 1) for q in idx]):
        sub = dict(zip(syms, combo))
        v = [sol[q].subs(sub) for q in range(len(Ssub))]
        if all(x.is_integer and x > 0 for x in v):
            out.append(tuple(int(x) for x in v))
    return out


def kind(m):
    i, j = m
    if i % 2 == 0 and j % 2 == 0:
        return 'N'   # 節: i, j ともに偶
    if i % 2 == 1 and j % 2 == 1:
        return 'L'   # 継ぎ目: i, j ともに奇
    return 'x'       # 混合（全次数が奇数の単項式は必ずこれ: cos²・cos⁶ の層）


def is_sym(Ssub, a):
    d = dict(zip(Ssub, a))
    return all(d.get((j, i)) == v for (i, j), v in d.items())


MON4 = [(i, d - i) for d in range(1, 5) for i in range(d, -1, -1)]
COL4 = columns(MON4, 4)
counts, five = {}, []
for k in range(2, 6):
    found = [(Ssub, a) for Ssub in combinations(MON4, k) for a in solutions(Ssub, COL4, 4)]
    counts[k] = len(found)
    if k == 5:
        five = found
print("    cos⁸ まで（i + j ≤ 4）、k 項の恒等式の数:", counts)
check("項数 2/3/4/5 で 1/4/16/79 個", counts == {2: 1, 3: 4, 4: 16, 5: 79})
sym5 = [(Ssub, a) for Ssub, a in five if is_sym(Ssub, a)]
check(f"五項のうち cos↔sin 対称なもの 7 個（得: {len(sym5)}）", len(sym5) == 7)
check("全次数が奇数の単項式（cos²・cos⁶ の層）はすべて混合パリティ",
      all(kind(m) == 'x' for m in MON4 if (m[0] + m[1]) % 2 == 1))

MON6 = [(i, d - i) for d in range(1, 7) for i in range(d, -1, -1) if (2 * i - d) % 2 == 0]
COL6 = columns(MON6, 6)
chains = []
for Ssub in combinations(MON6, 5):
    Sset = set(Ssub)
    if any((j, i) not in Sset for (i, j) in Ssub):
        continue
    order = sorted(Ssub, key=lambda m: (-sp.Rational(m[0], m[0] + m[1]), -(m[0] + m[1])))
    fr = [sp.Rational(m[0], m[0] + m[1]) for m in order]
    if len(set(fr)) != 5 or ''.join(kind(m) for m in order) != 'NLNLN':
        continue
    for a in solutions(Ssub, COL6, 6):
        d = dict(zip(Ssub, a))
        if all(d[(j, i)] == val for (i, j), val in d.items()):
            chains.append(tuple((m, d[m]) for m in order))
want = {tuple(zip([(2, 0), (3, 1), (2, 2), (1, 3), (0, 2)], [1, 2, 4, 2, 1])),
        tuple(zip([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], [1, 4, 6, 4, 1]))}
for row in chains:
    print("     ", " + ".join((f"{a}·" if a != 1 else "") + "·".join(
        ([f"cos^{2*m[0]}"] if m[0] else []) + ([f"sin^{2*m[1]}"] if m[1] else [])) for m, a in row), "= 1（引数 θ/2）")
check("cos¹² まで、対称・節／継ぎ目のみ・N-L-N-L-N 交互の五項は C5 と P4 の二つだけ", set(chains) == want)

for name, terms in (("E2", E2c), ("P4", P4c), ("C5", C5c)):
    check(f"{name} の和は恒等的に 1", toD(sum(terms)) == 1)

# ------------------------------------------------------------------------- H2
print("H2  Wigner の小 d 行列（行 m' = j）との一致（30 桁、7 角で照合）")
ANG = [mp.mpf(k) / 7 for k in (1, 3, 5, 8, 11, 15, 19)]


def same(f, g):
    F_, G_ = sp.lambdify(th, f, 'mpmath'), sp.lambdify(th, g, 'mpmath')
    return max(abs(F_(t) - G_(t)) for t in ANG) < mp.mpf('1e-25')


def dsq(j, m):
    return Rotation.d(j, m, j, th).doit() ** 2


check("E2 の三項 ＝ |d¹_{m1}(θ)|²（m = 1, 0, −1）",
      all(same(dsq(1, m), E2[k]) for k, m in enumerate((1, 0, -1))))
check("P4 の五項 ＝ |d²_{m2}(θ)|²（m = 2 … −2）",
      all(same(dsq(2, m), P4[k]) for k, m in enumerate((2, 1, 0, -1, -2))))
h = sp.Rational(1, 2)
P3 = [C**3, 3*C**2*S, 3*C*S**2, S**3]
check("cos⁶ + 3cos⁴sin² + 3cos²sin⁴ + sin⁶ ＝ |d^{3/2}_{m,3/2}|²",
      all(same(dsq(3*h, m), P3[k]) for k, m in enumerate((3*h, h, -h, -3*h))))
par = {str(j): all(((j - m) % 2) == ((j + m) % 2) for m in [j - q for q in range(int(2*j) + 1)])
       for j in (sp.Integer(1), 3*h, sp.Integer(2))}
print("    節／継ぎ目のパリティ (−1)^(j−m) が A↔B（m → −m）で不変か:", par)
check("不変なのは 2j が偶数のときだけ（cos⁶ 系 j = 3/2 は節と継ぎ目が入れ替わる）",
      par == {'1': True, '3/2': False, '2': True})

# ------------------------------------------------------------------------- H3
print("H3  三つの置き場 n₊ + n₀ + n₋ = 1 の二乗を M = m₁ + m₂ で束ねる")
npl, n0, nmi = sp.symbols('n_p n_0 n_m', nonnegative=True)
groups = {2: npl**2, 1: 2*npl*n0, 0: n0**2 + 2*npl*nmi, -1: 2*n0*nmi, -2: nmi**2}
check("(n₊ + n₀ + n₋)² ＝ Σ_M P(M)（任意の三つ組で成立）",
      sp.expand(sum(groups.values()) - (npl + n0 + nmi)**2) == 0)
on = {npl: cc**2, n0: 2*cc*ss, nmi: ss**2}      # 電子の三つの置き場（Hardy–Weinberg の曲線 n₀² = 4n₊n₋）
check("電子の置き場に乗せると P(M) は P4 の五項", all(sp.expand(groups[M].subs(on) - P4c[2 - M]) == 0 for M in groups))
ratio = sp.simplify((n0**2).subs(on) / (2*npl*nmi).subs(on))
check(f"中央の節 6c²s² ＝ KE²（4c²s²）＋ 2·TPE_A·TPE_B（2c²s²）、比 {ratio}:1", ratio == 2)
x0p, x00, x0m = C, sp.sin(th) / sp.sqrt(2), S       # スピン 1 のコヒーレント振幅 (a², √2ab, b²)
spin0 = sp.simplify(sp.expand(2*x0p*x0m - x00**2).subs(sp.sin(th)**2, 1 - sp.cos(th)**2))
check(f"二乗したコヒーレント状態のスピン 0 成分 (2x₊x₋ − x₀²)/√3 ＝ {spin0}", spin0 == 0)

# ------------------------------------------------------------------------- H4
print("H4  節 N と継ぎ目 L（D = cos θ の式）")
forms = {}
for name, terms, ni, li in (("E2", E2c, (0, 2), (1,)), ("P4", P4c, (0, 2, 4), (1, 3)), ("C5", C5c, (0, 2, 4), (1, 3))):
    Nd, Ld = toD(sum(terms[q] for q in ni)), toD(sum(terms[q] for q in li))
    forms[name] = (Nd, Ld)
    print(f"    {name}: N = {sp.factor(Nd)},  L = {sp.factor(Ld)},  N − L = {sp.factor(Nd - Ld)}")
check("E2: N = (1 + D²)/2, L = (1 − D²)/2", forms["E2"] == (sp.expand((1 + D_**2)/2), sp.expand((1 - D_**2)/2)))
check("P4: N = (1 + D⁴)/2, L = (1 − D⁴)/2", forms["P4"] == (sp.expand((1 + D_**4)/2), sp.expand((1 - D_**4)/2)))
check("C5: N = (3 + D⁴)/4, L = (1 − D⁴)/4（継ぎ目は P4 のちょうど半分）",
      forms["C5"] == (sp.expand((3 + D_**4)/4), sp.expand((1 - D_**4)/4)))
TPE, KE = cc**2 + ss**2, 2*cc*ss
E = TPE + KE
check("P4 ＝ (TPE + KE)²（恒等式を丸ごと二乗）", sp.expand(E**2 - sum(P4c)) == 0)
check("C5 ＝ TPE + KE·(TPE + KE)（搬送体だけを一段開く）: 中央 ＝ KE²、継ぎ目 ＝ TPE·KE",
      sp.expand(KE**2 - C5c[2]) == 0 and sp.expand(TPE*KE - C5c[1] - C5c[3]) == 0)
# 二つの系列: P_{2m} = E^m（二項）、C_k = TPE·(1 + KE + … + KE^k) + KE^{k+1}（搬送体の反復）
ok_series = True
for k in range(0, 4):
    terms = []
    for i in range(k + 1):
        terms += [sp.expand(cc**2 * KE**i), sp.expand(ss**2 * KE**i)]
    terms.append(sp.expand(KE**(k + 1)))
    ok_series &= (toD(sum(terms)) == 1)
    mons = []
    for t in terms:
        for mon, coef in sp.Poly(t, cc, ss).terms():
            mons.append(mon)
    order = sorted(set(mons), key=lambda m: -sp.Rational(m[0], m[0] + m[1]))
    seq = ''.join(kind(m) for m in order)
    ok_series &= (seq == 'NL' * (k + 1) + 'N')
check("搬送体の反復 C_k（k = 0…3）は和 1 で、節と継ぎ目が交互（k+2 個の節）", ok_series)

# ------------------------------------------------------------------------- H5
print("H5  位相平均（内部時間の平均）")
av = {name: [avg(t) for t in terms] for name, terms in (("E2", E2), ("P4", P4), ("C5", C5))}
for name, a in av.items():
    print(f"    {name}: " + ", ".join(str(x) for x in a))
check("P4 の平均 35/128, 5/32, 9/64, 5/32, 35/128",
      av["P4"] == [sp.Rational(35, 128), sp.Rational(5, 32), sp.Rational(9, 64), sp.Rational(5, 32), sp.Rational(35, 128)])
check("C5 の平均 3/8, 5/64, 3/32, 5/64, 3/8",
      av["C5"] == [sp.Rational(3, 8), sp.Rational(5, 64), sp.Rational(3, 32), sp.Rational(5, 64), sp.Rational(3, 8)])
sub_P = [cmb for r in range(1, 5) for cmb in combinations(range(5), r) if sum(av["P4"][q] for q in cmb) == sp.Rational(1, 4)]
sub_C = [cmb for r in range(1, 5) for cmb in combinations(range(5), r) if sum(av["C5"][q] for q in cmb) == sp.Rational(1, 4)]
check(f"平均がちょうど 1/4 になる項の組: P4 には無い（{sub_P}）、C5 は中央＋継ぎ目だけ（{sub_C}）",
      sub_P == [] and sub_C == [(1, 2, 3)])
print("    <N>:<L>  E2 = 3/4 : 1/4,  P4 = 11/16 : 5/16,  C5 = 27/32 : 5/32")
gen = [sp.Rational(1, 2) * (1 + sp.binomial(2*m, m) / sp.Integer(4)**m) for m in range(1, 6)]
print("    偶数次 p = 2m の二項で <N> = (1 + C(2m,m)/4^m)/2:", gen, "→ 1/2")
check("3/4 になるのは p = 2（電子）だけ", [g == sp.Rational(3, 4) for g in gen] == [True, False, False, False, False])

# ------------------------------------------------------------------------- H6
print("H6  倍音（θ の Fourier 係数）")


def fourier(expr, nmax=5):
    out = {}
    for n in range(nmax + 1):
        an = sp.simplify(sp.integrate(sp.expand(expr * sp.cos(n*th)), (th, 0, 2*sp.pi)) / (sp.pi if n else 2*sp.pi))
        if an != 0:
            out[n] = an
    return out


fE, fP = fourier(E2[0] - E2[2]), fourier(P4[0] - P4[4])
print("    E2・C5 の端の差 TPE_A − TPE_B:", fE)
print("    P4     の端の差 c⁴ − s⁴      :", fP)
check("C5 の端の差は純粋な cos θ（T1.9 の調和性を保つ）", fE == {1: 1})
check("P4 の端の差は (7/8)cos θ + (1/8)cos 3θ（a₃/a₁ = 1/7）", fP == {1: sp.Rational(7, 8), 3: sp.Rational(1, 8)})
fPl, fCl = fourier(P4[1] - P4[3]), fourier(C5[1] - C5[3])
print("    継ぎ目の差 P4:", fPl, " C5:", fCl)
print("    中央の節 P4:", fourier(P4[2]), " C5 (KE²):", fourier(C5[2]))

# ------------------------------------------------------------------------- H7
print("H7  力学の読み（x = D = cos t、ẋ² = 1 − x²）")
x, xd = sp.symbols('x xdot', real=True)
for name, T_, V_, E_ in (("E2", xd**2/2, x**2/2, sp.Rational(1, 2)),
                         ("P4", (1 + x**2)*xd**2/2, x**4/2, sp.Rational(1, 2)),
                         ("C5", (1 + x**2)*xd**2/4, x**4/4, sp.Rational(1, 4))):
    tot = sp.simplify((T_ + V_).subs(xd**2, 1 - x**2))
    check(f"{name}: T = {T_}, V = {V_} で T + V = {tot}（一次元なので x = cos t が厳密解）", tot == E_)
    # 一般化ビリアル: d<x p>/dt = 0 → <m ẋ²> + <½ x m'(x) ẋ²> = <x V'(x)>（m(x) = 2T/ẋ²）
    tt = sp.symbols('t', real=True)
    m_x = sp.simplify(2 * T_ / xd**2)
    on_orbit = lambda f: sp.integrate(sp.expand(f.subs(xd**2, 1 - x**2).subs(x, sp.cos(tt))), (tt, 0, 2*sp.pi)) / (2*sp.pi)
    lhs = on_orbit(m_x * xd**2 + sp.Rational(1, 2) * x * sp.diff(m_x, x) * xd**2)
    rhs = on_orbit(x * sp.diff(V_, x))
    Tav, Vav = on_orbit(T_), on_orbit(V_)
    check(f"{name}: <T>:<V> = {Tav}:{Vav}、一般化ビリアル {sp.nsimplify(lhs)} = {sp.nsimplify(rhs)}",
          sp.simplify(lhs - rhs) == 0)

# ------------------------------------------------------------------------- H8
print("H8  赤道 θ = π/2（D = 0、KE 最大、#58 の放出位相）")
eqP = [sp.nsimplify(t.subs(th, sp.pi/2)) for t in P4]
eqC = [sp.nsimplify(t.subs(th, sp.pi/2)) for t in C5]
print("    P4:", eqP, "  C5:", eqC)
check("C5 は赤道で三つの節が等しい（1/4 ずつ）、二つの継ぎ目も等しい（1/8 ずつ）",
      eqC == [sp.Rational(1, 4), sp.Rational(1, 8), sp.Rational(1, 4), sp.Rational(1, 8), sp.Rational(1, 4)])

# ------------------------------------------------------------------------- H9
print("H9  読み: T1.24 の D₀ = cos 2θ₀ = 1/γ に #61 の γ_p = 1 + a_p を入れる")
a_p = 1.79284734462                     # CODATA 2022: μ_p/μ_N − 1
g_p = 1 + a_p
D0 = 1 / g_p
c0, s0 = (1 + D0) / 2, (1 - D0) / 2
P4n = [c0**4, 4*c0**3*s0, 6*c0**2*s0**2, 4*c0*s0**3, s0**4]
C5n = [c0**2, 2*c0**3*s0, 4*c0**2*s0**2, 2*c0*s0**3, s0**2]
print(f"    γ_p = {g_p:.6f}, D₀ = {D0:.6f}, θ = {math.degrees(math.acos(D0)):.2f}°")
print("    P4:", [round(v, 4) for v in P4n], " N =", round(P4n[0] + P4n[2] + P4n[4], 4), " L =", round(P4n[1] + P4n[3], 4))
print("    C5:", [round(v, 4) for v in C5n], " N =", round(C5n[0] + C5n[2] + C5n[4], 4), " L =", round(C5n[1] + C5n[3], 4))
check("和は 1", abs(sum(P4n) - 1) < 1e-12 and abs(sum(C5n) - 1) < 1e-12)

# ------------------------------------------------------------------------- H10
print("H10 三核: S² 上の実振幅 x、n_i = x_i²、一様測度")
u, v = sp.symbols('u v', real=True)
X = [sp.sin(u)*sp.cos(v), sp.sin(u)*sp.sin(v), sp.cos(u)]
n = [xi**2 for xi in X]
meas = sp.sin(u) / (4*sp.pi)
savg = lambda f: sp.simplify(sp.integrate(sp.integrate(sp.expand(f*meas), (v, 0, 2*sp.pi)), (u, 0, sp.pi)))
nodes3 = savg(sum(ni**2 for ni in n))
check(f"<Σ n_i²> = {nodes3}、<Σ 2n_in_j> = {1 - nodes3}（対称点では 1/3 : 2/3）", nodes3 == sp.Rational(3, 5))

# ------------------------------------------------------------------------- H11
print("H11 look-elsewhere: QCD の数との 5% 以内の一致は偶然でいくつ出るか")
vals = set()
for terms in (E2, P4, C5):
    a = [avg(t) for t in terms]
    for r in range(1, len(a)):
        for cmb in combinations(range(len(a)), r):
            vals.add(round(float(sum(a[q] for q in cmb)), 9))
for vv in (P4n, C5n, [float(t) for t in eqP], [float(t) for t in eqC]):
    for r in range(1, 5):
        for cmb in combinations(range(5), r):
            vals.add(round(sum(vv[q] for q in cmb), 9))
vals.update([0.6, 0.4, 1/3, 2/3])
vals = sorted(z for z in vals if 0.02 < z < 0.98)
QCD = {  # 値（出典は SESSION 文書 §5）
    "χQCD18 クォーク凝縮": 0.09, "χQCD18 クォークのエネルギー": 0.33, "χQCD18 グルーオン場のエネルギー": 0.37,
    "χQCD18 異常項": 0.23, "ETMC20 <x>_q": 0.618, "ETMC20 <x>_g": 0.427, "HPS24 A_q(0)": 0.510,
    "HPS24 A_g(0)": 0.501, "ETMC20 ΔΣ": 0.382, "ETMC20 J_g/(1/2)": 0.374, "漸近 <x>_g n_f=3": 16/25,
    "漸近 <x>_g n_f=4": 16/28, "漸近 <x>_g n_f=5": 16/31, "トレース部分": 0.25,
}
tol = 0.05
hits = [(k, q, z) for k, q in QCD.items() for z in vals if abs(z - q) / q <= tol]
hit_t = {k for k, _, _ in hits}
random.seed(20261031)
R, mh, mt = 2000, 0, 0
for _ in range(R):
    rv = [random.uniform(0.02, 0.98) for _ in vals]
    hh = [(q, z) for q in QCD.values() for z in rv if abs(z - q) / q <= tol]
    mh += len(hh)
    mt += len({q for q, _ in hh})
print(f"    模型側の分率 {len(vals)} 個 × QCD の数 {len(QCD)} 個 → 5% 以内の一致 {len(hits)} 組、当たった的 {len(hit_t)}/{len(QCD)}")
print(f"    同数の一様乱数で: 一致 {mh/R:.1f} 組、当たる的 {mt/R:.1f}/{len(QCD)}（2000 回の平均）")
check("一致の数は偶然の期待値と同程度（数値の一致は証拠にならない）", len(hit_t) >= mt / R - 1)
c5mid = float(av["C5"][2])
print(f"    例: C5 の中央の節の平均 3/32 = {c5mid:.4f} と χQCD18 のクォーク凝縮 0.09(2) ── この程度の一致は偶然で出る")

# ------------------------------------------------------------------------- H12
print("H12 中性子の寿命をうなりの包絡線（T1.6）と読むのに要る離調")
hbar = 6.582119569e-22                  # MeV s
m_n, m_p = 939.56542194, 938.27208943   # MeV（CODATA 2022）
tau_n = 878.4                           # s（PDG 2024、ボトル法の平均）
omega = m_n / hbar
need = 2*math.pi / (omega*tau_n)
have = (m_n - m_p) / m_n
print(f"    要る Δω/ω = {need:.3e}、(m_n − m_p)/m_n = {have:.3e}、開き 10^{math.log10(have/need):.1f}")
print(f"    質量差をうなりと読むと周期 {2*math.pi/(have*omega):.3e} s（実測 τ_n = {tau_n} s）")
check("23 桁以上外れる（T1.6 の μ と同じ型で閉じる）", math.log10(have/need) > 23)

# ------------------------------------------------------------------------- H13
print("H13 旧 K7 の異議: (c+s)³ の中央二項は A↔B で互いに移る ── 鎖では継ぎ目どうしが移るのが当然")
swap = lambda p: sp.expand(p.subs({cc: ss, ss: cc}, simultaneous=True))
check("P3 の中央二項 3c²s ↔ 3cs²、P4・C5 の継ぎ目 4c³s ↔ 4cs³・2c³s ↔ 2cs³",
      swap(3*cc**2*ss) == 3*cc*ss**2 and swap(P4c[1]) == P4c[3] and swap(C5c[1]) == C5c[3])

# ------------------------------------------------------------------------- H14
print("H14 端の節を二光束と読んだ可視度 V = 2√(I_A I_B)/(I_A + I_B)（T1.8）の位相平均")
cA = lambda t: (1 + mp.cos(t)) / 2
sB = lambda t: (1 - mp.cos(t)) / 2
V2 = mp.quad(lambda t: 2*cA(t)*sB(t) / (cA(t)**2 + sB(t)**2), [0, mp.pi/2, mp.pi, 3*mp.pi/2, 2*mp.pi]) / (2*mp.pi)
V4 = mp.quad(lambda t: 2*cA(t)**2*sB(t)**2 / (cA(t)**4 + sB(t)**4), [0, mp.pi/2, mp.pi, 3*mp.pi/2, 2*mp.pi]) / (2*mp.pi)
print(f"    E2・C5（端 ＝ TPE）: <V> = {mp.nstr(V2, 12)}（√2 − 1 = {mp.nstr(mp.sqrt(2) - 1, 12)}）")
print(f"    P4（端 ＝ c⁴, s⁴）  : <V> = {mp.nstr(V4, 12)}")
print("    中性子干渉計の実測コントラスト: 0.92（Huber ら 2024）、0.90（Heacock ら 2018、焼鈍後）")
print("    参考（電子）: Mach–Zehnder 干渉計の可視度 0.62（Ji ら 2003）── #38 は √2 − 1 を「普遍」と書く")
check("<V> は C5 で √2 − 1、P4 で 0.2346 ── どちらも 0.92 の半分未満",
      abs(V2 - (mp.sqrt(2) - 1)) < mp.mpf('1e-20') and abs(V4 - mp.mpf('0.2346')) < 5e-5 and V2 < 0.46)

# ------------------------------------------------------------------------- H15
print("H15 θ の入れ方: 四乗の項は半角 θ/2、交差の項は全角 θ（中心恒等式 cos⁴(θ/2) + sin⁴(θ/2) + ½sin²θ と同じ書き方）")
sh, ch = sp.sin(th / 2), sp.cos(th / 2)
mixed = {
    "C5": [ch**4, ch**4 * sp.sin(th)**2 / 2, sp.sin(th)**4 / 4, sh**4 * sp.sin(th)**2 / 2, sh**4],
    "P4": [ch**8, ch**4 * sp.sin(th)**2, sp.Rational(3, 8) * sp.sin(th)**4, sh**4 * sp.sin(th)**2, sh**8],
}
for name, terms in (("C5", C5), ("P4", P4)):
    check(f"{name} の混合形（半角の冪 × 全角の sin²θ）は各項ごとに一致",
          all(same(mixed[name][k], terms[k]) for k in range(5)))
four = {name: [fourier(t) for t in terms] for name, terms in (("C5", C5), ("P4", P4))}
for name in ("C5", "P4"):
    for k, f in enumerate(four[name]):
        print(f"    {name} 第{k + 1}項 = " + " + ".join(
            f"({a})" + ("" if n == 0 else f"cos{'' if n == 1 else n}θ") for n, a in sorted(f.items())))
check("倍角展開は cos θ … cos 4θ で打ち切れる（どの項も 4θ まで）",
      all(max(f) <= 4 for name in four for f in four[name]))
check("中央の主項は偶数倍角だけ（周期 π、2ω）、端と渡りは奇数倍角を含む（周期 2π）",
      all(n % 2 == 0 for name in four for n in four[name][2]) and
      all(any(n % 2 == 1 for n in four[name][q]) for name in four for q in (0, 1, 3, 4)))

# ------------------------------------------------------------------------- H16
print("H16 振幅平面（φ = θ/2）での主項の位置と対称性 ── 分数電荷に要る 1/3 周（ℤ₃）が無い")
ph = sp.symbols('phi', real=True)
C5phi = [t.subs(th, 2 * ph) for t in C5]
ANGP = [mp.mpf(k) / 11 for k in (1, 4, 6, 9, 13, 17, 20)]


def set_invariant(shift_fn):
    """項の集合が φ の変換で自分自身に写るか（各項の像が集合のどれかと一致）"""
    fs = [sp.lambdify(ph, f, 'mpmath') for f in C5phi]
    gs = [sp.lambdify(ph, shift_fn(f), 'mpmath') for f in C5phi]
    return all(any(max(abs(g(a) - f(a)) for a in ANGP) < mp.mpf('1e-25') for f in fs) for g in gs)


check("φ → φ + π/2（A↔B）と φ → −φ で項の集合は不変（二面体群 D₄）",
      set_invariant(lambda f: f.subs(ph, ph + sp.pi / 2)) and set_invariant(lambda f: f.subs(ph, -ph)))
check("φ → φ + 2π/3（1/3 周）では不変でない ── 分数電荷 e/3 の弧を主項の間に置けない",
      not set_invariant(lambda f: f.subs(ph, ph + 2 * sp.pi / 3)))
peaks = sorted({round(float(mp.findroot(sp.lambdify(ph, sp.diff(C5phi[2], ph), 'mpmath'), x0)), 6)
                for x0 in (0.7, 2.3, 3.9, 5.5)})
print(f"    中央の主項 KE² の極大 φ = {peaks}（π/4 の奇数倍、1/8 周ごとに主項が並ぶ）")
check("主項の極大は φ = 0, π/4, π/2, …（1/8 周の格子）",
      all(abs(p / (math.pi / 4) - round(p / (math.pi / 4))) < 1e-6 for p in peaks))

print("=" * 78)
print("全項目:", "OK" if all(ALL_OK) else "NG あり", f"（{sum(ALL_OK)}/{len(ALL_OK)}）")
