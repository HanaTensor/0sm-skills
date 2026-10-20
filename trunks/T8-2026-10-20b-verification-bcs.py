"""
幹 T8 の T8.12「超伝導が与える境界条件」（T8-2026-10-20b-gravity-clock.md）の検算。
節記号 W1–W9 は幹 T8 の §4 と対応する。V1–V14 は T8-2026-10-20-verification.py。
定数と規約は V1–V14 と同じ（d = λ_C/2、ν_ZB = βν_C）。
実行: python3 -I T8-2026-10-20b-verification-bcs.py   （全 14 項目 OK で終わる）
"""
import math
import sympy as sp

h = 6.62607015e-34; hbar = h / (2 * math.pi); c = 299792458.0; e = 1.602176634e-19
me = 9.1093837015e-31; g0 = 9.80665; kB = 1.380649e-23
beta = math.sqrt(0.00163798087)
nuC = me * c**2 / h

ok = 0
def check(label, cond):
    global ok
    assert cond, label
    ok += 1
    print(f"  OK  {label}")

# ---- W1 BdG（Nambu）: H = ξτ_z + Δτ_x の基底状態 (u, v) = (cos θ, sin θ) ----
print("W1 BdG の混合角と 0SM の恒等式の層")
th = sp.Symbol('theta', real=True)
u, v = sp.cos(th), sp.sin(th)
xi, Dl = sp.symbols('xi Delta', positive=True)
E = sp.sqrt(xi**2 + Dl**2)
H = sp.Matrix([[xi, Dl], [Dl, -xi]])
evals = H.eigenvals()
check("固有値 ±√(ξ² + Δ²)（Dirac の ±√(p²c² + m²c⁴) と同じ形 ＝ Nambu の類比）",
      set(sp.simplify(k) for k in evals) == {E, -E})
check("(u² + v²)² = u⁴ + v⁴ + 2u²v²、2u²v² = ½ sin²2θ（0SM の恒等式 E₀ の三項）",
      sp.simplify(sp.expand((u**2 + v**2)**2) - (u**4 + v**4 + 2 * u**2 * v**2)) == 0
      and sp.simplify(2 * u**2 * v**2 - sp.sin(2 * th)**2 / 2) == 0)
check("差 D = u² − v² = cos 2θ（0SM の T1.3 の差 D ＝ BdG の ξ/E）",
      sp.simplify(u**2 - v**2 - sp.cos(2 * th)) == 0)

# ---- W2 コヒーレンス因子: 同じエネルギーの二状態 k, k′（ξ′ = ±ξ）で平均 ----
print("W2 コヒーレンス因子（ξ′ = +ξ と ξ′ = −ξ の平均）")
uk, vk = u, v
same = {'u2': uk, 'v2': vk}        # ξ′ = +ξ
flip = {'u2': vk, 'v2': uk}        # ξ′ = −ξ（u と v が入れ替わる）
caseI = sp.simplify(((uk * same['u2'] - vk * same['v2'])**2 + (uk * flip['u2'] - vk * flip['v2'])**2) / 2)
caseII = sp.simplify(((uk * same['u2'] + vk * same['v2'])**2 + (uk * flip['u2'] + vk * flip['v2'])**2) / 2)
print(f"    I（超音波減衰の型）= {sp.simplify(caseI)}、II（NMR 緩和の型）= {sp.simplify(caseII)}")
check("I = ½ − ½ sin²2θ、II = ½ + ½ sin²2θ（交差項 ½ sin²2θ が二つの型を分ける干渉項）",
      sp.simplify(caseI - (sp.Rational(1, 2) - sp.sin(2 * th)**2 / 2)) == 0
      and sp.simplify(caseII - (sp.Rational(1, 2) + sp.sin(2 * th)**2 / 2)) == 0)
check("ξ′ = +ξ だけなら II = E₀ = 1、I = D²", sp.simplify((u * u + v * v)**2 - 1) == 0
      and sp.simplify((u * u - v * v)**2 - sp.cos(2 * th)**2) == 0)

# ---- W3 対の振幅と数のゆらぎ（一つの対モード、占有 0 か 1） ----
print("W3 対モード: ⟨b⟩ = uv、Var(N_pair) = u²v²")
amp2 = (u * v)**2
var = v**2 - v**4
check("|⟨b⟩|² = Var(N_pair) = ¼ sin²2θ → 交差項 ½ sin²2θ = 2|⟨b⟩|² = 2 Var(N_pair)",
      sp.simplify(amp2 - var) == 0 and sp.simplify(sp.sin(2 * th)**2 / 2 - 2 * var) == 0)

# ---- W4 Nambu の辞書で 0SM の電子を読むと（形式上の対応のみ） ----
print("W4 sin 2θ₀ = β を BdG に置くと")
s2 = beta; c2 = math.sqrt(1 - beta**2)
print(f"    ξ/Δ = cot 2θ₀ = {c2/s2:.3f}、v² = sin²θ₀ = {(1-c2)/2:.3e}、mc²(1 − cos 2θ₀) = {me*c**2*(1-c2)/e:.1f} eV")
check("0SM の電子は Fermi 面から 24.7 ギャップ離れたモードに当たる（≈ 1/β）", abs(c2 / s2 - 1 / beta) / (1 / beta) < 1e-3)

# ---- W5 重力と Josephson: Jain・Lukens・Tsai 1987（高さ 7.2 cm） ----
print("W5 高さ H の二接合: Cooper 対（2m, 2e）の静止エネルギーの赤方偏移")
H = 0.072
dE_pair = 2 * me * g0 * H
V_eq = dE_pair / (2 * e)
f_J = 2 * e * V_eq / h
f_C = 2 * nuC * g0 * H / c**2
print(f"    2mgH = {dE_pair:.3e} J、等価な電位差 mgH/e = {V_eq:.3e} V、Josephson 周波数 2eV/h = {f_J:.1f} Hz")
print(f"    対の Compton の刻みのうなり 2ν_C gH/c² = {f_C:.1f} Hz、ZB の刻みなら β 倍 = {beta*f_C:.1f} Hz")
check("Josephson 周波数 ＝ 対の Compton の刻みのうなり（T8.3 を Josephson で読んだもの）", abs(f_J - f_C) / f_C < 1e-9)
check("ZB の刻みなら 1/25 → 約 4% の一致で排除（T8.5 の二つ目の実験の足場）", (1 - beta) / 0.04 > 20)

# ---- W6 導体の中の電場（Klein の関係 μ√g00 = 一定 の静止エネルギー分） ----
print("W6 平衡: 静止エネルギーの赤方偏移を電位が埋める")
E_SB = me * g0 / e
print(f"    E = mg/e = {E_SB:.3e} V/m（Schiff–Barnhill）、1 m で {E_SB:.3e} V")
check("電子 1 個でも Cooper 対でも同じ場（2m/2e = m/e）", abs((2 * me * g0) / (2 * e) - E_SB) < 1e-30)

# ---- W7 精密な普遍定数 ----
print("W7 超伝導が与える普遍定数")
KJ = 2 * e / h; Phi0 = h / (2 * e)
print(f"    K_J = 2e/h = {KJ/1e9:.4f} GHz/V（SI 2019 で厳密）、Φ₀ = h/2e = {Phi0:.5e} Wb")
omega = 2 * math.pi * 100
B_L = 2 * me * omega / e
print(f"    London モーメント B = 2mω/e（100 Hz の回転）= {B_L:.3e} T")
tate, theo = 1.000084, 0.999992
print(f"    Tate ら 1989: m*/2m_e = 1.000084(21)、理論 0.999992 → 差 {(tate-theo)*1e6:.0f} ppm（{(tate-theo)/21e-6:.1f}σ、未解決）")
check("Φ₀ · K_J = 1", abs(Phi0 * KJ - 1) < 1e-12)

# ---- W8 尺度の隔たり（T2.13 (c) の照合） ----
print("W8 0SM の内部の尺度と BCS の尺度")
Delta_Nb = 1.55e-3 * e
ratio = beta * me * c**2 / Delta_Nb
print(f"    βmc² / Δ(Nb, 1.55 meV) = {ratio:.2e}（{math.log10(ratio):.1f} 桁）")
print(f"    ν_ZB / (2Δ/h) = {beta*nuC/(2*Delta_Nb/h):.2e}")
check("隔たりは約 7 桁（T2.13 (c) の「22 桁」は算術の誤り）", 6.5 < math.log10(ratio) < 7.5)

# ---- W9 規格化が「引き込み」なら: 重力の離調で二核の位相差が静的にずれる大きさ ----
print("W9 二核の離調 Δω/ω = g d/c²（引き込みの強さを ω 程度と置いた場合の静的なずれ ε）")
d = h / (me * c) / 2
for name, gg in (("地表", g0), ("中性子星表面", 1e12), ("剛体限界 4c²/λ_C", 4 * c**2 / (2 * d))):
    eps = gg * d / c**2
    dq = eps**2 / 2 if eps < 1e-4 else 1 - math.cos(eps)     # 小角では ε²/2（浮動小数の桁落ちを避ける）
    print(f"    {name}: g = {gg:.2e} m/s²、ε ≈ {eps:.2e}、電荷 Q = cos ε の減り ≈ {dq:.1e}")
check("地表で ε ~ 1e-28（重力の実験では「制約か引き込みか」は決まらない）", 1e-29 < g0 * d / c**2 < 1e-27)
check("剛体限界では ε = 2（O(1)）", abs(4 * c**2 / (2 * d) * d / c**2 - 2) < 1e-12)

print(f"\n全 {ok} 項目 OK")
