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
