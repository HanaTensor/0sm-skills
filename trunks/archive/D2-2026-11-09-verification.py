"""D2（環境エクセルギーの台帳）2026-11-09 の検算 E1–E8。
外部入力は CODATA 2018 の定義値と、本文 §1 に挙げた文献値のみ。
"""
import numpy as np
from scipy.integrate import quad

h = 6.62607015e-34; k = 1.380649e-23; c = 2.99792458e8
sig = 5.670374419e-8; R = 8.314462618; g = 9.80665
cp_air = 1005.0; M_w = 0.018015; R_E = 6.371e6

def B_nu(nu, T):
    """分光放射輝度（両偏光）W m^-2 sr^-1 Hz^-1"""
    return 2*h*nu**3/c**2/np.expm1(h*nu/(k*T))

# E1 熱の通貨：kT/h
print("E1 kT/h (300 K) = %.3f THz" % (k*300/h/1e12))

# E2 大気の窓 8–13 µm が 300 K 黒体放射に占める割合
n1, n2 = c/13e-6, c/8e-6
P_win = np.pi*quad(B_nu, n1, n2, args=(300.0,))[0]
print("E2 8-13 um emission (300 K) = %.1f W/m2, fraction = %.3f" % (P_win, P_win/(sig*300**4)))

# E3 地球の外向き長波放射の総量（平均 240 W/m2）
print("E3 Earth OLR = %.2e W" % (240*4*np.pi*R_E**2))

# E4 サブテラヘルツの窓（0.15–0.25 THz、ΔT = 250 K、Rayleigh–Jeans、半球）
P_sub = np.pi*quad(lambda n: 2*n**2*k*250/c**2, 0.15e12, 0.25e12)[0]
print("E4 sub-THz window net flux bound = %.2e W/m2  (旧記載 3 mW/m2 を訂正)" % P_sub)

# E5 E4 と E2 の比（周波数の二乗で落ちる）
print("E5 ratio sub-THz / IR window = %.1e" % (P_sub/P_win))

# E6 湿度のエクセルギー（25 °C、相対湿度 50%）
T = 298.15
for phi in (0.3, 0.5, 0.8):
    ex = R*T*np.log(1/phi)/M_w
    print("E6 phi=%.1f: %.1f kJ/kg, equivalent head %.2f km" % (phi, ex/1e3, ex/g/1e3))

# E7 浮力機関の効率の上限 η ≈ gH/(cp T)（上昇気流塔の標準式、下降流にも同形）
for H in (200, 1000):
    eta = g*H/(cp_air*288)
    print("E7 H=%4d m: eta_max = %.4f ; x 80 W/m2 radiative cooling -> %.2f W/m2" % (H, eta, 80*eta))

# E8 ニュートリノ：D1 の値を引用（再計算しない）。比較のための単位換算のみ
print("E8 solar nu energy flux ~ 30 W/m2 (2% of L_sun) ; D1.16: 2.4e-25 W/kg (pure Gd)")

# ---- 同日追記（レーザーで結ぶ案・軌道上データセンター・電子版レーザー）----
# E9 天頂を中心とする半頂角 θ の円錐への正味放射の取り分 sin²θ（全天 80 W/m² を基準）
for name, th in (("hemisphere", np.pi/2), ("45 deg", np.pi/4), ("10 deg", np.radians(10)), ("1 mrad", 1e-3)):
    f = np.sin(th)**2
    print("E9 %-10s fraction %.2e -> %.2e W/m2" % (name, f, 80*f))

# E10 軌道上の放熱板（放射率 0.9、片面、地球と太陽の入射は無視）。面積あたり出力が最大になる T_c = 3/4 T_h
eps = 0.9; Q = 1e6; Th = 350.0; Tc = 0.75*Th
A0 = Q/(eps*sig*Th**4); W = Q*(1-Tc/Th); A1 = (Q-W)/(eps*sig*Tc**4)
print("E10 1 MW waste heat at 350 K: direct %.0f m2 ; with Carnot engine %.0f m2, work %.0f kW ; solar for same work ~%.0f m2 (300 W/m2 electric)"
      % (A0, A1, W/1e3, W/300))

# E11 電子版レーザー（D3 候補）: 内部時計 hν_ZB と、運動による時計のばらつき hν·β²/2
hev = 4.135667696e-15; E = hev*5.0e18
print("E11 h nu_ZB = %.0f eV" % E)
for name, v in (("Cu vF", 1.57e6), ("Fe vF", 1.98e6), ("Nb vF", 1.37e6), ("thermal e 300K", 1.17e5)):
    print("E11 %-15s spread %.3g eV" % (name, E*(v/c)**2/2))
print("E11 monochromatic beam dE=0.3 eV: spread %.3g eV" % (E*0.3/510998.95))
