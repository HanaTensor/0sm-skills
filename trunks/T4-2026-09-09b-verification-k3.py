# -*- coding: utf-8 -*-
"""
幹 T4（2026-09-09b 改訂）の K3 セッションで確定した数値の再現。
初版の T4-2026-09-09-verification.py を置き換えるものではなく、補うもの。
本script が再現するのは T4.4（修正した設計曲線）・T4.18（再結合と部位破壊）・
T4.19（実測 k_off と参照類）・§4.2（訂正の定量）である。

外部入力（2026年9月時点）:
  LanM-Tb  k_off = 0.033 s^-1 (T41W), 0.049/0.020 (T90W)  : Featherston, Issertell,
           Cotruvo, J. Am. Chem. Soc. 143 (2021). 停止流蛍光 + EGTA 挑戦, pH 7.2, 25 C.
  Kd(WT,Tb) = 7.3 +- 0.9 pM                                : 同上
  Gd-DOTA  k_obs(pH 7, 25 C) ~ 5e-13 s^-1                  : Ln-DOTA 速度論のまとめ値
  タンパク質の動的転移 T_D ~ 180 K (200-240 K とも)          : Doster ら Nature 337 (1989) ほか
実行: python3 T4-2026-09-09b-verification-k3.py
"""
import numpy as np

kB   = 8.617333262e-5      # eV/K
T0   = 298.15              # K
YR   = 3.155693e7          # s
NU0  = 1e13                # s^-1  結合振動の前指数因子（規約）
NMOL = 1000/12000*6.02214076e23   # 12 kDa の分子が 1 kg に何個  -> 5.0e22

def barrier(k, T=T0, nu0=NU0):   return kB*T*np.log(nu0/k)
def rate(dG, T, nu0=NU0):        return nu0*np.exp(-dG/(kB*T))
def hdr(t): print("\n"+"="*72+"\n"+t+"\n"+"="*72)

# --------------------------------------------------------------- T4.19
hdr("T4.19  実測 k_off から出る障壁")
print(f"1 kg あたりの分子数 N = {NMOL:.3e}  (幹 §3 の 5.0e22)")
for k,lab in [(0.033,"T41W"),(0.049,"T90W 速い相"),(0.020,"T90W 遅い相")]:
    print(f"  {lab:12s} k_off={k:6.3f}/s  半減期={np.log(2)/k:5.1f} s  dG*={barrier(k):.3f} eV")
kOFF = 0.033; DG_M = barrier(kOFF)
Kd   = 7.3e-12; kON = kOFF/Kd
print(f"\n  Kd = {Kd*1e12:.1f} pM -> k_on = {kON:.2e} /M/s  (拡散律速の級)")
print(f"  内訳 dG*_off = dG_bind({-kB*T0*np.log(Kd):.3f}) + dG*_on({kB*T0*np.log(NU0/kON):.3f}) = {DG_M:.3f} eV")
print(f"  初版の仮定 0.714 eV との差 = {DG_M-0.714:+.3f} eV  (会合障壁にほぼ等しい = 保守側に外れていた)")

# --------------------------------------------------------------- T4.4
hdr("T4.4  修正した設計曲線  dG/kT = ln(nu0 * N / R)")
print("初版: 分子あたり半減期 10 年  ->  dG/kT = ln(nu0*10yr/ln2) = %.1f  (線源に依存しない=誤り)"
      % np.log(NU0*10*YR/np.log(2)))
coef={}
for R,lab in [(3.82e4,"原子炉 10 m（実標的）"),(42.0,"核破砕 20 m（実標的）"),(3.00,"太陽（実標的）")]:
    Rs=R/YR; x=np.log(NU0*NMOL/Rs); coef[lab]=kB*x
    print(f"  {lab:22s} R={R:9.3g}/kg年  必要率/分子={Rs/NMOL:.2e}/s  dG/kT={x:.1f}  T_max=dG/{kB*x*1e3:.2f} meV")
C_NEW=coef["原子炉 10 m（実標的）"]; C_OLD=kB*np.log(NU0*10*YR/np.log(2))
print(f"\n  係数: 初版 {C_OLD*1e3:.2f} -> 修正 {C_NEW*1e3:.2f} meV/K  (比 {C_NEW/C_OLD:.2f})")
print("\n  障壁 / 修正 T_max / 初版 T_max")
for g,lab in [(4.30,"C-H"),(3.60,"C-C 共有結合"),(2.20,"S-S ジスルフィド"),(1.50,"Gd-DOTA 級"),
              (DG_M,"LanM 実測"),(0.714,"初版の仮定"),(0.607,"逆配列ペプチド推定"),(0.406,"初版 EF4-Rmod"),(0.200,"水素結合")]:
    flag = "  <- 室温を割った" if 273<g/C_OLD and g/C_NEW<300 else ""
    print(f"    {g:5.3f} eV  {lab:16s} {g/C_NEW:7.1f} K  ({g/C_OLD:7.1f} K){flag}")

hdr("T4.4(b)  前指数因子の幅 — 実測 k_off(298 K) を錨にした外挿")
kreq=(3.82e4/YR)/NMOL
for A in [1e13,1e11,1e9,1e6]:
    Tlim=T0*np.log(A/kOFF)/np.log(A/kreq)
    Ea=kB*T0*np.log(A/kOFF)
    d77=A*np.exp(-Ea/(kB*77))*NMOL*YR
    print(f"  A={A:.0e}: Ea={Ea:.4f} eV  動作温度上限={Tlim:6.1f} K  77 K の暗計数={d77:.2e}/kg年")
print("  -> 液体窒素 77 K が足りるかは前指数因子ひとつで決まる。これが K3 に残された実質。")

hdr("T4.4  暗計数（/kg年）。信号 = 3.82e4/kg年（原子炉 10 m 実標的）")
for dG,lab in [(3.60,"C-C 3.60 eV"),(DG_M,"LanM %.3f eV"%DG_M),(1.50,"Gd-DOTA 1.50 eV")]:
    row=" ".join(f"{T}K:{rate(dG,T)*NMOL*YR:.1e}" for T in (300,200,112,77))
    print(f"  {lab:18s} {row}")

hdr("T4.4(c)  温度安定度の要求  dlnk/dT = dG/(k T^2)")
for dG,T in [(DG_M,112),(DG_M,77),(3.60,300)]:
    sl=dG/(kB*T*T); print(f"  dG={dG:.3f} eV, T={T:3d} K : {sl:.3f}/K -> 暗計数 1% に許される揺らぎ {0.01/sl*1e3:.1f} mK")

hdr("T4.19  熱解離の半減期（実測 0.857 eV, nu0=1e13）")
for T in [310,298,250,200,150,112,77]:
    th=np.log(2)/rate(DG_M,T)
    u=f"{th:.3g} s" if th<3600 else (f"{th/3600:.3g} h" if th<YR else f"{th/YR:.3g} 年")
    print(f"  {T:4d} K : {u}")

# --------------------------------------------------------------- T4.18
hdr("T4.18  再結合と部位破壊")
V=(1e-9)**3*1000                      # 1 nm^3 を L で
c_eff=1/6.02214076e23/V
print(f"  空の配位圏が 1 nm 隣  -> 実効濃度 {c_eff:.2f} M")
print(f"  再結合速度 = k_on * c_eff = {kON*c_eff:.2e}/s  ->  時定数 {1/(kON*c_eff)*1e12:.0f} ps")
print("  井戸の深さは再結合を止めない。止めるのは部位の破壊である。\n")
print("  反跳 / 3.6 eV 換算の本数 / T4.9 の痕跡 / 判定")
for E,tr,lab in [(2.4,1,"太陽"),(121,34,"原子炉 10 m"),(12100,3350,"核破砕 20 m")]:
    n=E/3.6
    print(f"    {lab:12s} {E:8.1f} eV  {n:8.1f} 本  {tr:5d} 箇所  {'掛からない' if n<3 else '掛かる'}")

hdr("T4.14 / K4  閾値の梃を実効閾値で引き直す")
print("  基準: XENONnT の電子反跳閾値 1 keV。dsigma/dT ∝ 1/T なので率の比 = 1000/閾値[eV]")
print("  mu_nu 上限の改善は率の比の平方根（背景一定として）。実験室最良 2.9e-11、天体物理 1.5e-12 mu_B")
for th,lab in [(0.41,"初版の主張 0.41 eV"),(15,"単一電離 ~15 eV"),(25,"部位破壊 ~25 eV")]:
    r=1000/th; print(f"    {lab:22s} 率 {r:7.0f} 倍  mu 改善 {np.sqrt(r):5.1f} 倍  -> {2.9e-11/np.sqrt(r):.2e} mu_B"
                     f"  {'天体物理を下回る' if 2.9e-11/np.sqrt(r)<1.5e-12 else '天体物理には届かない'}")
print("\n完了。すべて numpy のみで再現。外部入力は 2026年9月時点であり、論文化の際は引き直すこと。")
