#!/usr/bin/env python3
"""
SESSION-2026-10-31-visibility-bound-verification.py
===================================================
〔max探索｜2026-10-31｜Opus 5.5・Effort = Max〕

2026-10-31 の壁練「#38 の可視度 √2 − 1 と実測 ── 位相を制御しない放出で 0.414 を
上回る干渉はあるか」（trunks/SESSION-2026-10-31-visibility-bound.md）の検算をまとめた
再現スクリプト。sympy / mpmath を使う。各項目は値と OK / NG を印字する。

記号（幹 T1 の T1.1）: 占有層 c = 𝒯_A = cos²(θ/2), s = 𝒯_B = sin²(θ/2), c + s = 1。
差 D = c − s = cos θ。#38 の式 (4.1) は二つの光束の強度を核エネルギー I_A = c²,
I_B = s² に取る。可視度 V = 2√(I_A I_B)/(I_A + I_B) = (1 − D²)/(1 + D²)（T1.8）。
#38 は θ₃₈ = θ/2 と書く（cos⁴θ₃₈ = c²）。位相平均は θ ∈ [0, 2π) の一様平均。

項目
  U1  #38 の式の再現と ⟨V⟩ = √2 − 1（閉形式 ∫₀^π sin²u/(1 + cos²u) du = π(√2 − 1)）
  U2  #38 式 (4.1)・(4.3) を字義どおり（係数 2C）に読むと負の強度が出る ── 救済に使えない
  U3  数え方: 一個一打（#38 §6 の MC）√2 − 1 ／ 強度の和（#4 の積分）1/3 ／ 通過中に θ が回る 1/3
  U4  層と分布: p ∈ {1, 2} × {位相一様, 球面一様} の天井。最も甘いものでも π/4
  U5  分布に依らない上界: ⟨V⟩ ≤ 1 − ⟨D²⟩（p = 2）、≤ 1 − ⟨D²⟩/2（p = 1）
  U6  外部の分波比 T を掛けても天井は上がらない（⟨V⟩(T) は T = 1/2 で最大）
  U7  実測値と天井（値は SESSION 文書 §2 の表。一次資料で確認したもの）
  U8  混合の上界: 二核が経路に分かれる成分の重み η ≤ (1 − V_obs)/(1 − (√2 − 1))
  U9  位相を選んで実測に届くための窓と時刻精度
  U10 実験の時刻のぼけと内部周期（前提 (a) はすべての実験で成り立つ）
  U11 二核の間隔と経路の間隔（前提 (b) は空間の分割としては取れない）
  U12 #4 の六点表と #4 の積分の再現
  U13 標準の量子力学の基準（内部状態に盲目な分波器）と #38 の式の同値な言い換え

実行:  python3 -I SESSION-2026-10-31-visibility-bound-verification.py
"""
import math

import mpmath as mp
import sympy as sp

mp.mp.dps = 30
th = sp.symbols('theta', real=True)
D_ = sp.symbols('D', real=True)
C = (1 + sp.cos(th)) / 2      # = cos²(θ/2)
S = (1 - sp.cos(th)) / 2      # = sin²(θ/2)

OK = lambda b: "OK" if b else "NG"
ALL_OK = []


def check(label, cond):
    ALL_OK.append(bool(cond))
    print(f"    [{OK(cond)}] {label}")


def avg(expr):
    """θ ∈ [0, 2π) の一様平均（内部時間の平均）"""
    return sp.nsimplify(sp.integrate(sp.expand(expr), (th, 0, 2 * sp.pi)) / (2 * sp.pi))


def mavg(f):
    """数値の一様平均（区間を四分割して求積）"""
    return mp.quad(f, [0, mp.pi/2, mp.pi, 3*mp.pi/2, 2*mp.pi]) / (2*mp.pi)


R21 = mp.sqrt(2) - 1
cA = lambda t: (1 + mp.cos(t)) / 2
sB = lambda t: (1 - mp.cos(t)) / 2
Vp = lambda p: (lambda t: 2*(cA(t)*sB(t))**(mp.mpf(p)/2) / (cA(t)**p + sB(t)**p))   # 占有層で非整数冪（README §0.6）

print("=" * 78)
# ------------------------------------------------------------------------- U1
print("U1  #38 の可視度の式と位相平均")
V = 2*C*S / (C**2 + S**2)
check("V = 2√(I_A I_B)/(I_A + I_B) ＝ (1 − D²)/(1 + D²)（T1.8）",
      sp.simplify(V - (1 - sp.cos(th)**2) / (1 + sp.cos(th)**2)) == 0)
t38 = sp.symbols('theta38', real=True)
V38 = 2*sp.cos(t38)**2*sp.sin(t38)**2 / (sp.cos(t38)**4 + sp.sin(t38)**4)
check("#38 の式 (4.3) の右辺 2cos²θ₃₈sin²θ₃₈/(cos⁴θ₃₈ + sin⁴θ₃₈) と θ₃₈ = θ/2 で一致",
      sp.simplify(sp.expand_trig(V38.subs(t38, th/2) - V)) == 0
      or abs(float(V38.subs(t38, 0.37/2) - V.subs(th, 0.37))) < 1e-15)
u = sp.symbols('u', real=True)
I_closed = sp.integrate(sp.sin(u)**2 / (1 + sp.cos(u)**2), (u, 0, sp.pi))
print("    ∫₀^π sin²u/(1 + cos²u) du =", sp.nsimplify(sp.simplify(I_closed)))
check("∫₀^π sin²u/(1 + cos²u) du = π(√2 − 1)", sp.simplify(I_closed - sp.pi*(sp.sqrt(2) - 1)) == 0)
mV = mavg(Vp(2))
print(f"    ⟨V⟩ = {mp.nstr(mV, 20)}（√2 − 1 = {mp.nstr(R21, 20)}）")
check("⟨V⟩ = √2 − 1（30 桁の求積）", abs(mV - R21) < mp.mpf('1e-25'))
check("V(D = 0) = 1、V(D = ±1) = 0 ── 一粒ごとには 0 から 1 まで動く",
      V.subs(th, sp.pi/2) == 1 and V.subs(th, 0) == 0)

# ------------------------------------------------------------------------- U2
print("U2  式 (4.1)・(4.3) を字義どおり（交差項の係数 2𝒞、𝒞 = 2cs）に読む")
I_min_lit = sp.expand(C**2 + S**2 - 2*(2*C*S))          # φ = π の強度
print("    I_min =", sp.simplify(I_min_lit), "（cos φ = −1）")
frac_neg = mp.quad(lambda t: 1 if (1 - 6*cA(t)*sB(t)) < 0 else 0, mp.linspace(0, 2*mp.pi, 721)) / (2*mp.pi)
frac_neg_closed = (mp.pi - 2*mp.asin(mp.sqrt(mp.mpf(2)/3))) / mp.pi
print(f"    I_min < 0 となる位相の割合 = {mp.nstr(frac_neg_closed, 6)}（sin²θ > 2/3。求積 {mp.nstr(frac_neg, 4)}）")
Vlit = lambda t: 4*cA(t)*sB(t) / (cA(t)**2 + sB(t)**2)
print(f"    字義どおりの V の最大 = {mp.nstr(Vlit(mp.pi/2), 6)}、平均 = {mp.nstr(mavg(Vlit), 10)} = 2(√2 − 1)")
check("字義どおりの式は位相の 39.2% で負の強度、V の最大は 2 ── 物理的に許されない（T1 §4 の『係数の重複』）",
      abs(frac_neg_closed - mp.mpf('0.391827')) < 1e-5 and abs(Vlit(mp.pi/2) - 2) < 1e-25)

# ------------------------------------------------------------------------- U3
print("U3  アンサンブルの数え方（どれを採っても √2 − 1 を超えない）")
A_cross, A_ends = avg(2*C*S), avg(C**2 + S**2)
V_int = A_cross / A_ends
print(f"    一個一打（各電子が一つの点、#38 §6 の MC が各電子の確率密度を規格化）: ⟨V⟩ = √2 − 1 = {mp.nstr(R21, 8)}")
print(f"    強度の和（Σ I）: ⟨2cs⟩/⟨c² + s²⟩ = {A_cross}/{A_ends} = {V_int}")
print("    通過中に θ が回る（README §0.1、通過時間 ≫ 内部周期）: 一粒の像が時間平均され、同じく", V_int)
check("強度の和・通過中の回転はともに 1/3、一個一打は √2 − 1 ── 天井は √2 − 1",
      V_int == sp.Rational(1, 3) and R21 > mp.mpf(1)/3)

# ------------------------------------------------------------------------- U4
print("U4  層（p）と位相の分布を変えた天井")
mV1 = mavg(Vp(1))
sphere2 = sp.integrate((1 - D_**2)/(1 + D_**2), (D_, -1, 1)) / 2
sphere1 = sp.integrate(sp.sqrt(1 - D_**2), (D_, -1, 1)) / 2
print(f"    p = 2（エネルギー層、#38）位相一様 : {mp.nstr(mV, 8)} = √2 − 1")
print(f"    p = 1（占有層）        位相一様 : {mp.nstr(mV1, 8)} = 2/π")
print(f"    p = 2                 球面一様 : {sp.nsimplify(sphere2)} = {float(sphere2):.6f}（参考）")
print(f"    p = 1                 球面一様 : {sp.nsimplify(sphere1)} = {float(sphere1):.6f}（参考）")
print(f"    参考 p = 3, 4 位相一様: {mp.nstr(mavg(Vp(3)), 6)}, {mp.nstr(mavg(Vp(4)), 6)}（T1 §3 の V_p）")
check("2/π、π/2 − 1、π/4 の閉形式", abs(mV1 - 2/mp.pi) < 1e-25
      and sp.simplify(sphere2 - (sp.pi/2 - 1)) == 0 and sp.simplify(sphere1 - sp.pi/4) == 0)
print("    README §0.1（θ が回り TPE が 100% → 0% と移る）の下では D = cos θ は逆正弦分布 → 球面一様は取れない")
p1_int = mavg(lambda t: 2*mp.sqrt(cA(t)*sB(t))) / mavg(lambda t: cA(t) + sB(t))   # p = 1 の強度の和
CEIL01 = {"1/3（p=2 強度の和）": 1/3, "√2−1（p=2 一個一打、#38）": float(R21), "2/π（p=1）": 2/math.pi}
CEIL = dict(CEIL01, **{"π/2−1（参考）": math.pi/2 - 1, "π/4（参考、最も甘い）": math.pi/4})
check(f"§0.1 と両立する変種の天井は最大 2/π = 0.6366（p = 1 の強度の和も {mp.nstr(p1_int, 10)}）",
      max(CEIL01.values()) == 2/math.pi and abs(p1_int - 2/mp.pi) < 1e-25)
check("§0.1 を捨てた参考値まで含めても最大は π/4 = 0.7854（占有層 ＋ 球面一様）", max(CEIL.values()) == math.pi/4)

# ------------------------------------------------------------------------- U5
print("U5  分布に依らない上界（どんな位相分布でも）")
xs = [mp.mpf(k)/1000 for k in range(1001)]
ok2 = all((1 - x)/(1 + x) <= 1 - x + mp.mpf('1e-30') for x in xs)          # x = D²
ok1 = all(mp.sqrt(1 - x) <= 1 - x/2 + mp.mpf('1e-30') for x in xs)
check("(1 − x)/(1 + x) ≤ 1 − x、√(1 − x) ≤ 1 − x/2（x = D² ∈ [0, 1]）", ok2 and ok1)
print("    ⇒ p = 2: ⟨V⟩ ≤ 1 − ⟨D²⟩、p = 1: ⟨V⟩ ≤ 1 − ⟨D²⟩/2。位相一様では ⟨D²⟩ = 1/2 なので 1/2 と 3/4")
check("位相一様の ⟨D²⟩ = 1/2", avg(sp.cos(th)**2) == sp.Rational(1, 2))
for vobs in (0.62, 0.90, 0.92, 0.98):
    print(f"    V = {vobs:.2f} に要る ⟨D²⟩: p = 2 で ≤ {1 - vobs:.2f}、p = 1 で ≤ {2*(1 - vobs):.2f}（位相一様は 0.50）")

# ------------------------------------------------------------------------- U6
print("U6  外部の分波比 T と二核の分配を掛けた模型 I₁ = T·c², I₂ = (1 − T)·s²")


def V_T(T):
    T = mp.mpf(T)
    f = lambda t: 2*mp.sqrt(T*(1 - T))*cA(t)*sB(t) / (T*cA(t)**2 + (1 - T)*sB(t)**2)
    return mavg(f)


grid = [mp.mpf(k)/20 for k in range(1, 20)]
vals = [V_T(T) for T in grid]
best = grid[vals.index(max(vals))]
print("    ⟨V⟩(T):", ", ".join(f"{float(T):.2f}→{float(v):.4f}" for T, v in zip(grid[::3], vals[::3])))
check(f"最大は T = {float(best):.2f} で {mp.nstr(max(vals), 10)} = √2 − 1（外部の分波器では天井は上がらない）",
      best == mp.mpf(1)/2 and abs(max(vals) - R21) < 1e-20)
std = lambda T: 2*mp.sqrt(mp.mpf(T)*(1 - mp.mpf(T)))     # 標準の形 V(T)/V(1/2)（Ji ら 2003 の当てはめ 2η√(T₁(1 − T₁))）
shape = [(T, std(T), V_T(T)/R21) for T in ('0.05', '0.2', '0.35')]
print("    形 V(T)/V(1/2): " + "、".join(f"T = {T}: 標準 {float(a):.3f} ／ 積の模型 {float(b):.3f}" for T, a, b in shape))
check("積の模型は標準の √(T(1 − T)) よりはるかに平ら（T = 0.05 で 0.86 対 0.44）── 分波比依存の形でも区別できる",
      shape[0][2] > 0.85 and shape[0][1] < 0.44)

# ------------------------------------------------------------------------- U7
print("U7  実測（値と出典は SESSION 文書 §2。ここでは比較だけ）")
OBS = [
    # (ラベル, 可視度, 分野, 出典の略記, 標準誤差 or None) ── 2026-10-31 に一次資料（本文・図の説明）で確認
    ("Schütz ら 2015 遠方場バイプリズム", 0.67, "電子・真空", "Measurement 68, 201", None),
    ("Schütz ら 2014 バイプリズム 0.5 V", 0.513, "電子・真空", "Ultramicrosc. 141, 9", 0.041),
    ("Chang ら 2009 点投影 CNT ナノプリズム", 0.78, "電子・真空", "Nanotechnology 20, 115401", None),
    ("Ji ら 2003 GaAs MZI", 0.62, "電子・固体", "Nature 422, 415", None),
    ("Roulleau ら 2008 小型 MZI", 0.65, "電子・固体", "PRL 100, 126802", None),
    ("Neder ら 2007 MZI（75–90% の上端）", 0.90, "電子・固体", "Nature 448, 333", None),
    ("Kundu ら 2023 MZI", 0.91, "電子・固体", "Nat. Phys. 19, 515", None),
    ("Wei ら 2017 グラフェン MZI（抵抗補正後）", 0.98, "電子・固体", "Sci. Adv. 3, e1700600", None),
    ("Huber ら 2024 完全結晶 Si（最終）", 0.92, "中性子", "PRR 6, 043079", 0.04),
    ("Heacock ら 2018 焼鈍後", 0.90, "中性子", "RSI 89, 023502", None),
    ("Hasegawa ら 2003 ILL S18 経路の縞", 0.91, "中性子", "Nature 425, 45", None),
]
for lab, v, part, src, err in OBS:
    over = [k for k, c in CEIL.items() if v > c]
    sig = f"（√2−1 の {(v - float(R21))/err:.1f}σ 上）" if err else ""
    print(f"    {lab:<40s} {v:5.3f}  {part:<6s} {src:<24s} 超える天井 {len(over)}/{len(CEIL)}{sig}")
above = [o for o in OBS if o[1] > float(R21)]
check(f"√2 − 1 を超える実測 {len(above)} 件（真空の電子 {sum(o[2] == '電子・真空' for o in above)}・固体中の電子 "
      f"{sum(o[2] == '電子・固体' for o in above)}・中性子 {sum(o[2] == '中性子' for o in above)}）",
      len(above) == len(OBS) and {o[2] for o in above} == {"電子・真空", "電子・固体", "中性子"})
vac01 = [o[0] for o in OBS if o[2] == "電子・真空" and o[1] > max(CEIL01.values())]
check(f"#4・#38 自身の場（真空の電子）で §0.1 と両立する天井 2/π を超える: {len(vac01)} 件", len(vac01) >= 2)
pi4 = {o[2] for o in OBS if o[1] > math.pi/4}
check(f"参考値 π/4 まで超える分野: {sorted(pi4)}", pi4 == {"電子・固体", "中性子"})

# ------------------------------------------------------------------------- U8
print("U8  混合の上界: 経路に二核が分かれる成分の重み η（残りは V = 1 と最も甘く置く）")
for lab, v, part, src, err in OBS:
    if v > float(R21):
        print(f"    {lab:<40s} η ≤ {(1 - v)/(1 - float(R21)):.3f}")

# ------------------------------------------------------------------------- U9
print("U9  位相を選んで実測に届くには ── 赤道（D = 0）を中心とする窓の幅")
hbar, h_, c_, me = mp.mpf('1.054571817e-34'), mp.mpf('6.62607015e-34'), mp.mpf('299792458'), mp.mpf('9.1093837139e-31')
beta2 = mp.mpf('0.00163798087')                          # #10 の β²（index §2）
lamC = h_/(me*c_)
nu_ZB = mp.sqrt(beta2)*c_/lamC                            # 横チャネルの ν_ZB ＝ β c/λ_C
P38 = mp.pi*hbar/(me*c_**2)                               # #38: θ₃₈ = ωt/2, ω = m_ec²/ħ, V の周期 π/ω
P0S = 1/(2*nu_ZB)                                         # 現行: θ の角振動数 2πν_ZB, V の周期は半サイクル
print(f"    ν_ZB = β c/λ_C = {mp.nstr(nu_ZB, 4)} Hz（index §2 の 5.0×10¹⁸ Hz）")
print(f"    V の周期: #38 の書き方 πħ/m_ec² = {mp.nstr(P38, 3)} s ／ 現行の 1/(2ν_ZB) = {mp.nstr(P0S, 3)} s")


def window_mean(w):
    return mp.quad(Vp(2), [mp.pi/2 - w, mp.pi/2, mp.pi/2 + w]) / (2*w)


win = {}
for vobs in (0.62, 0.90, 0.92, 0.98):
    w = mp.findroot(lambda x: window_mean(x) - vobs, (mp.mpf('0.05'), mp.pi/2 - mp.mpf('0.01')), solver='anderson')
    f = 2*w/mp.pi
    win[vobs] = f
    print(f"    V = {vobs:.2f}: 窓 ±{mp.nstr(w*180/mp.pi, 4)}°、周期の {mp.nstr(f*100, 3)}% → 時刻を "
          f"{mp.nstr(f*P38, 2)} s（#38）／{mp.nstr(f*P0S, 2)} s（現行）以内に揃える必要")
check("0.62 でも周期の半分強、0.92 では 2 割強の窓 ── 10⁻²⁰ s 級の位相の選別が要る",
      0.5 < win[0.62] < 0.65 and 0.15 < win[0.92] < 0.3)

# ------------------------------------------------------------------------- U10
print("U10 実験の時刻のぼけ（入力は代表値）と内部周期 ── 前提 (a)（位相一様）の判定")
eV = mp.mpf('1.602176634e-19')
# 透過電子顕微鏡（電子線ホログラフィー・バイプリズム）: 200 keV, ΔE = 0.3 eV, 光路 1 m
Ek = 200e3*eV
gam = 1 + Ek/(me*c_**2)
v = c_*mp.sqrt(1 - 1/gam**2)
dt_tem = 1*(mp.mpf('0.3')*eV)/(gam**3*me*v**3)
# 中性子（完全結晶干渉計）: λ = 2 Å, Δλ/λ = 1%, 光路 0.1 m
mn = mp.mpf('1.67492750056e-27')
vn = h_/(mn*mp.mpf('2e-10'))
dt_n = (mp.mpf('0.1')/vn)*mp.mpf('0.01')
rows = [("連続源（量子ホール MZI の直流注入・原子炉・電界放出）", None),
        ("TEM 200 keV, ΔE = 0.3 eV, 光路 1 m の飛行時間のぼけ", dt_tem),
        ("中性子 λ = 2 Å, Δλ/λ = 1%, 光路 0.1 m の飛行時間のぼけ", dt_n),
        ("仮に放出時刻を 1 as（10⁻¹⁸ s）に揃えた場合", mp.mpf('1e-18'))]
for lab, dt in rows:
    if dt is None:
        print(f"    {lab}: 時刻の基準そのものが無い → 位相は定義により一様")
    else:
        print(f"    {lab}: Δt = {mp.nstr(dt, 2)} s = V の周期の {mp.nstr(dt/P38, 2)} 倍（#38）／{mp.nstr(dt/P0S, 2)} 倍（現行）")
supp = mp.exp(-2*mp.pi**2*(mp.mpf('1e-18')/P0S)**2)
print(f"    1 as のガウス型のぼけでも、位相分布の一様からのずれ（第一 Fourier 成分）は ×{mp.nstr(supp, 3)}")
check("どの実験でも時刻のぼけは内部周期の 10 倍以上 ── 前提 (a) は成り立ち、逃げ道 (a) は運動学で閉じる",
      min(dt_tem/P0S, dt_n/P0S, mp.mpf('1e-18')/P0S) >= 10)

# ------------------------------------------------------------------------- U11
print("U11 二核の間隔と、干渉計の二つの経路の間隔")
seps = {"λ_C = h/m_ec": lamC, "ƛ_C = ħ/m_ec（#38 式 (1.1)）": hbar/(me*c_), "λ_C/2（#51 の核間隔）": lamC/2}
paths = {"二重スリット・バイプリズム 1 μm": mp.mpf('1e-6'), "量子ホール MZI の腕 10 μm": mp.mpf('1e-5'),
         "中性子干渉計の腕 3 cm": mp.mpf('0.03')}
for k, d in seps.items():
    print(f"    {k:<28s} {mp.nstr(d, 4)} m → 比 " + "、".join(f"{p.split()[0]} {mp.nstr(L/d, 2)}" for p, L in paths.items()))
mp_ = mp.mpf('1.67262192595e-27')
lam_p0 = hbar*c_/(mp.mpf('335.94e6')*eV)                # #61 の m₀ᵖ の換算 Compton 長
print(f"    #61 の核子（m₀ᵖ = 335.94 MeV の ħ/m₀c = {mp.nstr(lam_p0*1e15, 3)} fm）と中性子干渉計の腕: 比 {mp.nstr(mp.mpf('0.03')/lam_p0, 2)}")
check("経路の間隔は二核の間隔の 10⁵ 倍以上 ── 二核が一つずつ別の経路を通る空間の絵は取れない",
      min(L/d for L in paths.values() for d in seps.values()) > 1e5)

# ------------------------------------------------------------------------- U12
print("U12 #4（2019）の六点表と #4 の積分")
pts = [mp.pi/4 - k*mp.pi/20 for k in range(6)]            # 0.785, 0.628, 0.471, 0.314, 0.157, 0
amp = [(mp.cos(t)**2, mp.sin(t)**2) for t in pts]          # #4 の A_spinor1, A_spinor2（振幅）
print("    θ₃₈:", ", ".join(f"{float(t):.3f}" for t in pts))
print("    振幅比:", ", ".join(f"{float(a):.3f}:{float(b):.3f}" for a, b in amp))
Vk = [2*a*b/(a**2 + b**2) for a, b in amp]
print("    一点ごとの V:", ", ".join(f"{float(x):.3f}" for x in Vk))
sumV = sum(2*a*b for a, b in amp) / sum(a**2 + b**2 for a, b in amp)
print(f"    六点の和の可視度（強度の和）= {mp.nstr(sumV, 6)}、一個一打 = {mp.nstr(sum(Vk)/6, 6)}")
check("#4 の表の 0.655:0.345 と 0.794:0.206 を再現",
      abs(amp[1][0] - mp.mpf('0.655')) < 5e-4 and abs(amp[2][0] - mp.mpf('0.794')) < 5e-4)
a_, b_ = sp.symbols('a b', real=True)
t4 = sp.symbols('t', real=True)
I4 = sp.expand(sp.integrate(sp.expand((sp.cos(t4)**2*a_ + sp.sin(t4)**2*b_)**2), (t4, 0, 2*sp.pi)) / (2*sp.pi))
print("    #4 式 (e3_J0_W_int) の位相平均: ⟨(cos²θ·a + sin²θ·b)²⟩ =", I4)
check("#4 の積分は強度の和 ── 等振幅の二波で V = (1/4)/(3/4) = 1/3",
      sp.simplify(I4 - (sp.Rational(3, 8)*(a_**2 + b_**2) + sp.Rational(1, 4)*a_*b_)) == 0)

# ------------------------------------------------------------------------- U13
print("U13 標準の量子力学の基準（分波器が内部状態に盲目なとき）")
T1_, T2_ = sp.symbols('T1 T2', positive=True)
V_MZ = 2*sp.sqrt(T1_*(1 - T1_)*T2_*(1 - T2_)) / (T1_*T2_ + (1 - T1_)*(1 - T2_))
check("MZI の理想可視度 2√(T₁R₁T₂R₂)/(T₁T₂ + R₁R₂) は T₁ = T₂ = 1/2 で 1（内部状態に依らない）",
      sp.simplify(V_MZ.subs({T1_: sp.Rational(1, 2), T2_: sp.Rational(1, 2)})) == 1)
x_ = sp.symbols('x', positive=True)
check("#38 の V(θ) ＝ 第一分波器の比を T₁ = c²/(c² + s²) に置き換え、T₂ = 1/2 とした MZI の可視度",
      sp.simplify(V_MZ.subs({T2_: sp.Rational(1, 2), T1_: x_}) - 2*sp.sqrt(x_*(1 - x_))) == 0
      and abs(float((2*sp.sqrt(x_*(1 - x_))).subs(x_, (C**2/(C**2 + S**2)).subs(th, 1.1)) - V.subs(th, 1.1))) < 1e-14)
print("    ⇒ #38 の主張は『内部位相が分波比を決める』と同値。実際の分波比は外部（QPC の透過率・結晶・バイプリズム）が決める")

print("=" * 78)
print(f"結果: {sum(ALL_OK)}/{len(ALL_OK)} OK")
