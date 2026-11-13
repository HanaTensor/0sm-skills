#!/usr/bin/env python3
"""Paper #67 (provisional): channels of the energy identity, recoil closure, quadrupole.
Requires numpy only."""
import math
import numpy as np

N = 4096
t = np.linspace(0, 2*np.pi, N, endpoint=False)
d = 1.0
TA, TB, K = np.cos(t/2)**4, np.sin(t/2)**4, 0.5*np.sin(t)**2

def check(label, ok):
    print(("PASS " if ok else "FAIL ") + label)

check("identity TA+TB+K = 1", np.allclose(TA+TB+K, 1))
check("Fourier TA = 3/8 + cos/2 + cos2/8", np.allclose(TA, 3/8 + np.cos(t)/2 + np.cos(2*t)/8))
check("Fourier TB = 3/8 - cos/2 + cos2/8", np.allclose(TB, 3/8 - np.cos(t)/2 + np.cos(2*t)/8))
check("Fourier K  = 1/4 - cos2/4", np.allclose(K, 1/4 - np.cos(2*t)/4))

X = (d/2)*np.cos(t)*(1 + 0.5*np.sin(t)**2)
xg = X - (d/2)*np.cos(t)
D = TA*(X - d/2) + TB*(X + d/2) + K*xg
check("dipole vanishes under recoil closure (max |D| < 1e-14)", np.abs(D).max() < 1e-14)

J = TA*(X - d/2)**2 + TB*(X + d/2)**2 + K*xg**2
check("J = sin^4 (1+sin^2)/16", np.allclose(J, np.sin(t)**4*(1 + np.sin(t)**2)/16))
check("J = (22 - 31cos2 + 10cos4 - cos6)/512",
      np.allclose(J, (22 - 31*np.cos(2*t) + 10*np.cos(4*t) - np.cos(6*t))/512))

c = np.fft.rfft(J)/N
amp = np.array([abs(c[0])] + [2*abs(c[k]) for k in range(1, 9)])
check("only even harmonics up to 6", np.allclose(amp[[1, 3, 5, 7, 8]], 0, atol=1e-14))
k = np.arange(9); pw = (amp*k**3)**2; pw[0] = 0; share = pw/pw.sum()
print("amplitudes 2w,4w,6w:", amp[2], amp[4], amp[6])
print("power shares 2w,4w,6w: %.4f %.4f %.4f" % (share[2], share[4], share[6]))
J3 = sum((amp[k]*k**3)**2/2 for k in (2, 4, 6))
check("mean square of d3J/dtheta3 = 4045/4096", abs(J3 - 4045/4096) < 1e-12)


# Momentum bookkeeping on the closure (units E0 = omega = d = 1)
g = lambda f: np.gradient(f, t, edge_order=2)
xA, xB = X - d/2, X + d/2
bodies = (TA + TB)*g(X) + K*g(xg)
transfer = g(TA)*xA + g(TB)*xB + g(K)*xg
check("bodies = -(1/2) sin^3",  np.allclose(bodies, -0.5*np.sin(t)**3, atol=1e-5))
check("transfer = +(1/2) sin^3", np.allclose(transfer, 0.5*np.sin(t)**3, atol=1e-5))
check("total momentum = 0", np.allclose(bodies + transfer, 0, atol=1e-5))
check("largest kernel speed = (3/4) omega d", abs(np.abs(g(X)).max() - 0.75) < 1e-4)
check("largest photon-sphere speed = (1/4) omega d", abs(np.abs(g(xg)).max() - 0.25) < 1e-4)

# The form of Paper #58: Q proportional to T_A - T_B with fixed kernels
dE = TA - TB
check("T_A - T_B = cos(theta)", np.allclose(dE, np.cos(t)))
check("T_A - T_B is odd under exchange (theta -> theta + pi)",
      np.allclose(np.roll(dE, N//2), -dE))

# Largest kernel speed against the group velocity c/n = beta c of Paper #66 (d = lambda_C/2)
# (3/4) omega d / (beta c) with omega = 2 pi beta c / lambda_C and d = lambda_C/2 gives 3 pi / 4
ratio = 3*math.pi/4
for b_test in (math.sqrt(0.00163798087), 0.01, 0.1):
    lam_test = 1.0
    v_max = 0.75*(2*math.pi*b_test/lam_test)*(lam_test/2)     # in units of c
    check("v_kernel,max / (c/n) = 3 pi / 4 = %.4f for beta = %.5f" % (v_max/b_test, b_test),
          abs(v_max/b_test - ratio) < 1e-12)
above = np.abs(np.sin(t))**3 > 1/ratio
frac_closed = 1 - 2*math.asin((1/ratio)**(1/3))/math.pi
check("fraction of the cycle with v_kernel > c/n = %.3f (closed form %.4f)" % (above.mean(), frac_closed),
      abs(above.mean() - frac_closed) < 1e-3)

G, c0 = 6.67430e-11, 299792458.0
me, lamC = 9.1093837139e-31, 2.42631023538e-12
beta = math.sqrt(0.00163798087)
nu = beta*c0/lamC; w = 2*math.pi*nu
for dd, name in ((lamC/2, "lambda_C/2"), (lamC, "lambda_C")):
    P = G/(5*c0**5)*(2/3)*(me*dd**2)**2*w**6*4045/4096
    age = 13.787e9*3.15576e7
    print("d = %-10s P = %.3e W, loss over age = %.2e eV, v_kernel/c = %.4f, energy in transit/E0 >= %.4f"
          % (name, P, P*age/1.602176634e-19, 0.75*w*dd/c0, w*dd/(2*c0)))
print("nu_ZB = %.4e Hz" % nu)
hkeV = 4.135667696e-18
for n in (2, 4, 6):
    print("%dw: %.4e Hz, %.1f keV" % (n, n*nu, n*nu*hkeV))
