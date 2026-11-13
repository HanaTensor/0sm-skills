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

G, c0 = 6.67430e-11, 299792458.0
me, lamC = 9.1093837139e-31, 2.42631023538e-12
beta = math.sqrt(0.00163798087)
nu = beta*c0/lamC; w = 2*math.pi*nu
P = G/(5*c0**5)*(2/3)*(me*lamC**2)**2*w**6*4045/4096
print("nu_ZB = %.4e Hz, P = %.3e W" % (nu, P))
hkeV = 4.135667696e-18
for n in (2, 4, 6):
    print("%dw: %.4e Hz, %.1f keV" % (n, n*nu, n*nu*hkeV))
