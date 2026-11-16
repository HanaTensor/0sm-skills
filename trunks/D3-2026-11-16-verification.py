"""D3（内部時計の位相をそろえる装置／チャネリング共鳴）2026-11-16 の検算 F1–F6。
外部入力は CODATA の定義値・推奨値、結晶の格子定数（文献値）、先例実験の数値（本文 §1）のみ。
仮定: 内部時計は固有時の時計として実験室系で 1/γ に遅れる（de Broglie の時計と同じ扱い）。
"""
import numpy as np

me = 0.51099895          # MeV
lam_C = 2.42631024e-12   # m（コンプトン波長 h/mc）
beta = 0.040472          # β_ZB（#10 の正準値）
h_eVs = 4.135667696e-15
c = 2.99792458e8

# F1 共鳴条件: 時計一周期に進む距離 = 原子列の間隔 d
#     d = v/ν_lab = γv/ν  →  p = m ν d  →  pc = mc² · (ν/ν_C) · d/λ_C
crystals = {"Si<110>": 3.840e-10, "Si<100>": 5.431e-10, "Ge<110>": 4.000e-10, "C(diamond)<110>": 2.522e-10}
print("F1 resonant momentum (MeV/c) and kinetic energy (MeV)")
for name, d in crystals.items():
    for lab, f in (("nu_C", 1.0), ("2nu_C (Dirac ZB)", 2.0), ("nu_ZB", beta), ("nu_ZB x1/2", beta/2), ("nu_ZB x2", 2*beta)):
        p = me*f*d/lam_C
        T = np.sqrt(p*p + me*me) - me
        print("   %-16s %-18s p = %8.3f  T = %8.3f" % (name, lab, p, T))

# F2 予言の形: 同じ結晶での二つの共鳴の比は β_ZB（結晶に依らない）
p_C = me*crystals["Si<110>"]/lam_C
p_Z = beta*p_C
print("F2 ratio p_ZB/p_C = %.6f (= beta_ZB), 1/ratio = %.3f (non-integer)" % (p_Z/p_C, p_C/p_Z))

# F3 先例の高調波との分離: 共鳴は p_k = p_res/k にも立ちうる（Rivas の p_k = 161.748/k）
print("F3 nearest harmonics of known lines to p_ZB = %.4f MeV/c" % p_Z)
for lab, base in (("nu_C", p_C), ("2nu_C", 2*p_C)):
    k = int(round(base/p_Z))
    for kk in (k-1, k, k+1):
        print("   %-6s k=%2d : %.4f MeV/c (%+.2f %%)" % (lab, kk, base/kk, (base/kk - p_Z)/p_Z*100))

# F4 先例（Gouanère et al. 2005）の数値
print("F4 precedent: predicted 80.874, observed dip 81.1 MeV/c -> shift %.2f %% (calibration limit 0.3 %%), dip 8 %%" % ((81.1-80.874)/80.874*100))

# F5 内部時計の量子と振動数
print("F5 nu_C = %.4e Hz, nu_ZB = %.3e Hz, h nu_ZB = %.2f keV" % (me*1e6/h_eVs, beta*me*1e6/h_eVs, beta*me*1e3))

# F6 運動による時計のばらつき h nu_ZB beta_e^2/2（D2 E11 を再掲）
E = beta*me*1e6
for name, v in (("Cu vF", 1.57e6), ("Fe vF", 1.98e6), ("Nb vF", 1.37e6), ("thermal e 300K", 1.17e5)):
    print("F6 %-15s spread %.3g eV" % (name, E*(v/c)**2/2))
print("F6 monochromatic beam dE = 0.3 eV: spread %.3g eV" % (E*0.3/(me*1e6)))
