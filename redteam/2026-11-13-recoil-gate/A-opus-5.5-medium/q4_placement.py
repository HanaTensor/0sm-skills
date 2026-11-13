"""Q4: 光子球の置き方への依存（＋ Q5 の J を各案で）。

一般形: 光子球の重心を x_γ = x_m + (d/2) g(θ)、その内部の広がり（分散）を σ²(θ) とする。
  c²D = E0 x_m - (d/2) E0 cosθ + K (d/2) g      （E_B - E_A = -E0 cosθ）
  D 一定 ⇔ x_m = C + (d/2)[cosθ - (K/E0) g]
  J = E_A (x_A-C)² + E_B (x_B-C)² + K[(x_γ-C)² + σ²]
案:
  base : g = -cosθ, σ² = 0                     （BRIEF §1.3）
  (i)  : g = 0,     σ² = d²/12                  （K が二核のあいだに一様）
  (ii) : g = 三角波（A→B を一定の速さで往復）, σ² = 0
  (iii): g を「移送の運動量 P_tr が 0」になるよう選ぶ（局所的な受け渡し）→ g = -1/cosθ
  読み B: base に核の静止エネルギー Mc² を足す（J への影響）
"""
import numpy as np
from common import omega, lamC, c_light, nu, E0_J, G, frac

M = 2 ** 16
t = np.arange(M) * 2 * np.pi / M
cA, sA = np.cos(t / 2), np.sin(t / 2)
EA, EB, K = cA ** 4, sA ** 4, 0.5 * np.sin(t) ** 2
a_flow = 2 * cA ** 3 * sA          # -dE_A/dθ
b_flow = 2 * sA ** 3 * cA          # dE_B/dθ

def deriv(y):
    """周期関数の数値微分（中心差分、刻み 2π/M）。"""
    return (np.roll(y, -1) - np.roll(y, 1)) / (2 * (2 * np.pi / M))

def series(y, nmax=12, tol=1e-9):
    F = np.fft.rfft(y) / M
    a = 2 * F.real; a[0] /= 2
    b = -2 * F.imag
    out = []
    for n in range(nmax + 1):
        if abs(a[n]) > tol: out.append(f"{a[n]:+.6f}cos{n}θ")
        if abs(b[n]) > tol and n: out.append(f"{b[n]:+.6f}sin{n}θ")
    return " ".join(out), a, b

def tri(t):
    tm = np.mod(t, 2 * np.pi)
    return np.where(tm <= np.pi, -1 + 2 * tm / np.pi, 3 - 2 * tm / np.pi)

cases = {
    "base": (-np.cos(t), np.zeros(M)),
    "(i) 一様": (np.zeros(M), np.full(M, 1 / 12)),
    "(ii) 三角波": (tri(t), np.zeros(M)),
}

def analyse(name, g, sig2, Mrest=0.0):
    print(f"\n==================== {name} ====================")
    Etot = 1 + 2 * Mrest
    xm = (0.5 * np.cos(t) - K * 0.5 * g) / Etot        # d=1, C=0
    xA, xB, xg = xm - 0.5, xm + 0.5, xm + 0.5 * g
    D = EA * xA + EB * xB + K * xg + Mrest * (xA + xB)
    print(f"  max|c²D/(E0 d)| (定数 0 のはず) = {np.max(np.abs(D)):.2e}")
    s, a, b = series(xm)
    print(f"  x_m/d = {s}")
    print(f"  x_m の値域/d: [{xm.min():.5f}, {xm.max():.5f}]  （振幅 {(xm.max()-xm.min())/2:.5f} d）")
    v = deriv(xm)
    vmax = np.max(np.abs(v))
    for dd, nm in [(lamC / 2, "λC/2"), (lamC, "λC")]:
        print(f"  d={nm}: 核の v_max = {vmax*omega*dd/c_light:.5f} c,  光子球の v_max = "
              f"{np.max(np.abs(deriv(xg)))*omega*dd/c_light:.5f} c")
    # 移送の運動量と、それを光速以下で運ぶのに要るエネルギー
    if name.startswith("(i)"):
        # 区間内の流束 S(x) は x_A で a、x_B で b の一次式（対の静止系）
        xs = np.linspace(0, 1, 401)
        Sabs = np.array([np.trapz(np.abs(a_flow[k] + (b_flow[k] - a_flow[k]) * xs), xs) for k in range(0, M, 64)])
        Ptr = 0.5 * (a_flow + b_flow)
        Etr = Sabs
    else:
        Ptr = a_flow * (xg - xA) + b_flow * (xB - xg)
        Etr = np.abs(a_flow * (xg - xA)) + np.abs(b_flow * (xB - xg))
    Pkin = (EA + EB + 2 * Mrest) * v + K * deriv(xg)
    print(f"  max|P_kin + P_tr| (0 のはず) = {np.max(np.abs(Pkin + Ptr)):.2e}")
    s, _, _ = series(Ptr)
    print(f"  P_tr c²/(ω E0 d) = {s}")
    for dd, nm in [(lamC / 2, "λC/2"), (lamC, "λC")]:
        print(f"  d={nm}: 移送中に要る最小エネルギー max E_tr/E0 = {np.max(Etr)*omega*dd/c_light:.4f}")
    # J
    J = EA * xA ** 2 + EB * xB ** 2 + K * (xg ** 2 + sig2) + Mrest * (xA ** 2 + xB ** 2)
    s, aJ, bJ = series(J, nmax=12)
    print(f"  J/(E0 d²) = {s}")
    F = np.fft.rfft(J) / M
    an = 2 * np.abs(F)
    n = np.arange(len(F))
    odd = np.max(an[1::2][:200])
    print(f"  奇数倍の成分の最大 |a_n| = {odd:.2e}")
    w = (n ** 3 * an) ** 2 / 2
    w[0] = 0
    S = w[: M // 8].sum()
    shares = w / S
    top = [(k, shares[k]) for k in range(1, 40) if shares[k] > 1e-4]
    print("  出力の取り分: " + ", ".join(f"{k}ω:{p*100:.2f}%" for k, p in top))
    tail = shares[13:M // 8].sum()
    print(f"  12ω を超える成分の合計 = {tail*100:.3f}%   S=<J'''²>/(E0d²)²ω⁶ = {S:.5f}")
    for dd, nm in [(lamC, "λC")]:
        P = 2 * G / (15 * c_light ** 5) * S * (omega ** 3 * E0_J * dd ** 2 / c_light ** 2) ** 2
        print(f"  d={nm}: P_GW = {P:.4e} W")
    return xm, J

for nm, (g, s2) in cases.items():
    analyse(nm, g, s2)

# (iii) 局所的な受け渡し: a(1+g) + b(1-g) = 0 → g = -(a+b)/(a-b) = -1/cosθ
print("\n==================== (iii) P_tr = 0 となる置き方 ====================")
for th in [0.0, 0.5, 1.0, 1.4, 1.55, 1.5707]:
    print(f"  θ={th:6.4f}: g = -1/cosθ = {-1/np.cos(th):10.3f}  → x_γ - x_m = {-0.5/np.cos(th):9.3f} d")
print("  |g| ≥ 1 で光子球は常に二核の外側にあり、θ→π/2 で無限遠へ発散する。物理的に採れない。")

# 読み B（核の静止エネルギー）で J の成分がどう変わるか
for Mr in [1.0, 1836.15]:
    analyse(f"読み B: base, Mc² = {Mr} E0", -np.cos(t), np.zeros(M), Mrest=Mr)
