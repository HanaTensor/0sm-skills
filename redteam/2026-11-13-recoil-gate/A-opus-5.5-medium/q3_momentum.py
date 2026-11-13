"""Q3: 自明でない検査 ── 運動量の明示的な割り当て。

D 一定の解（Q2）の上で、運動量を三つに分ける（c² を掛けた量、ω 単位）:
  P_pair  = (E_A+E_B) v_m             核対（相対論的にも p = E v / c² は厳密）
  P_gam   = K v_γ                     光子球を「E/c² の塊」とみなす割り当て
  P_tr    = Σ Ė_i (x_i - x_c)          エネルギーが離れた点へ移ること自体の運動量
            （A→γ、γ→B の流れとして書くと  a (x_γ-x_A) + b (x_B-x_γ)）
c² dD/dt = P_pair + P_gam + P_tr は積の微分の恒等式。自明でないのは
 (1) P_tr を落とすと和が 0 にならないか
 (2) 各部分に ω の成分が残るか
 (3) P_tr を光速以下の流れで運ぶには、予算の外に「移送中のエネルギー」がどれだけ要るか
 (4) 光子球の運動量を K/c（光としての運動量）にすると矛盾するか
"""
import sympy as sp
import numpy as np
from common import *

xm = C + d / 2 * sp.cos(th) * (1 + sp.sin(th) ** 2 / 2)   # Q2 の解
xA, xB = xm - d / 2, xm + d / 2
xg = xm - d / 2 * sp.cos(th)
xc = C

D = lambda f: sp.diff(f, th)
P_pair = (EA + EB) * D(xm)
P_gam = K * D(xg)
P_kin = P_pair + P_gam
a_flow = -D(EA)          # A から光子球へ流れ出す率（θ∈(0,π) で正）
b_flow = D(EB)           # 光子球から B へ流れ込む率
print("流れの保存 a - b - dK/dθ =", sp.simplify(a_flow - b_flow - D(K)))
P_tr = a_flow * (xg - xA) + b_flow * (xB - xg)
P_tr2 = D(EA) * (xA - xc) + D(EB) * (xB - xc) + D(K) * (xg - xc)
print("P_tr の二つの書き方の差 =", sp.simplify(P_tr - P_tr2))
print("P_pair + P_gam + P_tr =", sp.simplify(P_kin + P_tr), "（恒等的に 0 ＝ D 一定と同値）")

tt = np.linspace(0, 2 * np.pi, 200001)
print("\n各部分の振動数成分（c²P/(ω E0 d)）:")
for name, ex in [("P_pair", P_pair), ("P_gam", P_gam), ("P_kin=P_pair+P_gam", P_kin), ("P_tr", P_tr)]:
    a, b = fourier_cos_sin(to_num(ex / (E0 * d)))
    show_series(name, a, b)
    fn = to_num(ex / (E0 * d))
    print(f"     max|·| = {np.max(np.abs(fn(tt))):.6f}")

# 力（核対に働く力 F = dP_pair/dt, ω² 単位）
F_pair = D(P_pair)
a, b = fourier_cos_sin(to_num(F_pair / (E0 * d)))
print("\n核対に働く力:")
show_series("c²F_pair/(ω² E0 d)", a, b)
F_gam = D(P_gam)
a, b = fourier_cos_sin(to_num(F_gam / (E0 * d)))
show_series("c²dP_gam/dt/(ω² E0 d)", a, b)

# (1) P_tr を落とした場合: P_kin = 0 を課して x_m を決め直すと D は一定か
print("\n(1') P_tr を無視し P_pair+P_gam=0 を課した場合の x_m:")
xm2 = sp.Function('y')(th)
xg2 = xm2 - d / 2 * sp.cos(th)
eq = (EA + EB) * D(xm2) + K * D(xg2)
# (E_A+E_B+K) y' = K (d/2)(-sinθ) ... を解く:  y' = -K (d/2) sinθ / E0
yprime = sp.simplify(sp.solve(sp.Eq(eq, 0), D(xm2))[0])
print("  y'(θ) =", yprime)
y = sp.integrate(yprime, th)
print("  y(θ) =", sp.simplify(y))
Dbad = sp.simplify((EA * (y - d / 2) + EB * (y + d / 2) + K * (y - d / 2 * sp.cos(th))))
a, b = fourier_cos_sin(to_num(Dbad / (E0 * d)))
show_series("  その時の c²D/(E0 d)", a, b)
print("  → 運動量を『塊の運動』だけに割り当てると D は ω・3ω で振れる（dD/dt=P が破れる）")

# (3) 移送中に必要な最小エネルギー: 流れ a が距離 L を速さ u ≤ c で進むと
#     移送中のエネルギー = a ω L / u ≥ a ω L / c。予算 E0 の外に要る量。
Etr = (sp.Abs(a_flow * (xg - xA)) + sp.Abs(b_flow * (xB - xg)))   # × ω/c で E
fEtr = to_num(Etr / (E0 * d))
m = np.max(fEtr(tt))
print(f"\n(3) 移送中に最低限必要なエネルギー E_tr,min = (ω/c)[a|x_γ-x_A| + b|x_B-x_γ|]")
print(f"    max E_tr,min/(E0 · ωd/c) = {m:.6f}  (θ={tt[np.argmax(fEtr(tt))]:.4f})")
for dd, name in [(lamC / 2, "λC/2"), (lamC, "λC")]:
    print(f"    d={name}: max E_tr,min/E0 = {m*omega*dd/c_light:.4f}")
print("    （中点で結ぶ一様分布 Q4(i) と比べる場合は q4_placement.py）")

# (4) 光子球の運動量を光として K/c（向きは v_γ の符号）にした場合
print("\n(4) 光子球の運動量を ±K/c とした場合（基準案の運動のまま）:")
fPg = to_num(P_gam / (E0 * d))     # 塊としての値 × ω d E0 / c²
fK = to_num(K / E0)
for dd, name in [(lamC / 2, "λC/2"), (lamC, "λC")]:
    eps = omega * dd / c_light
    blob = np.max(np.abs(fPg(tt))) * eps          # E0/c 単位
    light = np.max(fK(tt))                         # E0/c 単位
    print(f"    d={name}: max|K v_γ/c²| = {blob:.4f} E0/c,  max K/c = {light:.4f} E0/c,  比 ≈ {light/blob:.1f}")
print("    → K/c を割り当てると、それを打ち消す反対向きの運動量がどこにも無い。")
print("      dD/dt = P を保つには、光子球の運動量は (K/c²)·v_γ（＝不変質量 K/c² の塊）でなければならない。")
