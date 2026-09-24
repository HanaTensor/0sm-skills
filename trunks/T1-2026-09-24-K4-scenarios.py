#!/usr/bin/env python3
"""
幹 T1 の K4（恒等式の E₀ はどの層か ＋ 核の空間トレース）── 選択肢ごとに結果がどう動くか（2026-09-24）

注意: 幹 T1 の本文は β_ZB の値を使わない方針だが、K4 の比較は幹 T3・T4 の数値を要するので、
このスクリプトだけは例外として β_ZB（#10 の β² = 0.00163798087）を使う。T1 の本文には定性的にのみ書く。
必要: mpmath
"""
import mpmath as mp
mp.mp.dps = 20

mec2 = mp.mpf('510.99895069')          # keV（CODATA 2022）
b2 = mp.mpf('0.00163798087'); beta = mp.sqrt(b2)
gam = 1/mp.sqrt(1 - b2)
ae = mp.mpf('0.00115965218062')        # a_e（CODATA 2022）
h_keVs = mp.mpf('4.135667696e-18')     # keV·s
G, c = mp.mpf('6.67430e-11'), mp.mpf('299792458')
me = mp.mpf('9.1093837139e-31'); lamC = mp.mpf('2.42631023538e-12')
nuZB = beta*c/lamC                     # #67 の定義 ν_ZB = v_ZB/λ_C

print("=== 0. 基準量（幹 T3 の三層）")
print(f"   β_ZB = {mp.nstr(beta,10)}   mc² = {mp.nstr(mec2,10)} keV")
print(f"   βmc² = {mp.nstr(beta*mec2,6)} keV = hν_ZB = {mp.nstr(h_keVs*nuZB,6)} keV  (ν_ZB = {mp.nstr(nuZB,5)} Hz)")
print(f"   ½β²mc² = {mp.nstr(b2*mec2/2*1000,6)} eV / (γ−1)mc² = {mp.nstr((gam-1)*mec2*1000,6)} eV / (a_e/√2)mc² = {mp.nstr(ae/mp.sqrt(2)*mec2*1000,6)} eV")

print("=== 1. T4.5 の重力波出力はどの質量で計算されていたか")
J3 = mp.mpf(4045)/4096; w = 2*mp.pi*nuZB
P = lambda M: G/(5*c**5)*mp.mpf(2)/3*(M*lamC**2)**2*w**6*J3
print(f"   P(M = m_e, d = λ_C, ω = 2πν_ZB) = {mp.nstr(P(me),4)} W  → T4.5 の 1.00×10⁻⁴³ W は M = m_e（E₀ = mc²）で計算されている")

print("=== 2. 四つの E₀ と二つの空間トレースで何が動くか")
S_M = -(mp.mpf(1)/2)*(1 + 405*mp.pi**2/256*b2)      # T4.3（物質）× E₀
S_R = mp.mpf(-2)                                   # T4.3（輻射）× E₀
cands = [
  ("E1  2mc²    (#43/#65: E₀ = ħω_Dirac-gap)", 2*mec2),
  ("E2  mc²     (#38)",                         mec2),
  ("E3  βmc²    (#46: E₀ = hν_ZB)",            beta*mec2),
  ("E4  β²mc²   (2026-09-06: 床 = (a_e/√2)mc²)", b2*mec2),
]
hdr = f"   {'選択肢':<44}{'E₀ [keV]':>12}{'床 E₀/2':>11}{'⟨S⟩物質':>11}{'⟨S⟩輻射':>11}{'ν=E₀/h [Hz]':>13}{'P_GW [W]':>11}{'v_max/c*':>9}"
print(hdr)
for name, E0 in cands:
    vmax = mp.sqrt(E0/mec2)                 # KE_max = E₀/2 を質量 m の ½mv² と読んだ場合
    print(f"   {name:<44}{mp.nstr(E0,6):>12}{mp.nstr(E0/2,6):>11}{mp.nstr(S_M*E0,5):>11}{mp.nstr(S_R*E0,5):>11}"
          f"{mp.nstr(E0/h_keVs,4):>13}{mp.nstr(P(me)*(E0/mec2)**2,3):>11}{mp.nstr(vmax,4):>9}")
print("   * v_max は恒等式の KE（最大 E₀/2）を電子の質量 m の運動エネルギー ½mv² と読んだ場合の最大速度（非相対論）")
print("   ⟨S⟩ の物質／輻射の比 =", mp.nstr(S_R/S_M, 6), "（T4.3 の「4 倍」）")

print("=== 3. 判定の材料（各選択肢と既存の記録の整合）")
rows = [
 ("B2 の和と差（⟨H⟩ = mc²D、振幅の和 = mc²）が E₀ と一致", ["×", "○", "×", "×"]),
 ("#1 の定義（KE = 核間の捕捉光子のエネルギー）と #46 の E₀ = ħω", ["×", "×", "○", "×"]),
 ("T4.1 の反跳（E_γ ≈ βmc²、反跳速度 v_ZB）と同じ層", ["×", "×", "○", "×"]),
 ("KE を質量 m の運動と読んで v_max = v_ZB", ["×(√2 c)", "×(c)", "×(√β c)", "○"]),
 ("T3 §4 の著者撤回「恒等式は mc² 尺度で適用されない」", ["×", "×", "○", "○"]),
 ("#65 の和解案（床 E₀/2 = 静止エネルギー mc²）", ["○", "×", "×", "×"]),
 ("ジューコフスキーの板 ±mc² の半長／全長と一致（T1.24–T1.25）", ["全長", "半長", "別の板", "別の板"]),
]
print(f"   {'材料':<52} E1     E2     E3     E4")
for k, v in rows:
    print(f"   {k:<52} " + "  ".join(f"{x:<6}" for x in v))

print("=== 4. 空間トレース（物質／輻射）")
print("   T4.3: 物質の読みの先頭項 −E₀/2 は T1.3 の調和振動子のビリアル 2⟨T⟩ = E_osc が要求する値と厳密に一致（E₀ に依らない）")
print("   輻射の読み −2E₀ は、核の輻射を領域の境界が閉じ込める場合。核が自己束縛（フォン・ラウエ）なら物質になる")
print("   外部の実測: 電子の D 項（重力形状因子）は QED で D(t→0) が発散し、実測もない ── 外から決める手段は現状ない")
