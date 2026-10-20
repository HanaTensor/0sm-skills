"""
幹 T8「重力と内部時計」（T8-2026-10-20-gravity-clock.md）の検算。
節記号 V1–V12 は幹 T8 の §4 と対応する（命題との対応は §4 の各行に書いてある）。

前提（量子重力の論文は使わない。幾何学の部分のみ）
  - 二核 A・B の間隔 d = λ_C/2（固有長）、1 サイクル = 1 往復、ν_ZB = βc/λ_C（T3 の K1、2026-10-11 確定分）
  - β = 0.04047（#10、β² = 0.00163798087）は局所不変量（T3 §現在地、LPI）
  - h = 一回の受け渡しの作用（T5.13）
実行: python3 -I T8-2026-10-20-verification.py   （全項目 OK で終わる）
"""
import math
import sympy as sp

# ---- 定数（CODATA 2018 の定義値・推奨値） ----
h    = 6.62607015e-34
hbar = h / (2 * math.pi)
c    = 299792458.0
kB   = 1.380649e-23
G    = 6.67430e-11
e    = 1.602176634e-19
eps0 = 8.8541878128e-12
me   = 9.1093837015e-31
g0   = 9.80665
GM_E = 3.986004418e14
R_E  = 6.371e6
beta = math.sqrt(0.00163798087)

ok_count = 0
def check(label, cond):
    global ok_count
    assert cond, label
    ok_count += 1
    print(f"  OK  {label}")

def rel(a, b):
    return abs(a - b) / abs(b)

lamC  = h / (me * c)          # Compton 波長
lamCb = hbar / (me * c)       # 換算 Compton 波長
d     = lamC / 2              # 核間隔（固有長）
nuC   = me * c**2 / h         # Compton 振動数
nuZB  = beta * c / lamC       # 内部線（1 往復 = 1 サイクル）
lP    = math.sqrt(hbar * G / c**3)

print("V1  0SM の基本量")
print(f"    β = {beta:.6f}, λ_C = {lamC:.5e} m, d = λ_C/2 = {d:.5e} m")
print(f"    ν_C = {nuC:.5e} Hz, ν_ZB = βν_C = {nuZB:.5e} Hz, hν_ZB = {h*nuZB/e/1e3:.3f} keV")
check("ν_ZB = 5.00e18 Hz", rel(nuZB, 5.00e18) < 1e-3)
check("hν_ZB = βmc² = 20.68 keV（第二層）", rel(h * nuZB / e, 20.68e3) < 1e-3)

# ---- V2 境界条件: 移送時計の周期は g00 だけで決まる（係数 1）。座標間隔を固定すると係数 2 ----
print("V2  境界条件（指針 1）: 等方座標 ds² = −A c²dt² + B dx²、A = 1+2φ、B = 1−2φ（φ = Φ/c² < 0）")
phi = sp.Symbol('phi', negative=True)
L, v = sp.symbols('L v', positive=True)
A = 1 + 2 * phi
B = 1 - 2 * phi
coord_speed = v * sp.sqrt(A / B)              # 局所速さ v の信号の座標速さ（光でも βc でも同じ形）
T_proper_sep = 2 * (L / sp.sqrt(B)) / coord_speed    # 核間隔が固有長 L
T_coord_sep  = 2 * L / coord_speed                   # 核間隔が座標長 L（屈折率だけを効かせた読み）
s1 = sp.series(sp.simplify(T_proper_sep / (2 * L / v)), phi, 0, 2).removeO()
s2 = sp.series(sp.simplify(T_coord_sep / (2 * L / v)), phi, 0, 2).removeO()
print(f"    固有長で置いた周期 / 局所周期 = {sp.simplify(T_proper_sep/(2*L/v))}  ≈ {s1}")
print(f"    座標長で置いた周期 / 局所周期 ≈ {s2}")
ratio = sp.lambdify(phi, T_proper_sep / (2 * L / v) * sp.sqrt(A))
check("固有長の核間隔 → 周期 ∝ 1/√A（係数 1、種に依らない）",
      sp.simplify(s1 - (1 - phi)) == 0 and all(abs(ratio(x) - 1) < 1e-12 for x in (-1e-9, -1e-3, -0.2)))
check("座標長の核間隔 → 一次の係数が 2（#63 の局所読みと同じ形、Lange 2021 で 10⁸ 倍排除）",
      sp.simplify(s2 - (1 - 2 * phi)) == 0)

# ---- V3 高度による内部時計のずれ ----
print("V3  高度によるずれ（地表基準、重力分のみ）")
dphi_1m = g0 * 1.0 / c**2
dphi_400 = GM_E * (1 / R_E - 1 / (R_E + 400e3)) / c**2
print(f"    1 m: Δν/ν = {dphi_1m:.4e}, Δν_C = {nuC*dphi_1m:.1f} Hz, Δν_ZB = {nuZB*dphi_1m:.1f} Hz")
print(f"    400 km: ΔΦ/c² = {dphi_400:.4e}, Δν_ZB = {nuZB*dphi_400/1e6:.1f} MHz")
check("400 km で Δν_ZB ≈ +205.6 MHz（T3 §3 と一致）", abs(nuZB * dphi_400 / 1e6 - 205.6) < 0.5)

# ---- V4 断熱性: 降下で量子数は変わらない ----
print("V4  断熱パラメータ (dω/dt)/ω² = g v/(c² ω)")
for vv in (1.0, 1e3):
    for name, nu in (("Compton", nuC), ("ZB", nuZB)):
        eta = g0 * vv / (c**2 * 2 * math.pi * nu)
        print(f"    v = {vv:g} m/s, {name}: {eta:.2e}")
eta_max = g0 * 1e3 / (c**2 * 2 * math.pi * nuZB)
check("断熱パラメータ < 1e-30（遷移は起きない＝作用 E/ν は保存）", eta_max < 1e-30)

# ---- V5 降下で手放すエネルギー = h × うなり振動数 ----
print("V5  電子を 1 m 降ろす")
dE = me * g0 * 1.0
dnu = nuC * dphi_1m
print(f"    mgΔh = {dE:.4e} J = {dE/e:.3e} eV")
print(f"    h Δν_C = {h*dnu:.4e} J、うなりの周期 1/Δν_C = {1/dnu*1e6:.1f} μs")
print(f"    ZB で数えると (h/β)Δν_ZB = {h/beta*nuZB*dphi_1m:.4e} J")
check("mgΔh = h Δν_C（作用は 1 サイクルあたり h のまま）", rel(dE, h * dnu) < 1e-9)
check("ΔE × (うなりの周期) = h", rel(dE / dnu, h) < 1e-9)

# ---- V6 電磁放射では運べない ----
print("V6  a = g の Larmor 出力と、降下の仕事率 mgv")
P_L = e**2 * g0**2 / (6 * math.pi * eps0 * c**3)
P_W = me * g0 * 1.0
print(f"    Larmor = {P_L:.3e} W、mgv(1 m/s) = {P_W:.3e} W、比 = {P_L/P_W:.2e}")
check("放射が運べるのは仕事率の 1e-20 未満 → エネルギーは力（仕事）の経路で出る", P_L / P_W < 1e-20)

# ---- V7 二核のうなりから力: F = h Δν_AB / d ----
print("V7  核 A・B の時計差から力を組む")
m_, g_, d_, hh, c_ = sp.symbols('m g d h c', positive=True)
nu_C_s = m_ * c_**2 / hh
F_C  = hh * (nu_C_s * g_ * d_ / c_**2) / d_
F_ZB = hh * (sp.Symbol('beta') * nu_C_s * g_ * d_ / c_**2) / d_
print(f"    Compton 時計で: F = {sp.simplify(F_C)}   ZB 時計で: F = {sp.simplify(F_ZB)}")
check("Compton 時計なら F = mg、核間隔 d は相殺（0SM 固有の量を使っていない）", sp.simplify(F_C - m_ * g_) == 0)
check("ZB 時計で数えると βmg（重さが 1/25）→ 力を担うのは Compton 側の刻み", sp.simplify(F_ZB - sp.Symbol('beta') * m_ * g_) == 0)

# ---- V8 すべり時間と Unruh の熱時間 ----
print("V8  二点の時計が 1 サイクルずれるまでの時間 τ = h/(m g Δx)")
tau_KMS = hbar / (kB * hbar * g0 / (2 * math.pi * c * kB))
T_U = hbar * g0 / (2 * math.pi * c * kB)
tau_bar = h / (me * g0 * lamCb)
tau_d   = h / (me * g0 * d)
print(f"    T_U(g) = {T_U:.3e} K、熱時間 ħ/(k_B T_U) = 2πc/g = {tau_KMS:.4e} s")
print(f"    Δx = λ̄_C: τ = {tau_bar:.4e} s（質量に依らない）")
print(f"    Δx = λ_C/2: τ = 2c/g = {tau_d:.4e} s = {tau_d/3.156e7:.2f} 年（Compton 時計）"
      f"、ZB 時計なら {tau_d/beta/3.156e7:.1f} 年")
check("Unruh の熱時間 = 換算 Compton 波長だけ離れた二時計の 1 サイクルすべり時間（次元の恒等式）",
      rel(tau_bar, tau_KMS) < 1e-12)
check("核間隔 λ_C/2 では τ = 2c/g（質量に依らない）", rel(tau_d, 2 * c / g0) < 1e-12)
for name, gg in (("中性子星表面", 1e12), ("Schwinger 加速度 c²/λ̄_C", c**2 / lamCb)):
    print(f"    {name}: g = {gg:.2e} m/s², すべり時間 2c/g = {2*c/gg:.2e} s")

# ---- V9 エントロピー最大 + 降下で手放すエネルギー → Tolman–Ehrenfest ----
print("V9  二つの高さの熱浴。保存するのは局所エネルギーではなく E∞ = E_loc √A（指針 2 の帳簿）")
E1, T1, T2, A1, A2 = sp.symbols('E1 T1 T2 A1 A2', positive=True)
# dS = dE1/T1 + dE2/T2、拘束 dE1 √A1 + dE2 √A2 = 0
dE2 = -sp.sqrt(A1) / sp.sqrt(A2)
dS = 1 / T1 + dE2 / T2
sol = sp.solve(sp.Eq(dS, 0), T2)[0]
print(f"    dS = 0 → T2 = {sol}")
check("T √A = 一定（Tolman–Ehrenfest：下ほど熱い）", sp.simplify(sol * sp.sqrt(A2) - T1 * sp.sqrt(A1)) == 0)
dS_local = 1 / T1 - 1 / T2
check("局所エネルギーが保存するなら一様温度になる（重力が熱力学に入らない）",
      sp.solve(sp.Eq(dS_local, 0), T2)[0] == T1)
print(f"    1 m の高低差で T_下/T_上 − 1 = {dphi_1m:.3e}")

# ---- V10 Geroch–Bekenstein: 地平面まで降ろして落とす ----
print("V10 地平面近傍: √A ≈ κℓ/c²。中心が地平面から R のところで放す → 残りのエネルギー mκR")
for name, R in (("R = λ̄_C", lamCb), ("R = λ_C/2（0SM の光子球）", lamC / 2)):
    dS_kB = 2 * math.pi * R / lamCb
    dA = 4 * dS_kB      # ℓ_P² 単位
    print(f"    {name}: ΔS_BH = {dS_kB:.4f} k_B = {dS_kB/math.log(2):.2f} bit、ΔA_min = {dA:.2f} ℓ_P²")
check("R = λ̄_C で ΔS = 2π k_B（Bekenstein 1973 の ΔA_min = 8π ℓ_P²）", rel(2 * math.pi * lamCb / lamCb, 2 * math.pi) < 1e-12)
check("R = λ_C/2 で ΔS = 2π² k_B（質量に依らない）", rel(2 * math.pi * (lamC / 2) / lamCb, 2 * math.pi**2) < 1e-12)
S_bound = 2 * math.pi * (me * c**2) * (lamC / 2) / (hbar * c)
check("Bekenstein 上限 2πER/ħc（E = mc²、R = λ_C/2）も 2π² で一致", rel(S_bound, 2 * math.pi**2) < 1e-12)

# ---- V11 光子球に光子気体を詰めた場合のエントロピー（上限との照合） ----
print("V11 半径 λ_C/2 の球に光子気体")
R = lamC / 2
V = 4 / 3 * math.pi * R**3
a_rad = math.pi**2 * kB**4 / (15 * hbar**3 * c**3)
T_half = me * c**2 / (2 * kB)
U_half = a_rad * T_half**4 * V
S_half = 4 / 3 * U_half / T_half / kB
T_fit = (me * c**2 / (a_rad * V))**0.25
S_fit = 4 / 3 * (me * c**2) / T_fit / kB
print(f"    kT = mc²/2 と置くと U = {U_half/(me*c**2):.2f} mc²、S = {S_half:.2f} k_B（T5.12 の数え方）")
print(f"    U = mc² に合わせると kT = {kB*T_fit/(me*c**2):.3f} mc²、S = {S_fit:.2f} k_B")
check("U = mc² の光子気体は Bekenstein 上限 2π² k_B の内側", S_fit < 2 * math.pi**2)
check("kT = mc²/2 を統計の温度と読むと U が mc² の 5 倍を超える（T2.0「温度は占有層」を支持）", U_half > 5 * me * c**2)

# ---- V12 二核の剛体限界と Schwinger 加速度 ----
print("V12 固有長 L の剛体（Born）を加速するとき、中心の固有加速度の上限は 2c²/L")
a_max = 2 * c**2 / (lamC / 2)
a_S = c**2 / lamCb
print(f"    L = λ_C/2: a_max = {a_max:.3e} m/s²、Schwinger c²/λ̄_C = {a_S:.3e}、比 = {a_max/a_S:.3f}（= 2/π）")
check("剛体限界と Schwinger 加速度は同じ桁（比 2/π）", rel(a_max / a_S, 2 / math.pi) < 1e-12)

# ---- V13 自由落下する二核の往復: 曲率は「往復の刻み」と「核の刻み」の二次の食い違いとして残る ----
print("V13 Fermi 座標（中心が自由落下）: 軸 n̂ 上で g00 = −(1 + E_nn s²)、g_ss = 1（c = 1）")
E, s_, dd, vv = sp.symbols('E s d v', real=True)
dt_ds = 1 / (vv * sp.sqrt(1 + E * s_**2))                     # 局所速さ v の信号の座標時間
T_round = 2 * sp.integrate(sp.series(dt_ds, E, 0, 2).removeO(), (s_, -dd / 2, dd / 2))
tau_K = sp.expand(sp.series(T_round * sp.sqrt(1 + E * (dd / 2)**2), E, 0, 2).removeO())
mismatch = sp.simplify(tau_K / (2 * dd / vv) - 1)
print(f"    核の時計で測った往復 / (2d/v) − 1 = {mismatch}")
aa = sp.Symbol('a', real=True)
rate_fermi = lambda x: sp.sqrt(1 + E * x**2)          # 自由落下（Fermi）: g00 に一次の項が無い
rate_rindler = lambda x: 1 + aa * x                  # 静止して支えられた（固有加速度 a）
beat_free = sp.simplify(rate_fermi(dd / 2) - rate_fermi(-dd / 2))
beat_held = sp.simplify(rate_rindler(dd / 2) - rate_rindler(-dd / 2))
print(f"    核 A・B の刻みの差: 自由落下 {beat_free}、支えられた {beat_held}")
check("自由落下では二核の刻みが一致し（一次のうなり零 ＝ 等価原理）、支えられると a·d だけずれる",
      beat_free == 0 and sp.simplify(beat_held - aa * dd) == 0)
check("二次の食い違い δ = E_nn d²/12（向き n̂ に依る）", sp.simplify(mismatch - E * dd**2 / 12) == 0)

print("    δ(n̂) ∝ n̂ᵀ E n̂ を向きの球面で球面調和に分ける（E は乱数の対称行列、数値求積）")
import numpy as np
th, ph = sp.symbols('theta phi', real=True)
rng = np.random.default_rng(20261020)
Mx = rng.normal(size=(3, 3))
Enum = (Mx + Mx.T) / 2
xg, wg = np.polynomial.legendre.leggauss(40)          # cos θ の Gauss–Legendre
TH = np.arccos(xg)[:, None]
PH = (np.arange(80) + 0.5) * 2 * np.pi / 80
PH = PH[None, :]
W = wg[:, None] * (2 * np.pi / 80)
nvec = np.stack([np.sin(TH) * np.cos(PH), np.sin(TH) * np.sin(PH), np.cos(TH) * np.ones_like(PH)])
fnum = np.einsum('i...,ij,j...->...', nvec, Enum, nvec)
power = {}
for l in range(0, 5):
    tot = 0.0
    for m in range(-l, l + 1):
        Yf = sp.lambdify((th, ph), sp.Ynm(l, m, th, ph).expand(func=True), 'numpy')
        Yv = np.asarray(Yf(TH, PH), dtype=complex) * np.ones_like(fnum)
        cl = np.sum(fnum * np.conj(Yv) * W)
        tot += abs(cl)**2
    power[l] = tot
    print(f"    ℓ = {l}: Σ|c_ℓm|² = {tot:.3e}")
check("奇数の ℓ（1, 3）と ℓ = 4 は零 ── 二次の食い違いは ℓ = 0 と ℓ = 2 だけ",
      all(power[l] < 1e-24 for l in (1, 3, 4)) and power[2] > 1e-3)
avg = np.sum(fnum * W) / (4 * np.pi)
check("向きの平均（ℓ = 0）は E_ii/3 ＝ R₀₀/3（Ricci の時間成分）", abs(avg - np.trace(Enum) / 3) < 1e-12)

# ---- V14 大きさ（構造の確認であって測れる量ではない） ----
print("V14 δ の大きさ（d = λ_C/2）")
E_earth = 2 * GM_E / R_E**3
print(f"    地表の潮汐（真空、ℓ = 2 のみ）: |E| ≈ {E_earth:.3e} s⁻²、δ ≈ {E_earth*d**2/(12*c**2):.2e}")
for name, rho in (("水", 1e3), ("中性子星の中心", 5e17)):
    avg = 4 * math.pi * G * rho * d**2 / (36 * c**2)
    print(f"    {name}（ρ = {rho:.0e} kg/m³）の中の ℓ = 0: ⟨δ⟩ = 4πGρ d²/(36c²) = {avg:.2e}")
rho_one = 36 * c**2 / (4 * math.pi * G * d**2)
print(f"    ⟨δ⟩ = 1 になる密度: {rho_one:.2e} kg/m³（核密度 ~2e17 の 10³³ 倍）")
check("地上の物質中では 1e-45 未満（測れない。言えるのは構造だけ）", 4 * math.pi * G * 1e3 * d**2 / (36 * c**2) < 1e-45)

print(f"\n全 {ok_count} 項目 OK")
