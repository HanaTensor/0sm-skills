"""
幹 T5 の T5.16 補「五つの半径」と T5.20「逆二乗の積と c⁴」（T5-2026-10-28-interaction-picture.md）の検算。
節記号 R1–R8 は幹 T5 の §4 と対応する。§4 のそれ以前の数値は T6-2026-09-15-verification.py（改番前の名のまま）。
定数は CODATA 2018。R3 だけは CGS-Gauss 単位で独立に計算し直す。
実行: python3 -I T5-2026-10-28-verification-radii.py   （全 22 項目 OK で終わる）
"""
import math
import sympy as sp

G = 6.67430e-11; c = 299792458.0; hbar = 1.054571817e-34; e = 1.602176634e-19
eps0 = 8.8541878128e-12; k = 1 / (4 * math.pi * eps0)
me = 9.1093837015e-31; mp = 1.67262192369e-27
alpha = k * e**2 / (hbar * c)
mP = math.sqrt(hbar * c / G); lP = math.sqrt(hbar * G / c**3); FP = c**4 / G

ok = 0
def check(label, cond):
    global ok
    assert cond, label
    ok += 1
    print(f"  OK  {label}")

def close(a, b, tol=1e-9):
    return abs(a / b - 1) < tol

# ---- R1 力の比 F_e/F_g = k e²/(G m₁m₂)。r に依らない ----
print("R1 力の比（三つの組）")
R = {}
for name, m1, m2 in (("e-e", me, me), ("p-e", mp, me), ("p-p", mp, mp)):
    R[name] = k * e**2 / (G * m1 * m2)
    print(f"    {name}: {R[name]:.4e}（10^{math.log10(R[name]):.2f}）")
check("e–e は 4.17×10⁴²", close(R["e-e"], 4.1656e42, 1e-4))
check("p–e は 2.27×10³⁹（#66 C1 の値と一致）", close(R["p-e"], 2.269e39, 1e-3))
check("「40 桁」は一つの数ではない ── 粒子を替えると 6.5 桁動く（質量の比 (m_p/m_e)² = 10^6.53）",
      abs(math.log10(R["e-e"] / R["p-p"]) - 2 * math.log10(mp / me)) < 1e-9)

# ---- R2 分解 F_e/F_g = α/α_G = α (m_P/m)²、c は比で厳密に消える ----
print("R2 分解と c の相殺")
aG = G * me**2 / (hbar * c)
print(f"    α = {alpha:.6e}（10^{math.log10(alpha):.2f}）、α_G = {aG:.4e}、(m_P/m_e)² = {(mP/me)**2:.4e}（10^{2*math.log10(mP/me):.2f}）")
check("α/α_G = α (m_P/m_e)² = F_e/F_g(e–e)", close(alpha / aG, R["e-e"]) and close(alpha * (mP / me)**2, R["e-e"]))
Gs, ks, es, ms, hs, cs = sp.symbols('G k e m hbar c', positive=True)
ratio_sym = (ks * es**2 / (hs * cs)) / (Gs * ms**2 / (hs * cs))
check("α/α_G は c も ħ も含まない（∂/∂c = ∂/∂ħ = 0）",
      sp.diff(ratio_sym, cs) == 0 and sp.diff(ratio_sym, hs) == 0)

# ---- R3 c⁴ の数値は単位系で変わり、比は変わらない ----
print("R3 単位系の依存")
for unit, f in (("m/s", 1), ("km/s", 1e-3), ("cm/s", 1e2), ("c = 1", 1 / c)):
    print(f"    c⁴ [{unit}] = {(c * f)**4:.3e}")
e_esu = 4.80320471e-10; G_cgs = 6.67430e-8; me_g = 9.1093837015e-28
R_cgs = e_esu**2 / (G_cgs * me_g**2)
print(f"    CGS-Gauss で独立に: e²/(G m_e²) = {R_cgs:.4e}")
check("c⁴ は m/s で 8.08×10³³、km/s で 8.08×10²¹（「32 乗」は SI の人工物）",
      close(c**4, 8.0776e33, 1e-4) and close((c * 1e-3)**4, 8.0776e21, 1e-4))
check("CGS-Gauss でも比は 4.17×10⁴²（単位に依らない）", close(R_cgs, R["e-e"], 1e-6))

# ---- R4 五つの半径 λ̄_C × {1, α, √α_G, √(α α_G), α_G} ----
print("R4 五つの半径")
lC = hbar / (me * c); re = alpha * lC; rQ = math.sqrt(G * k * e**2) / c**2; rg = G * me / c**2
for name, val, form in (("λ̄_C", lC, "1"), ("r_e", re, "α"), ("ℓ_P", lP, "√α_G"),
                        ("r_Q", rQ, "√(α α_G)"), ("r_g", rg, "α_G")):
    print(f"    {name:4s} = {val:.4e} m   ÷ λ̄_C = {val/lC:.4e}   [{form}]")
check("ℓ_P = √α_G λ̄_C（T5.16 の三段目）", close(lP, math.sqrt(aG) * lC))
check("r_g = G m_e/c² = α_G λ̄_C", close(rg, aG * lC))
check("重力の自己エネルギー G m²/r が mc² になるのは r_g（ℓ_P では √α_G = 4.2×10⁻²³ 倍）── T5.16 の ℓ_P の説明の訂正",
      close(G * me**2 / rg, me * c**2) and close(G * me**2 / lP / (me * c**2), math.sqrt(aG)))
check("ℓ_P² = λ̄_C r_g（ℓ_P は膜と r_g の幾何平均）", close(lP**2, lC * rg))
check("r_Q = √(G k e²)/c² = √(α α_G) λ̄_C = √α ℓ_P（質量を含まない）",
      close(rQ, math.sqrt(alpha * aG) * lC) and close(rQ, math.sqrt(alpha) * lP))
check("r_Q² = r_e r_g（r_Q は幾何平均）", close(rQ**2, re * rg))
check("F_e/F_g = r_e/r_g = (r_Q/r_g)² = (r_e/r_Q)² = α (λ̄_C/ℓ_P)²",
      all(close(x, R["e-e"]) for x in (re / rg, (rQ / rg)**2, (re / rQ)**2, alpha * (lC / lP)**2)))
s1, s2 = math.log10(re / rQ), math.log10(rQ / rg)
print(f"    log10(r_e/r_Q) = {s1:.3f}、log10(r_Q/r_g) = {s2:.3f}")
check("42.6 桁は r_Q を挟んで 21.3 + 21.3 に割れる", abs(s1 - s2) < 1e-9 and abs(s1 - 21.31) < 0.01)
print(f"    （書き換えの記帳）膜の面積 / Planck 面積 4π λ̄_C²/ℓ_P² = {4*math.pi*(lC/lP)**2:.2e}")

# ---- R5 各力を c⁴/G で割ると長さの比の二乗、積は 1/r⁴ ----
print("R5 Planck 力 c⁴/G で測る")
print(f"    c⁴/G = {FP:.4e} N")
check("F_e/(c⁴/G) = (r_Q/r)²、F_g/(c⁴/G) = (r_g/r)²（r = 10⁻¹⁰, 10⁻¹⁵ m）",
      all(close(k * e**2 / r**2 / FP, (rQ / r)**2) and close(G * me**2 / r**2 / FP, (rg / r)**2)
          for r in (1e-10, 1e-15)))
prod = lambda r: (k * e**2 / r**2) * (G * me**2 / r**2) / FP**2
slope = math.log(prod(1e-10) / prod(1e-12)) / math.log(1e-10 / 1e-12)
check("積 F_e F_g/(c⁴/G)² = (r_Q r_g)²/r⁴（傾き −4）", abs(slope + 4) < 1e-12 and close(prod(1e-10), (rQ * rg)**2 / 1e-40))

# ---- R6 掛け算が本物になる場所 ── RN の電荷項。質量が消える ----
print("R6 Reissner–Nordström の電荷項")
rs, Qs, e0s = sp.symbols('r Q epsilon_0', positive=True)
pot_prod = (ks * Qs**2 / (ms * cs**2 * rs)) * (Gs * ms / (cs**2 * rs))
check("(k Q²/(m c² r))·(G m/(c² r)) = G k Q²/(c⁴ r²) = r_Q²/r²、m を含まない",
      sp.simplify(pot_prod - Gs * ks * Qs**2 / (cs**4 * rs**2)) == 0 and sp.diff(pot_prod, ms) == 0)
E_field = Qs / (4 * sp.pi * e0s * rs**2)
u_E = e0s * E_field**2 / 2
curv = sp.simplify(8 * sp.pi * Gs / cs**4 * u_E)
check("(8πG/c⁴)·(ε₀E²/2) = G Q²/(4πε₀ c⁴ r⁴) = r_Q²/r⁴（係数 1、1/r⁴ はここにある）",
      sp.simplify(curv - Gs * Qs**2 / (4 * sp.pi * e0s * cs**4 * rs**4)) == 0)

# ---- R7 幾何学化した電荷/質量 ----
print("R7 幾何学化した Q/M（極限 RN は 1）")
rQp = rQ; rgp = G * mp / c**2
print(f"    電子 r_Q/r_g = {rQ/rg:.3e}、陽子 = {rQp/rgp:.3e}")
check("電子の Q/M = 2.04×10²¹ = √(F_e/F_g)", close(rQ / rg, math.sqrt(R["e-e"])) and close(rQ / rg, 2.041e21, 1e-3))

# ---- R8 標準理論側の照合（外部入力を含む） ----
print("R8 数あわせと大数仮説")
a20 = alpha**-20
print(f"    α⁻²⁰ = {a20:.3e}（F_e/F_g の {a20/R['e-e']:.2f} 倍）")
check("α⁻²⁰ は 1.31 倍ずれる（一致は探せば出る、の記帳）", abs(a20 / R["e-e"] - 1.31) < 0.01)
t0 = 13.787e9                     # 年。Planck 2018
Gdot_dirac = -1 / t0
Gdot_llr, sig_llr = -5.0e-15, 9.6e-15   # 年⁻¹。LLR、2025 年の総説が引く値（2026-10-28 確認、外部入力）
excl = abs(Gdot_dirac) / (2 * sig_llr)
print(f"    Dirac: Ġ/G = −1/t₀ = {Gdot_dirac:.2e} /年、LLR ({Gdot_llr:.1e} ± {sig_llr:.1e}) /年 → 2σ で {excl:.0f} 倍")
check("Dirac の大数仮説は LLR で 10³ 倍以上排除", excl > 1e3)

print(f"\n全 {ok} 項目 OK")
