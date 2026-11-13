"""Q1・Q2: 質量双極子 D と核対の反跳 x_m(θ)。"""
import sympy as sp
import numpy as np
from common import *

xm = sp.Function('x_m')(th)
xA, xB = xm - d / 2, xm + d / 2
xg = xm - d / 2 * sp.cos(th)

# --- 恒等式の確認 ---
print("T_A+T_B+K-E0 =", sp.simplify(EA + EB + K - E0))

Dc2 = EA * xA + EB * xB + K * xg              # = c² D
Dc2_s = sp.simplify(sp.expand_trig(Dc2.rewrite(sp.cos)))
print("c²D =", sp.factor(sp.simplify(Dc2)))

# ===== Q1: x_m = 0 固定 =====
print("\n=== Q1: 核を固定（x_m=0） ===")
D1 = sp.simplify(Dc2.subs(xm, 0))
print("c²D(θ) =", sp.simplify(D1), "  （期待: -(E0 d/2) cosθ (1 + ½ sin²θ)）")
chk = sp.simplify(D1 + E0 * d / 2 * sp.cos(th) * (1 + sp.sin(th) ** 2 / 2))
print("  照合:", chk)
a, b = fourier_cos_sin(to_num(D1 / (E0 * d)))
show_series("c²D/(E0 d)", a, b)
# 全運動量 P = dD/dt と、外から核を支える力 F = dP/dt
P1 = sp.diff(D1, th)          # × ω / c²
F1 = sp.diff(D1, th, 2)       # × ω² / c²
a, b = fourier_cos_sin(to_num(P1 / (E0 * d)))
show_series("c²P/(ω E0 d)", a, b)
a, b = fourier_cos_sin(to_num(F1 / (E0 * d)))
show_series("c²F_ext/(ω² E0 d)", a, b)
fP = sp.lambdify(th, (P1 / (E0 * d)).subs({d: 1, E0: 1}))
tt = np.linspace(0, 2 * np.pi, 200001)
print(f"  max|c²P/(ω E0 d)| = {np.max(np.abs(fP(tt))):.6f}  (θ={tt[np.argmax(np.abs(fP(tt)))]:.4f})")
for dd, name in [(lamC / 2, "λC/2"), (lamC, "λC")]:
    Pmax = np.max(np.abs(fP(tt))) * omega * E0_J * dd / c_light ** 2
    print(f"  d={name}: max|P| = {Pmax:.4e} kg m/s = {Pmax*c_light/E0_J:.4f} E0/c")

# ===== Q2: D 一定を課す =====
print("\n=== Q2: 核対の反跳を許す ===")
sol = sp.solve(sp.Eq(Dc2, E0 * C), xm)
xm_sol = sp.simplify(sol[0])
print("x_m(θ) =", xm_sol)
f = sp.simplify((xm_sol - C) / (d / 2))
print("  (x_m - C)/(d/2) = f(θ) =", sp.simplify(f))
print("  照合 f - cosθ(1+½sin²θ) =", sp.simplify(f - sp.cos(th) * (1 + sp.sin(th) ** 2 / 2)))
print("  f を cosθ=u の多項式で: f = (3u - u³)/2 →", sp.simplify(f.subs(sp.sin(th) ** 2, 1 - sp.cos(th) ** 2)))
a, b = fourier_cos_sin(to_num(f))
show_series("f", a, b)
fn = to_num(f)
print(f"  f の値域: [{fn(tt).min():.6f}, {fn(tt).max():.6f}]  → x_m の振幅 d/2・全幅 d")
# 一意性: D=E0 C の線形一階でない代数方程式（x_m について一次）→ 定数 C を除き一意
print("  x_m について一次方程式（係数 =", sp.simplify(sp.diff(Dc2, xm)), "）なので、C を除いて一意")

# 速度
v = sp.simplify(sp.diff(xm_sol, th))     # × ω
print("\n  dx_m/dθ =", sp.factor(sp.simplify(v)), " （期待 -(3/4) d sin³θ）")
print("  照合:", sp.simplify(v + sp.Rational(3, 4) * d * sp.sin(th) ** 3))
print(f"  νλC/c = {nu*lamC/c_light:.6f}   ωλC/c = {omega*lamC/c_light:.6f}")
for dd, name in [(lamC / 2, "λC/2"), (lamC, "λC")]:
    vmax = 0.75 * omega * dd
    print(f"  d={name}: v_max(核) = (3/4)ωd = {vmax:.4e} m/s = {vmax/c_light:.5f} c,"
          f" γ = {1/np.sqrt(1-(vmax/c_light)**2):.5f},  振幅 d/2 = {dd/2:.4e} m")
# 光子球の速度
xg_sol = sp.simplify(xg.subs(xm, xm_sol))
print("\n  x_γ - C =", sp.factor(sp.simplify(xg_sol - C)), " （d/4 · cosθ sin²θ）")
vg = to_num(sp.diff(xg_sol, th) / d)
vgmax = np.max(np.abs(vg(tt)))
print(f"  max|dx_γ/dθ|/d = {vgmax:.6f}")
for dd, name in [(lamC / 2, "λC/2"), (lamC, "λC")]:
    print(f"  d={name}: v_max(光子球) = {vgmax*omega*dd/c_light:.5f} c")
print("  θ=0 で A は", sp.simplify((xm_sol - d/2 - C).subs(th, 0)), "、θ=π で B は",
      sp.simplify((xm_sol + d/2 - C).subs(th, sp.pi)), "（重心 C からのずれ）")

a, b = fourier_cos_sin(to_num(Dc2.subs(xm, xm_sol) / (E0 * d)))
show_series("c²D/(E0 d) [Q2]", a, b)

# ===== 読み B: 核に静止エネルギー M c² が別にある場合 =====
print("\n=== 読み B: 核それぞれに T とは別の静止エネルギー Mc² がある ===")
M = sp.symbols('M', positive=True)   # Mc² を E0 単位で
DcB = Dc2 + M * E0 * (xA + xB)
xmB = sp.simplify(sp.solve(sp.Eq(DcB, (1 + 2 * M) * E0 * C), xm)[0])
print("  (x_m - C) =", sp.factor(sp.simplify(xmB - C)))
print("  → 形は同じ f(θ)、振幅だけ μ = E0/(E0+2Mc²) 倍")
for Mval, name in [(0, "M=0"), (1, "Mc²=E0 (電子程度)"), (1836.15, "Mc²=陽子/電子 比 ×E0")]:
    mu = 1 / (1 + 2 * Mval)
    print(f"  {name}: μ={mu:.5g}, d=λC での v_max = {0.75*omega*lamC*mu/c_light:.5g} c")
