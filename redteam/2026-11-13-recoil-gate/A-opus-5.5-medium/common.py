"""共通の定義（BRIEF.md §1 の設定）。

記号:
  th = θ = ωt,  c2 = cos(θ/2), s2 = sin(θ/2)
  E_A = E0 c2^4,  E_B = E0 s2^4,  K = ½ E0 sin²θ
  核 A = x_m - d/2,  核 B = x_m + d/2
  基準案: x_γ = x_m - (d/2) cos θ
エネルギーは E0 単位、長さは d 単位で扱うことが多い（すべて d と E0 に比例するため）。
"""
import sympy as sp
import numpy as np
from fractions import Fraction

th = sp.symbols('theta', real=True)
d, E0, C = sp.symbols('d E_0 C', positive=True)

EA = E0 * sp.cos(th / 2) ** 4
EB = E0 * sp.sin(th / 2) ** 4
K = sp.Rational(1, 2) * E0 * sp.sin(th) ** 2

# ---- 数値（BRIEF §1.2） ----
h = 6.62607015e-34
me = 9.1093837015e-31
c_light = 299792458.0
G = 6.67430e-11
nu = 5.0007e18
omega = 2 * np.pi * nu
lamC = 2.42631e-12          # BRIEF の値をそのまま使う
E0_J = me * c_light ** 2    # = 511 keV
keV = 1.602176634e-16


def fourier_cos_sin(f_num, nmax=16, M=4096):
    """2π 周期の数値関数 f(θ) の係数 a_n (cos nθ), b_n (sin nθ) を FFT で求める。"""
    t = np.arange(M) * 2 * np.pi / M
    y = f_num(t)
    F = np.fft.rfft(y) / M
    a = np.zeros(nmax + 1)
    b = np.zeros(nmax + 1)
    a[0] = F[0].real
    a[1:] = 2 * F[1:nmax + 1].real
    b[1:] = -2 * F[1:nmax + 1].imag
    return a, b


def frac(x, den=4096):
    """数値を分数で見やすくする（表示用）。"""
    if abs(x) < 1e-12:
        return "0"
    return str(Fraction(x).limit_denominator(den))


def show_series(name, a, b, tol=1e-10):
    terms = []
    for n in range(len(a)):
        if abs(a[n]) > tol:
            terms.append(f"{frac(a[n])}·cos{n}θ" if n else f"{frac(a[n])}")
        if abs(b[n]) > tol:
            terms.append(f"{frac(b[n])}·sin{n}θ")
    print(f"  {name} = " + (" + ".join(terms) if terms else "0"))
    return [n for n in range(len(a)) if abs(a[n]) > tol or abs(b[n]) > tol]


def to_num(expr, subs=None):
    subs = subs or {}
    return sp.lambdify(th, expr.subs({d: 1, E0: 1, C: 0, **subs}), 'numpy')
