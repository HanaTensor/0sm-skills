#!/usr/bin/env python3
"""Paper #66: Subluminal Zitterbewegung and the Invariant Speed.
Reproduces every number of the Letter and checks the identities of Appendix B.
Requires numpy only."""
import math
import numpy as np

def check(label, ok):
    print(("PASS " if ok else "FAIL ") + label)

c = 299792458.0            # m/s
h = 6.62607015e-34         # J s
me = 9.1093837139e-31      # kg
eV = 1.602176634e-19       # J
alpha = 1/137.035999177

beta2 = 0.00163798087      # Paper #10
beta = math.sqrt(beta2)
n = 1/beta
lamC = h/(me*c)
mc2 = me*c**2/eV           # eV

nuC  = c/lamC              # light-speed reference
nuZB = beta*c/lamC         # 0-Sphere transport frequency
nuD  = 2*me*c**2/h         # Dirac ZB frequency

print(f"beta       = {beta:.6f}")
print(f"n = 1/beta = {n:.3f},  n^2 = {n*n:.2f}")
print(f"sqrt(2)pi/alpha = {math.sqrt(2)*math.pi/alpha:.2f}  "
      f"(ratio {n*n/(math.sqrt(2)*math.pi/alpha):.4f})")
print(f"lambda_C   = {lamC:.5e} m")
print(f"nu_C       = {nuC:.4e} Hz")
print(f"nu_ZB      = {nuZB:.4e} Hz,  E = {beta*mc2/1e3:.2f} keV")
print(f"nu_D       = {nuD:.4e} Hz,  E = {2*mc2/1e6:.3f} MeV")
print(f"nu_D/nu_ZB = {nuD/nuZB:.2f}  (2/beta = {2/beta:.2f})")
print(f"layers     = {mc2/1e3:.1f} keV : {beta*mc2/1e3:.2f} keV : {0.5*beta2*mc2:.1f} eV")
print(f"drag 1-1/n^2 = {1-1/n**2:.6f}")
print(f"theta_c    = {math.degrees(math.asin(1/n)):.2f} deg")

# Appendix B: identity, rates, gradient, Fourier content, discrete group index
t = np.linspace(0, 2*np.pi, 4096, endpoint=False)
TA, TB, K = np.cos(t/2)**4, np.sin(t/2)**4, 0.5*np.sin(t)**2
check("identity TA+TB+K = 1", np.allclose(TA + TB + K, 1))
dTA = -2*np.cos(t/2)**3*np.sin(t/2)
dTB = 2*np.sin(t/2)**3*np.cos(t/2)
dK = np.sin(t)*np.cos(t)
check("radiation gradient dTB - dTA = sin(theta)", np.allclose(dTB - dTA, np.sin(t)))
check("conservation dTA + dTB + dK = 0", np.allclose(dTA + dTB + dK, 0))
check("TA = 3/8 + cos/2 + cos2/8", np.allclose(TA, 3/8 + np.cos(t)/2 + np.cos(2*t)/8))
check("TB = 3/8 - cos/2 + cos2/8", np.allclose(TB, 3/8 - np.cos(t)/2 + np.cos(2*t)/8))
check("K  = 1/4 - cos2/4", np.allclose(K, 1/4 - np.cos(2*t)/4))
for name, f in (("TA", TA), ("TB", TB), ("K", K)):
    c = np.fft.rfft(f)/len(t)
    check(name + ": no frequency above 2w", np.allclose(np.abs(c[3:20]), 0, atol=1e-14))
# discrete group index: two lines omega, 2omega
for n1, n2 in ((n, n), (n, 1.01*n)):
    vg = 1/(2*n2 - n1)
    print("n1=%.4f n2=%.4f -> v_g/c = %.6f (c/n = %.6f)" % (n1, n2, vg, 1/n))
