# -*- coding: utf-8 -*-
"""
幹 T4（T4.10）と幹 T7（T7.2）2026-10-06 版の再現スクリプト。
出典: trunks/SESSION-2026-10-06-karman-landau.md §2・§3（検算 [2]–[5]）を、幹に書く形で検算し直したもの。
numpy だけで動く。scipy・sympy があれば使う（無ければその項目は数値で代える）。

記法（必ず書き分ける）:
  θ₁ ＝ #1 の θ（全角、θ₁ = ωt。核は θ₁/2 に乗る）
  θ  ＝ 幹の θ ＝ θ₁/2（E₀ = cos⁴θ + sin⁴θ + ½ sin²2θ）
  D = cos θ₁ = cos 2θ、F/E₀ = sin θ₁ = sin 2θ
"""
import numpy as np

try:
    from scipy.integrate import quad
except Exception:
    quad = None
try:
    import sympy as sp
except Exception:
    sp = None

OK = lambda b: "OK" if b else "NG"
ALL = []
def check(label, val, tol):
    ALL.append(abs(val) < tol)
    print(f"  {label:<52}: {float(abs(val)):.1e}  {OK(abs(val) < tol)}")

def simpson(f, a, b, n=200000):
    x = np.linspace(a, b, n + 1); y = f(x); h = (b - a) / n
    return h / 3 * (y[0] + y[-1] + 4 * y[1:-1:2].sum() + 2 * y[2:-1:2].sum())

print("=" * 72)
print("[A] 開始時刻の補題  y(T) = ∫₀ᵀ e^{σ(T−t)} sin(Ωt+χ) dt")
def y_exact(s, W, T, c):
    return np.exp(s*T) * ((s*np.sin(c) + W*np.cos(c))
            - np.exp(-s*T) * (s*np.sin(W*T + c) + W*np.cos(W*T + c))) / (s**2 + W**2)
if sp is not None:
    s_, W_, T_, t_, c_ = sp.symbols('sigma Omega T t chi', positive=True)
    ysym = sp.integrate(sp.exp(s_*(T_ - t_)) * sp.sin(W_*t_ + c_), (t_, 0, T_))
    f = sp.lambdify((s_, W_, T_, c_), ysym, 'numpy')
    d = max(abs(f(1.3, 37.0, 2.1, c) - y_exact(1.3, 37.0, 2.1, c)) for c in np.linspace(0, 6.2, 13))
    check("sympy の積分と閉じた式（記号→数値）", d, 1e-9)
s, W, T = 1.0, 200.0, 6.0
worst = 0.0
for c in np.linspace(0, 2*np.pi, 25):
    g = lambda t: np.exp(s*(T - t)) * np.sin(W*t + c)
    num = quad(g, 0, T, limit=2000)[0] if quad else simpson(g, 0, T)
    worst = max(worst, abs(num - y_exact(s, W, T, c)) / np.exp(s*T) * W)
check("数値積分と閉じた式（e^{σT}/Ω で規格化）", worst, 1e-8)
# 静的な種（Ω→0 で sin χ = 1 の一定力）に対する重み
static = (np.exp(s*T) - 1) / s
for c, want in [(0.0, s/W), (np.pi, -s/W)]:
    check(f"χ = {c:.3f} で y/静的 → ±σ/Ω（相対）", y_exact(s, W, T, c)/static/want - 1, 1e-3)
# 赤道（χ = π/2）: 種は零ではなく σ²/(σ²+Ω²) ≈ (σ/Ω)² ── 二次で消える
T2 = 30.0                                        # 過渡項 e^{−σT} を落とすため長く取る
r = y_exact(s, W, T2, np.pi/2) / ((np.exp(s*T2) - 1) / s)
want = s**2 / (s**2 + W**2)
check("χ = π/2 で y/静的 = σ²/(σ²+Ω²)（相対、e^{−σT} 項を除く）", r/want - 1, 1e-2)
print(f"    χ = π/2: y/静的 = {r:.3e}、(σ/Ω)² = {(s/W)**2:.3e}、σ/Ω = {s/W:.3e}")
print("  → 選ばれる符号は cos χ。赤道の残差は (σ/Ω)² で一次の種より Ω/σ 倍小さい。")

print()
print("[B] #1 の式（θ₁ 全角）と幹の θ（= θ₁/2）")
th1 = np.linspace(0, 4*np.pi, 4001)
Te1, Te2 = np.cos(th1/2)**4, np.sin(th1/2)**4
check("D = T_e1 − T_e2 = cos θ₁", np.max(np.abs(Te1 - Te2 - np.cos(th1))), 1e-12)
dTe1 = np.gradient(Te1, th1); dTe2 = np.gradient(Te2, th1)
check("d/dθ₁(T_e2 − T_e1) = sin θ₁（#1 e3_simple_harmonic_motion）", np.max(np.abs((dTe2 - dTe1 - np.sin(th1))[5:-5])), 1e-5)
th = th1 / 2
check("幹の記法: D = cos 2θ、F/E₀ = sin 2θ", np.max(np.abs(np.cos(2*th) - np.cos(th1)) + np.abs(np.sin(2*th) - np.sin(th1))), 1e-12)
# F の時間積分の直流成分: ∫₀ᵗ sin(ω t' + χ) dt' = [cos χ − cos(ωt+χ)]/ω
om = 3.0; tt = np.linspace(0, 2*np.pi/om*40, 400001)   # 整数周期で平均する
for c in [0.4, 2.0]:
    integ = np.concatenate([[0], np.cumsum((np.sin(om*tt[1:]+c) + np.sin(om*tt[:-1]+c))/2 * np.diff(tt))])
    check(f"∫F dt の直流成分 = cos χ/ω（χ = {c}）", integ.mean() - np.cos(c)/om, 1e-3)

print()
print("[C] 札の付け替え（A↔B）と位相平均")
chi = np.linspace(0, 2*np.pi, 100001)[:-1]
D0 = np.cos(chi); n = 1.0
check("付け替え: (−D)(−n̂) = D n̂", np.max(np.abs((-D0)*(-n) - D0*n)), 1e-15)
check("⟨D(t₀)⟩_φ = 0（φ 平均で種は消える）", D0.mean(), 1e-12)
check("⟨F⟩_φ = 0", np.sin(chi).mean(), 1e-12)
check("⟨F²⟩_φ = ½（二乗平均は非零）", (np.sin(chi)**2).mean() - 0.5, 1e-12)
check("P(+) = ⟨Θ(cos χ)⟩_φ = ½（対称配置で 50/50）", (np.cos(chi) > 0).mean() - 0.5, 1e-4)

print()
print("[D] T4.4–T4.6 の X は D = cos θ₁ の関数（θ₁ は #1 の全角）── ジューコフスキー二段分解")
D = np.cos(th1)
X = 0.25*(np.sin(th1)**2 + 2)*np.cos(th1)
check("X(θ₁) = ¼(3 − D²)D", np.max(np.abs(X - 0.25*(3 - D**2)*D)), 1e-12)
u = 1 - D
check("X − ½ = −(3/4)(1−D)² + ¼(1−D)³（厳密）", np.max(np.abs(X - 0.5 - (-0.75*u**2 + 0.25*u**3))), 1e-12)
for e in [1e-2, 3e-3]:
    Xe = 0.25*(np.sin(e)**2 + 2)*np.cos(e)
    check(f"θ₁ = {e}: (X − ½)/θ₁⁴ → −3/16", (Xe - 0.5)/e**4 + 3/16, 1e-3)
    the = e/2
    Xe2 = 0.25*(np.sin(2*the)**2 + 2)*np.cos(2*the)
    check(f"幹の θ = {the}: (X − ½)/θ⁴ → −3（= −(3/16)·2⁴）", (Xe2 - 0.5)/the**4 + 3, 1e-3)

print()
print("[E] 数値（CODATA 2022）")
me, c0, hbar = 9.1093837139e-31, 299792458.0, 1.054571817e-34
lamC = 2.42631023538e-12
w = me*c0**2/hbar; Om = 2*w
F0 = me*c0**2/(lamC/2)
muB = 9.2740100657e-24
print(f"  ω = mc²/ħ = {w:.4e} rad/s、Ω = 2ω（ZB 角周波数）= {Om:.4e} rad/s")
print(f"  λ_C/2 = {lamC/2:.4e} m（光子球の変位の上限）")
print(f"  F₀ = mc²/(λ_C/2) = {F0:.4e} N、SG 力 μ_B×10³ T/m = {muB*1e3:.4e} N、比 {F0/(muB*1e3):.2e}")
for sg in [1e1, 1e5, 1e9]:
    print(f"  σ = {sg:.0e} s⁻¹: 実効の種 F₀σ/Ω = {F0*sg/Om:.3e} N、赤道残差 F₀(σ/Ω)² = {F0*(sg/Om)**2:.3e} N")
print("  （Ω を mc²/ħ に取っても σ/Ω が 2 倍になるだけで、桁の結論は変わらない）")

print()
print("[F] 一粒の Malus 検定 ── 準備後の軸 n̂ の分布の三候補（読み出しは sign(a·n̂)）")
# 準備方向 p = ẑ、検出器 a は z から角 a 傾ける。P(+|a) を球面上で直接積分（決定論的な求積）
Nt, Nf = 1500, 1500
tg = (np.arange(Nt) + 0.5) * (np.pi/2) / Nt          # p 側の半球のみ（θ_n ∈ [0, π/2]）
fg = (np.arange(Nf) + 0.5) * 2*np.pi / Nf
TG, FG = np.meshgrid(tg, fg, indexing='ij')
dA = np.sin(TG) * (np.pi/2/Nt) * (2*np.pi/Nf)
nx, nz = np.sin(TG)*np.cos(FG), np.cos(TG)
rows = []
for ad in [0, 30, 45, 60, 90, 120, 150, 180]:
    a = np.radians(ad)
    up = (np.sin(a)*nx + np.cos(a)*nz) > 0
    w_cos = nz * dA; w_uni = dA
    P_cos = (up*w_cos).sum()/w_cos.sum()
    P_uni = (up*w_uni).sum()/w_uni.sum()
    P_align = 1.0 if ad < 90 else (0.5 if ad == 90 else 0.0)
    P_circ = 1 - a/np.pi                                   # 円周一様の位相 φ だけ
    rows.append((ad, P_align, P_uni, P_cos, P_circ, np.cos(a/2)**2))
print("   a(度)  (i)揃う   (ii)半球一様  (iii)半球余弦=KS  円周位相   cos²(a/2)")
for r in rows:
    print(f"   {r[0]:5d}   {r[1]:.4f}    {r[2]:.4f}       {r[3]:.4f}          {r[4]:.4f}    {r[5]:.4f}")
check("(iii) 余弦重み（KS 1967）と cos²(a/2) の最大差", max(abs(r[3]-r[5]) for r in rows), 2e-3)
check("(ii) 半球一様 = 1 − a/π（線形）の最大差", max(abs(r[2]-r[4]) for r in rows), 2e-3)
dev = max(abs(r[2]-r[5]) for r in rows)
ALL.append(dev > 0.05); print(f"  (ii) 半球一様は余弦と食い違う（最大差 {dev:.3f}）  {OK(dev > 0.05)}")
if sp is not None:
    # (iii) の閉じた形: P(+|a) = (1 + cos a)/2 を、p·n̂ = cos θ_n の密度で記号的に確かめる（a = 0 と π/2 の区間端で）
    th_, = sp.symbols('theta', positive=True),
    norm = sp.integrate(sp.cos(th_)*sp.sin(th_), (th_, 0, sp.pi/2)) * 2*sp.pi
    print(f"  余弦密度の規格化 ∫(p·n̂)dΩ over 半球 = {sp.simplify(norm)}（= π）")
print("  → 位相 φ だけでも、軸が揃っても、半球に一様でも Malus は出ない。")
print("    p 側の半球に (p·n̂) の重みで分布するときだけ cos²(a/2)（KS 1967）。T7 の K5。")

print("=" * 72)
print("全項目:", "OK" if all(ALL) else "NG", f"({sum(ALL)}/{len(ALL)})")
