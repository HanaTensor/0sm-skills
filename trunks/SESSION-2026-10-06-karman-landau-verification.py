#!/usr/bin/env python3
"""
SESSION-2026-10-06-karman-landau-verification.py
================================================
2026-10-06 の壁練（カルマン渦列 → Landau → 0SM の時間位相と初期値の種）で
用いた検算をすべて一つにまとめた再現スクリプト。numpy / scipy のみを使う
（sympy は使わない）。各項目は OK / NG を印字する。

項目
  1. 恒等式の対称性と層の周期（θ → θ+π/2 不変、差 D は奇、エネルギー層は偶）
  2. #1 の式の再現（cos⁴(θ/2) − sin⁴(θ/2) = cos θ、grad(T_e2 − T_e1) = E₀ sin θ）
  3. 開始時刻の補題（遅い増幅器が速い種から拾う符号は cos χ ＝ D(t₀)）
  4. 数値（ZB 周期、進む距離、#1 の力の大きさ、Stern–Gerlach との比、σ/Ω 抑制）
  5. 一粒の Malus 検定（円周一様 ＝ 線形、Kochen–Specker 1967 ＝ cos²(a/2)）
"""
import numpy as np
try:
    from scipy import integrate
    def quad(f, a, b):
        return integrate.quad(f, a, b, limit=50000)[0]
    QUAD_NOTE = "scipy.integrate.quad"
except ImportError:                       # scipy の無い環境: 複合シンプソン（numpy のみ）
    def quad(f, a, b, n=4_000_001):
        t = np.linspace(a, b, n)
        y = f(t)
        h = (b - a) / (n - 1)
        return h / 3 * (y[0] + y[-1] + 4 * y[1:-1:2].sum() + 2 * y[2:-1:2].sum())
    QUAD_NOTE = "numpy 複合シンプソン（scipy 不在）"

OK = lambda c: "OK" if c else "NG"
print("=" * 72)

# ---------------------------------------------------------------- 1
print("[1] 恒等式の対称性と層の周期（幹の記法: θ、E0 = cos⁴θ + sin⁴θ + ½ sin²2θ）")
th = np.linspace(0, 4 * np.pi, 4001)
E0 = lambda t: np.cos(t) ** 4 + np.sin(t) ** 4 + 0.5 * np.sin(2 * t) ** 2
D = lambda t: np.cos(t) ** 4 - np.sin(t) ** 4            # 差（双極子層）
F4 = lambda t: np.cos(t) ** 4 + np.sin(t) ** 4           # エネルギー層
X = lambda t: 0.5 * np.sin(2 * t) ** 2                   # 交差項
e1 = np.max(np.abs(E0(th) - 1))
e2 = np.max(np.abs(E0(th + np.pi / 2) - E0(th)))
e3 = np.max(np.abs(D(th + np.pi / 2) + D(th)))           # 札の付け替え（半周期ずらし）で奇
e4 = np.max(np.abs(F4(th + np.pi / 2) - F4(th)))         # 偶
e5 = np.max(np.abs(D(th) - np.cos(2 * th)))              # D = cos 2θ（周期 π）
e6 = np.max(np.abs(F4(th) - (3 + np.cos(4 * th)) / 4))   # 周期 π/2
e7 = np.max(np.abs(X(th) - (1 - np.cos(4 * th)) / 4))
print(f"  E0 ≡ 1                          : {e1:.1e}  {OK(e1 < 1e-12)}")
print(f"  E0(θ+π/2) = E0(θ)（鏡映×半周期）: {e2:.1e}  {OK(e2 < 1e-12)}")
print(f"  D(θ+π/2) = −D(θ)（揚力 C_L, f0）: {e3:.1e}  {OK(e3 < 1e-12)}")
print(f"  F4(θ+π/2) = F4(θ)（抗力 C_D, 2f0）: {e4:.1e}  {OK(e4 < 1e-12)}")
print(f"  D = cos 2θ                       : {e5:.1e}  {OK(e5 < 1e-12)}")
print(f"  F4 = (3+cos 4θ)/4, X = (1−cos 4θ)/4: {max(e6, e7):.1e}  {OK(max(e6, e7) < 1e-12)}")
print("  → 振幅層 (cos θ, sin θ) は周期 2π で後流に対応物が無い。後流の複素振幅 A に対し")
print("    0SM の振幅 z = √A（A が一周する間に z は半周 ＝ Floquet −1 ＝ メビウス ＝ 720°）。")

# ---------------------------------------------------------------- 2
print("\n[2] #1 の式の再現（#1 の記法: θ = ωt は全角。核は θ/2 に乗る）")
th1 = np.linspace(0, 4 * np.pi, 4001)
Te1 = lambda t: np.cos(t / 2) ** 4                        # 核 A（x = +a）
Te2 = lambda t: np.sin(t / 2) ** 4                        # 核 B（x = −a）
h = 1e-6
dTe1 = (Te1(th1 + h) - Te1(th1 - h)) / (2 * h)
dTe2 = (Te2(th1 + h) - Te2(th1 - h)) / (2 * h)
g1 = np.max(np.abs(Te1(th1) - Te2(th1) - np.cos(th1)))
g2 = np.max(np.abs((dTe2 - dTe1) - np.sin(th1)))          # #1 eq. e3_simple_harmonic_motion
g3 = np.max(np.abs(dTe1 + 2 * np.cos(th1 / 2) ** 3 * np.sin(th1 / 2)))   # #1 eq. e3_gradT_e1
print(f"  cos⁴(θ/2) − sin⁴(θ/2) = cos θ   : {g1:.1e}  {OK(g1 < 1e-12)}")
print(f"  d/dθ[T_e2] − d/dθ[T_e1] = sin θ : {g2:.1e}  {OK(g2 < 1e-6)}   (#1 e3_simple_harmonic_motion)")
print(f"  d/dθ[T_e1] = −2cos³(θ/2)sin(θ/2) : {g3:.1e}  {OK(g3 < 1e-6)}   (#1 e3_gradT_e1)")
print("  → (D, F/E0) = (cos θ, sin θ) は複素振幅 E0·e^{iθ} の二つの直交成分。")
print("    F は全角（ベクトル, 2π）、核は半角（スピノル, 4π）── #1 本文の記述どおり。")

# ---------------------------------------------------------------- 3
print("\n[3] 開始時刻の補題：遅い増幅器（成長率 σ）が速い種 F0 sin(Ωt+χ) から拾う量")
print("    y(T) = ∫₀ᵀ e^{σ(T−t)} sin(Ωt+χ) dt")
print("         = e^{σT}[(σ sinχ + Ω cosχ) − e^{−σT}(σ sin(ΩT+χ) + Ω cos(ΩT+χ))]/(σ²+Ω²)")
s, Om, T = 1.0, 200.0, 10.0
worst = 0.0
rows = []
print(f"    （数値積分: {QUAD_NOTE}）")
for chi in [0.0, 0.3, 1.0, np.pi / 2, 2.0, 2.5, np.pi]:
    num = quad(lambda t: np.exp(s * (T - t)) * np.sin(Om * t + chi), 0, T)
    exact = np.exp(s * T) * ((s * np.sin(chi) + Om * np.cos(chi))
                             - np.exp(-s * T) * (s * np.sin(Om * T + chi) + Om * np.cos(Om * T + chi))) / (s * s + Om * Om)
    static = np.exp(s * T) / s                                   # 静的な種 1 に対する応答
    worst = max(worst, abs(num - exact) / abs(exact if exact != 0 else 1))
    rows.append((chi, num, exact, num / static, np.cos(chi) * s / Om))
print(f"  数値積分と閉じた式の一致（相対）: {worst:.1e}  {OK(worst < 1e-6)}")
print("    χ        y(T)数値      y(T)厳密     y/静的種     (σ/Ω)cos χ")
for chi, num, exact, r, pred in rows:
    print(f"  {chi:5.3f}  {num:12.4e}  {exact:12.4e}  {r:11.3e}  {pred:11.3e}")
print("  → 選ばれる符号は cos χ ＝ D(t₀)/E0 ＝ 到着時の光子球の位置（A 側か B 側か）。")
print("    χ = π/2（赤道、流れ F が最大、D = 0）で種は零。重みは静的な種の σ/Ω 倍。")

# ---------------------------------------------------------------- 4
print("\n[4] 数値")
hbar = 1.054571817e-34; me = 9.1093837015e-31; c = 2.99792458e8; e = 1.602176634e-19
muB = 9.2740100783e-24
mc2 = me * c ** 2; w = mc2 / hbar; W = 2 * w; T_ZB = 2 * np.pi / W
lamC = 2 * np.pi * hbar / (me * c)
F0 = mc2 / (lamC / 2)                                     # 勾配力の目安 D/(λ_C/2)
F_SG = muB * 1e3                                          # Stern–Gerlach, 10³ T/m
print(f"  ω = mc²/ħ = {w:.3e} rad/s, ZB 角周波数 2ω = {W:.3e} rad/s, T_ZB = {T_ZB:.3e} s")
print(f"  λ_C = {lamC:.3e} m, λ_C/2 = {lamC/2:.3e} m（光子球の変位の上限）")
for E in [100, 1e3, 1e4]:
    v = np.sqrt(2 * E * e / me)
    print(f"  E = {E:6.0f} eV: v = {v:.2e} m/s, 一周期に進む距離 {v*T_ZB:.2e} m, λ_C あたり {lamC/(v*T_ZB):.1f} 周期")
print(f"  #1 の力の目安 F0 = mc²/(λ_C/2) = {F0:.3e} N ／ SG 力 μ_B×10³ T/m = {F_SG:.3e} N ／ 比 {F0/F_SG:.1e}")
for sigma in [1e1, 1e5, 1e9]:
    print(f"  σ = {sigma:.0e} s⁻¹: 増幅器が拾う実効の種 F0·σ/Ω = {F0*sigma/W:.2e} N")

# ---------------------------------------------------------------- 5
print("\n[5] 一粒の Malus 検定（読み出し規則は Kármán ＝ KS の符号射影 sign(a·λ)）")
rng = np.random.default_rng(0)
N = 4_000_000
z = rng.uniform(-1, 1, N); ph = rng.uniform(0, 2 * np.pi, N); sn = np.sqrt(1 - z * z)
lam = np.stack([sn * np.cos(ph), sn * np.sin(ph), z], 1)       # S² 上一様
p = np.array([0.0, 0.0, 1.0])                                  # 準備方向
pl = lam @ p
wks = np.clip(pl, 0, None); wks /= wks.sum()                   # KS 1967: p 側半球で (p·λ) に比例
print("   a(度)   円周一様(線形)   KS 1967     cos²(a/2)")
worst_ks = 0.0; worst_lin = 0.0
for a_deg in [0, 30, 45, 60, 90, 120, 150, 180]:
    a = np.radians(a_deg); avec = np.array([np.sin(a), 0.0, np.cos(a)])
    out = (lam @ avec) > 0
    P_ks = (wks * out).sum()
    P_lin = 1 - a / np.pi                                      # 位相一様・符号読み出し（T7.1 と同型）
    mal = np.cos(a / 2) ** 2
    worst_ks = max(worst_ks, abs(P_ks - mal))
    worst_lin = max(worst_lin, abs(P_lin - mal) if a_deg not in (0, 90, 180) else 0)
    print(f"  {a_deg:5d}     {P_lin:.4f}        {P_ks:.4f}     {mal:.4f}")
print(f"  KS 1967 と cos²(a/2) の最大差: {worst_ks:.1e}  {OK(worst_ks < 2e-3)}")
print(f"  線形は 0, π/2, π 以外で余弦と食い違う（最大差 {worst_lin:.3f}）  {OK(worst_lin > 0.05)}")
print("  → 時間位相 φ だけでは Malus は出ない。向きの遅い変数（循環の軸 n̂、S² 上）が要る。")
print("    KS の二つの応答 {Θ(a·λ), Θ(−a·λ)} は半球の 1 の分割 ＝ T7 の K3「表と裏」。")
print("=" * 72)
