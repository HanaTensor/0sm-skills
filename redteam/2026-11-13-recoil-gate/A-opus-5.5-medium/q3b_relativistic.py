"""Q3 補: 核の速さ ~0.1–0.2c の相対論補正の大きさ。

読み R: BRIEF の T_A, T_B を「核対の静止系でのエネルギー」と読むと、実験室系では γ(v_m) 倍になる。
すると (1) 全エネルギーが E0 で一定でなくなり、(2) D 一定の x_m も変わる。
光子球は塊として K（v_γ の γ も掛ける）とする。固定点反復で D 一定の x_m を求め、
基準解からのずれと、全エネルギーの揺れを測る。
"""
import numpy as np
from common import omega, lamC, c_light

M = 2 ** 14
t = np.arange(M) * 2 * np.pi / M
EA, EB, K = np.cos(t / 2) ** 4, np.sin(t / 2) ** 4, 0.5 * np.sin(t) ** 2

def deriv(y):
    return (np.roll(y, -1) - np.roll(y, 1)) / (2 * (2 * np.pi / M))

for dd, nm in [(lamC / 2, "λC/2"), (lamC, "λC")]:
    eps = omega * dd / c_light          # v/c = eps · dx/dθ（x は d 単位）
    xm0 = 0.5 * np.cos(t) * (1 + 0.5 * np.sin(t) ** 2)
    xm = xm0.copy()
    for it in range(2000):
        g_m = 1 / np.sqrt(1 - (eps * deriv(xm)) ** 2)
        xg = xm - 0.5 * np.cos(t)
        g_g = 1 / np.sqrt(1 - (eps * deriv(xg)) ** 2)
        Ep, Kp = g_m * (EA + EB), g_g * K
        # D = Ep x_m + (d/2)g_m(E_B-E_A) + Kp x_γ = 一定（0）を x_m について解く
        new = -(0.5 * g_m * (EB - EA) - 0.5 * Kp * np.cos(t)) / (Ep + Kp)
        # 高い調和（>31ω）を落として数値微分の雑音の増幅を止め、緩和して進める
        Fn = np.fft.rfft(new); Fn[32:] = 0; new = np.fft.irfft(Fn, M)
        new = 0.5 * xm + 0.5 * new
        if np.max(np.abs(new - xm)) < 1e-14:
            break
        xm = new
    Etot = g_m * (EA + EB) + g_g * K
    print(f"d={nm}: 反復 {it} 回, max|x_m - x_m(非相対論)| = {np.max(np.abs(xm-xm0)):.4e} d,"
          f" 全エネルギーの揺れ max|E-E0|/E0 = {np.max(np.abs(Etot-1)):.4e}")
    F = np.fft.rfft(xm) / M
    print("    x_m/d の成分: " + ", ".join(f"{n}ω:{2*abs(F[n]):.5f}" for n in range(1, 10) if 2 * abs(F[n]) > 1e-6))
