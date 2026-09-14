#!/usr/bin/env python3
"""幹 T6（相互作用の描像）§4 の数値を再現するスクリプト。

python3 T6-2026-09-15-verification.py  → 各項目に OK / NG を表示する。
外部パッケージ不要（標準ライブラリのみ）。
"""
import math

# ---- 定数（CODATA 2018）----
c = 2.99792458e8
h = 6.62607015e-34
hbar = h / (2 * math.pi)
me = 9.1093837015e-31
e = 1.602176634e-19
eps0 = 8.8541878128e-12
G = 6.67430e-11
mc2_eV = 510998.95
alpha = 1 / 137.035999084
beta2 = 0.00163798087          # #10 正準値
beta = math.sqrt(beta2)        # 0.04047…
lamC = h / (me * c)
lambar = hbar / (me * c)

ok_all = True
def check(name, val, ref, rel=2e-2):
    global ok_all
    good = abs(val - ref) <= rel * abs(ref)
    ok_all &= good
    print(f"[{'OK' if good else 'NG'}] {name}: {val:.4g} (ref {ref:.4g})")

print("== T6.3 多重極パラメータ kr = 2π(λ_C/2)/λ ==")
def kr(nu):
    return 2 * math.pi * (lamC / 2) / (c / nu)
check("kr 可視光 5e14", kr(5e14), 1.27e-5)
check("kr 内部線 5e18", kr(5.0e18), 0.127)
check("(kr)^2 内部線", kr(5.0e18) ** 2, 1.62e-2)
check("kr Dirac ZB 3.93e20", kr(3.93e20), 9.99)
nu_kr1 = (mc2_eV * e / h) / math.pi
check("kr=1 の光子エネルギー keV", h * nu_kr1 / e / 1e3, 163)

print("== T6.4 角の硬さ δθ = E/(2βmc²) ==")
def dtheta(E_eV):
    return E_eV / (2 * beta * mc2_eV)
check("δθ 2 eV", dtheta(2), 4.84e-5)
check("δθ 1 keV", dtheta(1000), 0.0242)
check("δθ 20.68 keV", dtheta(beta * mc2_eV), 0.5, rel=1e-6)

print("== T6.6 / T6.7 内部アンジュレータと内部加速度 ==")
nu_int = beta * c / lamC
check("ν_ZB = βc/λ_C", nu_int, 5.00e18)
a_int = beta * c * 2 * math.pi * nu_int
check("a_int", a_int, 3.81e26)
g = 45e9 / mc2_eV; rho = 3096.0
check("LEP 静止系加速度", g * g * c ** 2 / rho, 2.3e23, rel=5e-2)
g8 = 8e9 / mc2_eV; lam_u = 0.032; K = 2.0
a_lab = K * c / g8 * 2 * math.pi * c / lam_u
check("SPring-8 静止系加速度", g8 * g8 * a_lab, 5.5e23, rel=5e-2)
check("Schwinger c²/λ̄_C", c ** 2 / lambar, 2.33e29)
check("(2/3)αβ²", (2 / 3) * alpha * beta2, 7.97e-6)
P = e ** 2 * a_int ** 2 / (6 * math.pi * eps0 * c ** 3)
check("内部運動の Larmor 出力 W", P, 0.829)
check("mc²/P s", me * c * c / P, 9.87e-14)

print("== T6.8 モードの梯子（整数 ℓ が出ないこと）==")
radii = {"λ_C/2": math.pi, "λ̄_C": 1.0, "λ_C": 2 * math.pi, "λ̄_C/2": 0.5}  # λ̄_C 単位
speeds = {"c": 1.0, "βc": beta}
targets = {"E0/2": 0.5, "βmc²": beta}
found_integer = False
for rn, R in radii.items():
    for sn, v in speeds.items():
        for tn, t in targets.items():
            x = (t * R / v) ** 2          # ℓ(ℓ+1)
            l = (-1 + math.sqrt(1 + 4 * x)) / 2
            near = abs(l - round(l)) < 0.03 and round(l) >= 1
            found_integer |= near
            print(f"    R={rn:6s} v={sn:3s} target={tn:5s} → ℓ={l:.3f}{'  <-- 整数近傍' if near else ''}")
print(f"[{'OK' if not found_integer else 'NG'}] 八通りで整数 ℓ は出ない")
ok_all &= not found_integer
# 参考: (λ_C/2, c) の ℓ=1,2,3
for l in (1, 2, 3):
    print(f"    (λ_C/2, c) ℓ={l}: {math.sqrt(l*(l+1))/math.pi*mc2_eV/1e3:.0f} keV")

print("== T6.9 シンクロトロン高調波 ==")
f0 = c / 26659; wc = 1.5 * g ** 3 * c / rho
check("LEP f0 Hz", f0, 1.12e4)
check("LEP 臨界 keV", hbar * wc / e / 1e3, 65.3)
check("LEP 高調波数", wc / (2 * math.pi * f0), 1.4e15)
check("LEP パルス幅 s", rho / (g ** 3 * c), 1.5e-20)
f0s = c / 1436; wcs = 1.5 * g8 ** 3 * c / 39.3
check("SPring-8 f0 Hz", f0s, 2.09e5)
check("SPring-8 臨界 keV", hbar * wcs / e / 1e3, 28.9)

print("== T6.13 Brillouin 帯の端 ==")
check("hν_ZB keV", h * nu_int / e / 1e3, 20.68)
check("βmc² keV", beta * mc2_eV / 1e3, 20.68)

print("== T6.14 膜のモード数 ==")
N = (8 * math.pi / 3) * (4 * math.pi / 3) * (1.5 / 2) ** 3
check("N ≈ 15", N, 14.8)

print("== T6.18 三つの半径 ==")
r_e = alpha * lambar
alpha_G = G * me ** 2 / (hbar * c)
lP = math.sqrt(hbar * G / c ** 3)
check("λ̄_C m", lambar, 3.862e-13)
check("r_e m", r_e, 2.818e-15)
check("α_G", alpha_G, 1.752e-45)
check("√α_G λ̄_C = ℓ_P", math.sqrt(alpha_G) * lambar, lP, rel=1e-6)
check("λ̄_C/ℓ_P", lambar / lP, 2.39e22)
EP_GeV = math.sqrt(hbar * c ** 5 / G) / e / 1e9
check("αE_P GeV", alpha * EP_GeV, 8.9e16)

print("== §5.1 T5 見直し用 ==")
th = 0.5 * math.asin(beta)
check("ΔH = mc² sin2θ0 eV", mc2_eV * math.sin(2 * th), beta * mc2_eV, rel=1e-9)
check("<H> 欠損 eV", mc2_eV * (1 - math.cos(2 * th)), 418.7)
check("419 eV / mc²", 418.7 / mc2_eV, 8.2e-4)

print("\n全項目:", "OK" if ok_all else "NG あり")
