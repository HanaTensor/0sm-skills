#!/usr/bin/env python3
"""Trunk T8 version 2026-10-31 (T8.13-T8.17): can 0SM predict g (and G)?  Numerical checks.

Sections B1-B7 (= T8 §4 X1-X7).  Constants: CODATA 2022.  Run: python3 -I T8-2026-10-31-verification-g.py
"""
import math
import numpy as np

# ---- CODATA 2022 -------------------------------------------------------------
c = 299792458.0
h = 6.62607015e-34
hbar = h / (2 * math.pi)
me = 9.1093837139e-31
mp = 1.67262192595e-27
G = 6.67430e-11
uG = 0.00015 / 6.67430            # relative standard uncertainty of G (2.2e-5)
alpha = 7.2973525643e-3
ae = 1.15965218059e-3
a0_codata = 5.29177210544e-11

lamC = h / (me * c)
lamCbar = hbar / (me * c)
mP = math.sqrt(hbar * c / G)
lP = math.sqrt(hbar * G / c**3)
alphaG = G * me**2 / (hbar * c)
aS = c**2 / lamCbar                # Schwinger acceleration
a0 = lamCbar / alpha               # Bohr radius, exact relation (CODATA a0 agrees to ~1e-11)

results = []


def check(name, cond):
    results.append((name, bool(cond)))
    print(("  OK  " if cond else "  NG  ") + name)


# ---- B1 bridge equation (#10 eq. III.4-RMS, #15 eq. gamma = 1 + a) -----------
print("B1 bridge equation")
gam_rms = 1 + ae / math.sqrt(2)
beta = math.sqrt(1 - 1 / gam_rms**2)
beta_max = math.sqrt(1 - 1 / (1 + ae)**2)
print(f"  beta_RMS = {beta:.8f}, beta^2 = {beta**2:.11f}, beta_max (gamma = 1 + a) = {beta_max:.5f}")
check("beta_RMS = 0.040472 (#10)", abs(beta - 0.040472) < 1e-6)
check("beta^2 = 0.00163798087 (index §2) to 1e-7 relative (9th digit depends on the a_e input)",
      abs(beta**2 / 0.00163798087 - 1) < 1e-7)
check("Bohr radius lamCbar/alpha = CODATA a0", abs(a0 / a0_codata - 1) < 1e-9)

# ---- B2 Earth's g is not a single number -------------------------------------
print("B2 Earth's g")
GM_E, R_E = 3.986004418e14, 6.3710e6
print(f"  GM/R_mean^2 = {GM_E / R_E**2:.4f} m/s^2; g_n = 9.80665 (CGPM 1901 convention); "
      f"equator 9.780, pole 9.832 (spread {(9.832 - 9.780) / 9.80665:.2%})")

# ---- B3 planetary surface-gravity scale from fundamental constants -----------
# Weisskopf 1975 / Press-Lightman 1983 scaling: gravitational energy per nucleon ~ atomic energy
#   M* = (alpha/alphaG_p)^(3/2) m_p,  R* = (alpha/alphaG_p)^(1/2) a0
print("B3 planetary scale")


def gstar_for(m_nucleon):
    aGp = G * m_nucleon**2 / (hbar * c)
    R = math.sqrt(alpha / aGp) * a0
    M = (alpha / aGp)**1.5 * m_nucleon
    return G * M / R**2, M, R


g_star, M_star, R_star = gstar_for(mp)
g_star_0sm = alpha**2.5 * (lP / lamCbar) * aS          # alpha^(5/2) (l_P/lamCbar) c^2/lamCbar
print(f"  M* = {M_star:.3e} kg, R* = {R_star:.3e} m, g* = {g_star:.2f} m/s^2")
print(f"  alpha^(5/2) (l_P/lamCbar) (c^2/lamCbar) = {g_star_0sm:.2f} m/s^2")
check("g* = alpha^(5/2) (m_e/m_P) a_S identically", abs(g_star / g_star_0sm - 1) < 1e-12)
check("m_p drops out (g* unchanged when m_p is doubled)", abs(gstar_for(2 * mp)[0] / g_star - 1) < 1e-12)
a_rigid = 4 * c**2 / lamC                              # T8.9 rigid limit of the two kernels
check("g* = alpha^(5/2)(m_e/m_P)(pi/2) a_rigid (T8.9)",
      abs(alpha**2.5 * (me / mP) * (math.pi / 2) * a_rigid / g_star - 1) < 1e-12)
planets = {  # GM [m^3 s^-2], mean radius [m]  (NASA fact sheets)
    "Moon": (4.9048695e12, 1.7374e6), "Mars": (4.282837e13, 3.3895e6),
    "Venus": (3.24859e14, 6.0518e6), "Earth": (3.986004418e14, 6.3710e6),
    "Uranus": (5.793939e15, 2.5362e7), "Neptune": (6.836529e15, 2.4622e7),
    "Saturn": (3.7931187e16, 5.8232e7), "Jupiter": (1.26686534e17, 6.9911e7),
}
for name, (gm, r) in planets.items():
    g = gm / r**2
    print(f"  {name:8s} g = {g:6.2f}  g/g* = {g / g_star:5.3f}  R/R* = {r / R_star:5.3f}  "
          f"M/M* = {gm / G / M_star:.2e}")

# ---- B4 0SM reading: the two-kernel beat (T8.5, T8 W9) -----------------------
print("B4 kernel beat")
d = lamC / 2
beat_E = 9.80665 * d / c**2
beat_star = g_star * d / c**2
print(f"  Earth g d/c^2 = {beat_E:.3e};  at g*: {beat_star:.3e} = pi alpha^(5/2) (m_e/m_P)")
check("Earth beat = 1.32e-28 (T8 W9)", abs(beat_E / 1.32e-28 - 1) < 0.01)
check("beat at g* = pi alpha^(5/2) m_e/m_P", abs(math.pi * alpha**2.5 * me / mP / beat_star - 1) < 1e-12)

# ---- B5 where the 10^45 reappears --------------------------------------------
print("B5 the 10^45")
G_ps = c**2 * (lamC / 2) / (3 * me)          # 0SM photon sphere lamC/2 = GR photon sphere 3Gm/c^2
G_jac = c**3 * lamCbar**2 / hbar             # Jacobson eta = 1/(4 cell), cell = lamCbar^2
print(f"  m_e/m_P = {me / mP:.4e}, (lamCbar/l_P)^2 = 1/alpha_G = {1 / alphaG:.4e}")
print(f"  G needed for lamC/2 = 3Gm/c^2: {G_ps:.3e} = {G_ps / G:.3e} G = (pi/3)/alpha_G")
print(f"  Jacobson with a Compton cell: G' = {G_jac / G:.3e} G")
print(f"  Sakharov at the Compton cutoff: N ~ 1/alpha_G = {1 / alphaG:.2e} (membrane modes, T5.12: ~15)")
print(f"  BH entropy of a horizon placed at the membrane: pi/alpha_G = {math.pi / alphaG:.3e} k_B")
check("G_ps/G = (pi/3)/alpha_G", abs(G_ps / G / (math.pi / 3 / alphaG) - 1) < 1e-12)
check("G'/G = 1/alpha_G", abs(G_jac / G * alphaG - 1) < 1e-12)

# ---- B6 look-elsewhere: beta^i alpha^j pi^k 2^l 3^m ---------------------------
print("B6 look-elsewhere")
I = np.arange(-40, 41)
J, K, L, M = np.meshgrid(np.arange(-30, 31), np.arange(-8, 9), np.arange(-12, 13),
                         np.arange(-8, 9), indexing="ij")
base = J * math.log(alpha) + K * math.log(math.pi) + L * math.log(2) + M * math.log(3)
cbase = np.abs(J) + np.abs(K) + np.abs(L) + np.abs(M)
n_formulas = I.size * base.size
for tname, tval, u in (("alpha_G", alphaG, uG), ("m_P/m_e", mP / me, uG / 2)):
    lt = math.log(tval)
    hit_u, hit_1pc, hit_W, best = 0, 0, 0, []
    W = 0.05
    for i in I:
        diff = i * math.log(beta) + base - lt
        a = np.abs(diff)
        hit_u += int((a < u).sum())
        hit_1pc += int((a < 0.01).sum())
        hit_W += int((a < W).sum())
        for idx in zip(*np.nonzero(a < u)):
            best.append((abs(i) + int(cbase[idx]), int(i), int(J[idx]), int(K[idx]), int(L[idx]),
                         int(M[idx]), float(diff[idx])))
    best.sort()
    print(f"  {tname}: {n_formulas:.2e} formulas; within 1%: {hit_1pc}; within +-{u:.1e} "
          f"(G's own uncertainty): {hit_u} (smooth expectation {hit_W * u / W:.1f})")
    for b in best[:4]:
        v = beta**b[1] * alpha**b[2] * math.pi**b[3] * 2.0**b[4] * 3.0**b[5]
        print(f"    beta^{b[1]} alpha^{b[2]} pi^{b[3]} 2^{b[4]} 3^{b[5]} = {v:.6e} vs {tval:.6e} "
              f"(ratio - 1 = {v / tval - 1:+.1e})")
    check(f"{tname}: hits at G precision exist in a modest formula space", hit_u >= 1)
r16 = beta**-16 / (mP / me)
r20 = alpha**-20 / (alpha / alphaG)
print(f"  beta^-16 / (m_P/m_e) = {r16:.3f};  exp(-2/beta)/(m_e/m_P) = {math.exp(-2 / beta) / (me / mP):.2f};"
      f"  alpha^-20 / (F_e/F_g) = {r20:.3f} (T5 R8)")
for b, f in ((1 / beta, r16), (1 / alpha, r20)):
    f = max(f, 1 / f)
    print(f"    base {b:6.2f}: within x{f:.2f} of some integer power by chance with p = {2 * math.log(f) / math.log(b):.2f}")

# ---- B7 Foit-Kleban ringdown test of the area quantum (Laghi et al. 2021) ----
# omega_0 = [alpha_A sqrt(1-a^2) + 16 pi a] / [16 pi (1 + sqrt(1-a^2))] / M   (arXiv:2011.03816 eq. 6)
# GR l=m=2,n=0: M omega = 1.5251 - 1.1568 (1-a)^0.1292 (Berti-Cardoso-Will 2006 fit); a=0 exact 0.373672
print("B7 area quantum vs ringdown")


def m_omega_220(a):
    return 0.373672 if a == 0 else 1.5251 - 1.1568 * (1 - a)**0.1292


def alpha_equiv(a):
    """alpha_A (times k+1) that makes the FK fundamental line sit on the GR 220 mode."""
    sq = math.sqrt(1 - a * a)
    return (16 * math.pi * (1 + sq) * m_omega_220(a) - 16 * math.pi * a) / sq


def m_omega_fk(alpha_A, a):
    sq = math.sqrt(1 - a * a)
    return (alpha_A * sq + 16 * math.pi * a) / (16 * math.pi * (1 + sq))


spins = [0.0] + list(np.linspace(0.01, 0.99, 99))
aeq = [alpha_equiv(a) for a in spins]
print(f"  alpha_equiv: a=0 {aeq[0]:.2f}, a=0.69 {alpha_equiv(0.69):.2f}, a=0.99 {alpha_equiv(0.99):.2f}, "
      f"max {max(aeq):.2f}")
for name, aA in (("0SM 8 pi^2", 8 * math.pi**2), ("Bekenstein 8 pi", 8 * math.pi), ("Hod 4 ln 3", 4 * math.log(3))):
    ratios = [m_omega_fk(aA, a) / m_omega_220(a) for a in spins]
    print(f"  {name:16s} alpha_A = {aA:6.2f}: omega_FK/omega_GR from {min(ratios):.2f} to {max(ratios):.2f} "
          f"(a=0.69: {m_omega_fk(aA, 0.69) / m_omega_220(0.69):.2f})")
check("(k+1) alpha_A <= 37.6 for every spin, so 8 pi^2 = 79 cannot sit on the 220 mode for any k >= 0",
      max(aeq) < 8 * math.pi**2 and abs(aeq[0] - 32 * math.pi * 0.373672) < 1e-9)
check("8 pi^2 lies above the LVK combined interval 15.6 (+20.5/-13.3)", 8 * math.pi**2 > 15.6 + 20.5)

print(f"\n{sum(ok for _, ok in results)}/{len(results)} checks OK")
