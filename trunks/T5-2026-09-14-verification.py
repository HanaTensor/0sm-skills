#!/usr/bin/env python3
"""幹 T5 検算スクリプト ── 恒等式 E0 = 1 の一次読解（ディラック因数分解）

再現する項目（幹 T5 §4）:
  1. 恒等式 cos^4 + sin^4 + (1/2) sin^2 2θ = 1（記号）
  2. 倍角分解 (3 + cos 4θ)/4, (1 − cos 4θ)/4（記号）
  3. 2×2 表現 β = σ_z, α_x = σ_x での ⟨β⟩ = cos 2θ, ⟨α_x⟩ = sin 2θ, 単位円（記号・数値）
  4. 純粋度分解 Tr ρ² = 1, 対角のみ = cos^4 + sin^4, 差 = 交差項（記号）
  5. 数値: β² = 0.00163798087 → θ0, sin²θ0, 混合の代価 (1/2) β² m c²
"""
import sympy as sp
import numpy as np

th = sp.symbols("theta", real=True)
c4 = sp.cos(th)**4 + sp.sin(th)**4
cross = sp.Rational(1, 2) * sp.sin(2 * th)**2

print("== 1. 恒等式 ==")
E0 = sp.simplify(c4 + cross)
print("E0 =", E0)
assert E0 == 1

print("== 2. 倍角分解 ==")
assert sp.simplify(c4 - (3 + sp.cos(4 * th)) / 4) == 0
assert sp.simplify(cross - (1 - sp.cos(4 * th)) / 4) == 0
print("cos^4+sin^4 = (3+cos4θ)/4,  (1/2)sin^2 2θ = (1−cos4θ)/4  ... OK")

print("== 3. 2×2 表現と単位円 ==")
beta = sp.Matrix([[1, 0], [0, -1]])      # 質量軸（β の固有基底）
alpha = sp.Matrix([[0, 1], [1, 0]])      # 速度軸（β と反交換）
assert (alpha * beta + beta * alpha) == sp.zeros(2, 2)
psi = sp.Matrix([sp.cos(th), sp.sin(th)])
eb = sp.simplify((psi.T * beta * psi)[0])
ea = sp.simplify((psi.T * alpha * psi)[0])
print("<β> =", eb, ",  <α_x> =", ea)
assert sp.simplify(eb - sp.cos(2 * th)) == 0
assert sp.simplify(ea - sp.sin(2 * th)) == 0
assert sp.simplify(eb**2 + ea**2) == 1
# 三項の一次表現
assert sp.simplify(c4 - (1 + eb**2) / 2) == 0
assert sp.simplify(cross - ea**2 / 2) == 0
print("fermion = (1+<β>²)/2,  boson = <α>²/2,  <β>²+<α>² = 1  ... OK")

print("== 4. 純粋度分解 ==")
rho = psi * psi.T
pur = sp.simplify((rho * rho).trace())
diag_only = sp.Matrix([[rho[0, 0], 0], [0, rho[1, 1]]])
pur_deph = sp.simplify((diag_only * diag_only).trace())
print("Tr ρ² =", pur, ",  対角のみ =", sp.simplify(pur_deph))
assert pur == 1
assert sp.simplify(pur_deph - c4) == 0
assert sp.simplify(pur - pur_deph - cross) == 0
print("交差項 = 正負成分のコヒーレンス  ... OK")

print("== 5. 数値 ==")
beta2 = 0.00163798087            # #10 正準値
mc2_keV = 510.99895              # 電子静止エネルギー [keV]
s2t = np.sqrt(beta2)             # sin 2θ0 = v_ZB/c
th0 = 0.5 * np.arcsin(s2t)
print(f"v_ZB/c = sin 2θ0 = {s2t:.6f}")
print(f"θ0 = {np.degrees(th0):.4f} deg")
print(f"sin²θ0 (負エネルギー成分の占有) = {np.sin(th0)**2:.4e}")
deficit_eV = mc2_keV * 1e3 * (1 - np.cos(2 * th0))
print(f"混合の代価 mc²(1−cos2θ0) = {deficit_eV:.2f} eV   (比較: (1/2)β²mc² = {0.5*beta2*mc2_keV*1e3:.2f} eV)")
assert abs(deficit_eV - 0.5 * beta2 * mc2_keV * 1e3) / deficit_eV < 1e-3
# 逆位相の確認（数値）
for t in np.linspace(0, np.pi, 7):
    f = np.cos(t)**4 + np.sin(t)**4
    b = 0.5 * np.sin(2 * t)**2
    assert abs(f + b - 1) < 1e-12
print("逆位相・和 = 1（数値走査）... OK")
print("\n全項目 OK")

# ---------------------------------------------------------------------------
# 2026-09-14b 追加分（K4・K10・K11）
# ---------------------------------------------------------------------------
print("\n== 6. 時間発展とブロッホ球（K4・K10）==")
t = sp.symbols("t", real=True)
w = sp.symbols("omega", positive=True)
th0 = sp.symbols("theta_0", real=True)
sig_y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
psi_t = sp.Matrix([sp.cos(th0) * sp.exp(-sp.I * w * t), sp.sin(th0) * sp.exp(sp.I * w * t)])
def ev(op):
    return sp.simplify((psi_t.H * op * psi_t)[0])
eb_t, ex_t, ey_t = ev(beta), ev(alpha), ev(sig_y)
print("<β>(t)   =", eb_t)
print("<α_x>(t) =", sp.simplify(ex_t.rewrite(sp.cos)))
print("<α_y>(t) =", sp.simplify(ey_t.rewrite(sp.cos)))
assert sp.simplify(eb_t - sp.cos(2 * th0)) == 0
assert sp.simplify(ex_t - sp.sin(2 * th0) * sp.cos(2 * w * t)) == 0
assert sp.simplify(ey_t - sp.sin(2 * th0) * sp.sin(2 * w * t)) == 0
# ラグランジュ（一粒・瞬間）: ブロッホ球条件
assert sp.simplify(eb_t**2 + ex_t**2 + ey_t**2 - 1) == 0
print("一粒・瞬間: <β>²+<α_x>²+<α_y>² = 1（ブロッホ球）... OK")
# オイラー（位相平均）: 一成分の平均が交差項
avg = sp.integrate(ex_t**2, (t, 0, 2 * sp.pi / (2 * w))) / (2 * sp.pi / (2 * w))
assert sp.simplify(avg - sp.Rational(1, 2) * sp.sin(2 * th0)**2) == 0
print("位相平均: mean(<α_x>²) = ½ sin²2θ0 = 交差項（½ は cos² の平均）... OK")

print("\n== 7. 受動的同期反転の二粒子相関（K11）==")
rng = np.random.default_rng(0)
N = 400000
phi = rng.uniform(0, 2 * np.pi, N)       # 共有位相、測定時刻に対して一様
def E(a, b):
    A = np.sign(np.cos(phi - a)); B = np.sign(-np.cos(phi - b))   # 一重項: 粒子2は −n
    return np.mean(A * B)
print(f"{'角度差':>8} {'同期反転':>10} {'線形':>8} {'量子 -cos':>10}")
for d in [0, np.pi / 8, np.pi / 4, 3 * np.pi / 8, np.pi / 2, 3 * np.pi / 4]:
    e = E(0.0, d)
    lin = -(1 - 2 * d / np.pi)
    print(f"{d:8.3f} {e:10.3f} {lin:8.3f} {-np.cos(d):10.3f}")
    assert abs(e - lin) < 5e-3
print("受動的同期反転 = 角度差に線形（Bell 1964 の反例と同一）。余弦にならない ... 記帳")
print("\n全項目 OK（09-14b）")
