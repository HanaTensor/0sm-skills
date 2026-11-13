"""Q5: D 一定（Q2 の解）での二階モーメント J と四重極放射。"""
import sympy as sp
import numpy as np
from common import *

u = sp.symbols('u')   # u = cos θ
xm = C + d / 2 * sp.cos(th) * (1 + sp.sin(th) ** 2 / 2)
xA, xB = xm - d / 2, xm + d / 2
xg = xm - d / 2 * sp.cos(th)
xc = C

J = EA * (xA - xc) ** 2 + EB * (xB - xc) ** 2 + K * (xg - xc) ** 2
# cos θ の多項式に直す
Ju = sp.expand(sp.simplify(J.subs({sp.cos(th / 2) ** 4: ((1 + u) / 2) ** 2}))
               .rewrite(sp.cos))
Ju = J.subs(th, sp.acos(u))
Ju = sp.expand(sp.simplify(sp.expand_trig(Ju)))
Ju = sp.expand(sp.simplify(Ju.subs(sp.sqrt(1 - u ** 2) ** 2, 1 - u ** 2)))
print("J/(E0 d²) を u=cosθ の多項式で:")
Jpoly = sp.Poly(sp.simplify(Ju / (E0 * d ** 2)), u)
print("  ", Jpoly.as_expr())
print("  因数分解:", sp.factor(Jpoly.as_expr()))

# チェビシェフ展開 → cos nθ の係数（厳密）
coeffs = {}
p = Jpoly.as_expr()
deg = sp.degree(p, u)
for n in range(deg, -1, -1):
    an = sp.Poly(p, u).coeff_monomial(u ** n) if n <= sp.degree(p, u) else 0
    if an == 0:
        continue
    cn = an / (2 ** (n - 1)) if n >= 1 else an
    coeffs[n] = sp.nsimplify(cn)
    p = sp.expand(p - cn * sp.chebyshevt(n, u))
print("\nJ/(E0 d²) = Σ a_n cos nθ（厳密）:")
for n in sorted(coeffs):
    print(f"   n={n}: a_n = {coeffs[n]}  ({float(coeffs[n]):+.6e})")
# 数値でも確認
a, b = fourier_cos_sin(to_num(J / (E0 * d ** 2)), nmax=14)
show_series("J/(E0 d²) [FFT]", a, b)

# 閉じた形（θ 表示）
Jclosed = sum(coeffs[n] * sp.cos(n * th) for n in coeffs)
fdiff = to_num(J / (E0 * d ** 2) - Jclosed)
fclosed = to_num(J / (E0 * d ** 2) - sp.sin(th) ** 4 * (1 + sp.sin(th) ** 2) / 16)
_t = np.linspace(0, 2 * np.pi, 10001)
print("\n照合 max|J - Σ a_n cos nθ| =", np.max(np.abs(fdiff(_t))))
print("閉じた形 J = (E0 d²/16) sin⁴θ (1 + sin²θ):  max 差 =", np.max(np.abs(fclosed(_t))))

# 四重極出力: I = J/c²,  P = (2G/(15 c⁵)) <I'''²>,  I''' の n 次成分振幅 = a_n (nω)³ E0 d²/c²
print("\n高調波ごとの出力の取り分 ∝ (n³ a_n)²:")
w = {n: float(coeffs[n]) ** 2 * n ** 6 for n in coeffs if n > 0}
tot = sum(w.values())
for n in sorted(w):
    print(f"   {n}ω: {w[n]/tot*100:8.4f} %   (n³a_n = {n**3*float(coeffs[n]):+.6f})")

S = sum(0.5 * (n ** 3 * float(coeffs[n])) ** 2 for n in coeffs if n > 0)   # <(J'''/(ω³E0d²))²>
print(f"\n<(d³J/dθ³)²>/(E0 d²)² = {S:.6f}")
# 時間平均の直接確認
fJ3 = to_num(sp.diff(J, th, 3) / (E0 * d ** 2))
tt = np.linspace(0, 2 * np.pi, 400000, endpoint=False)
print(f"   直接平均 = {np.mean(fJ3(tt)**2):.6f}")

for dd, name in [(lamC / 2, "λC/2"), (lamC, "λC")]:
    I3sq = S * (omega ** 3 * E0_J * dd ** 2 / c_light ** 2) ** 2
    P = 2 * G / (15 * c_light ** 5) * I3sq
    Ecyc = E0_J
    print(f"\n d={name}:  P_GW = {P:.4e} W")
    print(f"   = (2/15)·S·G E0² ω⁶ d⁴ / c⁹ ;  P/(E0 ν) = {P/(E0_J*nu):.3e} （一周期あたりに失う割合）")
    print(f"   減衰時間 E0/P = {E0_J/P:.3e} s = {E0_J/P/3.156e7:.3e} 年")
    # 無次元化: P = (2/15) S (G m_e²/(ħc))·... 参考に α_G
    hbar = h / (2 * np.pi)
    aG = G * me ** 2 / (hbar * c_light)
    print(f"   参考 α_G = G m_e²/(ħc) = {aG:.4e}")
