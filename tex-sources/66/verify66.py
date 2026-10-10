"""verify66.py -- numerical checks for Paper #66 of the 0-Sphere model series.

Every number quoted in the paper is recomputed here from measured inputs.
Run:  python3 verify66.py      (numpy and scipy required)
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

# ---- constants (CODATA 2022) -------------------------------------------
h = 6.62607015e-34; hbar = h/(2*np.pi); c = 299792458.0
me = 9.1093837139e-31; mec2_keV = 510.99895069
alpha = 1/137.035999177
lamC = h/(me*c)                       # Compton wavelength, m
G = 6.67430e-11; mp = 1.67262192595e-27; a0 = 5.29177210544e-11
e = 1.602176634e-19; eps0 = 8.8541878188e-12
u_keV = 931494.10372; me_u = 5.485799090441e-4

ok = True
def check(name, val, ref, rtol=2e-3):
    global ok
    good = abs(val-ref) <= rtol*abs(ref)
    ok &= good
    print(f"{'ok ' if good else 'BAD'} {name:46s} {val:.6g}  (paper {ref:.6g})")

# ---- 1. bridge equation and the internal clock (#10, #62, #65) ----------
def beta_of(a):
    gv = 1 + abs(a)/np.sqrt(2)
    return np.sqrt(1 - gv**-2)
a = {'electron':0.00115965218059, 'muon':0.00116592071,
     'proton':1.79284734463, 'neutron':1.91304276}
beta = {k: beta_of(v) for k,v in a.items()}
b = beta['electron']
check("beta_e", b, 0.0404720, 1e-6)
check("beta_e^2", b**2, 0.0016379809, 1e-7)
nuZB = b*c/lamC; nuC = c/lamC
check("nu_ZB = beta c / lambda_C  [Hz]", nuZB, 5.0007e18, 1e-4)
check("nu_C = c / lambda_C  [Hz]", nuC, 1.2356e20, 1e-4)
check("nu_C / nu_ZB = 1/beta", nuC/nuZB, 24.708, 1e-4)
check("T_tr = 1/nu_ZB  [s]", 1/nuZB, 1.9997e-19, 1e-4)
check("h nu_ZB  [keV]", h*nuZB/e/1e3, 20.681, 1e-4)
check("beta c  [km/s]", b*c/1e3, 12133, 1e-3)
for k in ['muon','proton','neutron']:
    print(f"    beta_{k:8s} = {beta[k]:.6f}   ratio to e = {beta[k]/b:.4f}   1/beta = {1/beta[k]:.4f}")
check("beta_p / beta_e", beta['proton']/b, 22.176, 1e-4)
check("beta_mu / beta_e", beta['muon']/b, 1.0027, 1e-4)

# ---- 2. Thomas vortex ---------------------------------------------------
pref = (b*c)**3/(4*hbar*c**3)
check("v^3/(4 hbar c^3)  [J^-1 s^-1]", pref, 1.5715e29, 1e-4)
th = np.linspace(0, 2*np.pi, 2_000_001)
cyc = np.trapezoid(np.abs(np.sin(2*th)), th) * b**2/4     # (beta^2 w/4) * (1/w) * int
check("cycle integral of |Omega_T| = beta^2  [rad]", cyc, 1.637981e-3, 1e-5)
check("#50 gap, continuum Thomas 2 pi a_e  [rad]", 2*np.pi*a['electron'], 7.29e-3, 1e-3)
check("#50 gap factor 1/(2 a_e)", 1/(2*a['electron']), 431.2, 1e-3)
check("#50 gap factor pi/beta^2", np.pi/b**2, 1918, 1e-3)

# ---- 3. hydrogen-like ions (point nucleus) -------------------------------
print("\n Z   gammaD    B(keV)   lam_eff/lamC  nu(1e18)  h nu(keV)")
ions = {}
for Z in [1, 26, 47, 79, 92]:
    gD = np.sqrt(1-(Z*alpha)**2)
    ions[Z] = gD
    print(f"{Z:3d} {gD:.6f} {mec2_keV*(1-gD):9.3f} {1/gD:10.6f} {nuZB*gD/1e18:9.4f} {h*nuZB*gD/e/1e3:9.3f}")
check("gammaD(92)", ions[92], 0.741135, 1e-6)
check("h nu_ZB at Z=92 [keV]", h*nuZB*ions[92]/e/1e3, 15.328, 1e-4)
check("kernel dilation at Z=92", 1/ions[92]-1, 0.3493, 1e-3)

# ---- 4. Dirac-Coulomb: <beta> = E/mc^2, admixture = B/2mc^2 -------------
def Edirac(n, kappa, Za):
    k = abs(kappa); g = np.sqrt(k*k - Za*Za)
    return 1/np.sqrt(1 + (Za/(n-k+g))**2)

def solve_state(n, kappa, Z, R=None):
    Za = Z*alpha
    gk = np.sqrt(kappa**2 - Za**2) if R is None else None
    def V(r):
        if R is not None and r < R:
            return -Za*(3 - (r/R)**2)/(2*R)
        return -Za/r
    def rhs(r, y, E):
        G_, F_, Ig, If = y
        v = V(r)
        return [-kappa/r*G_ + (E - v + 1)*F_, kappa/r*F_ - (E - v - 1)*G_, G_*G_, F_*F_]
    nr = n - abs(kappa)
    def shoot(E):
        lam = np.sqrt(1 - E*E)
        g = np.sqrt(kappa**2 - Za**2)
        rm = (nr + g + 1)/lam
        r0 = 1e-7/lam
        if R is None:
            y0 = [r0**g, r0**g*(kappa+g)/Za, 0, 0]
        else:   # regular finite-nucleus start
            l = kappa if kappa > 0 else -kappa-1
            if kappa < 0: y0 = [r0**(l+1), r0**(l+2)*(E - V(0) - 1)/(2*l+3), 0, 0]
            else:         y0 = [r0**(l+2)*(E - V(0) + 1)/(2*l+1), r0**(l+1), 0, 0]
        so = solve_ivp(rhs, [r0, rm], y0, args=(E,), rtol=1e-11, atol=1e-30, method='DOP853')
        rmax = rm + 50/lam
        yi = [1e-30, -1e-30*lam/(1+E), 0, 0]
        si = solve_ivp(rhs, [rmax, rm], yi, args=(E,), rtol=1e-11, atol=1e-60, method='DOP853')
        return so.y[:, -1], si.y[:, -1]
    def mismatch(E):
        o, i = shoot(E)
        return (o[0]*i[1] - i[0]*o[1])/np.hypot(o[0], o[1])/np.hypot(i[0], i[1])
    E0 = Edirac(n, kappa, Za)
    lo, hi = E0*(1-2e-3), min(E0*(1+2e-3), 0.999999999)
    E = brentq(mismatch, lo, hi, xtol=1e-15)
    o, i = shoot(E)
    s = (o[0]/i[0])**2
    Ig = o[2] - s*i[2]; If = o[3] - s*i[3]          # inward integral runs backwards
    N = Ig + If
    return E, (Ig - If)/N, If/N, E0

print("\n state   Z   E(shooting)        <beta>             |<b>-E|    int f^2     B/2mc^2")
for (lab, n, kap, Z) in [("1s1/2",1,-1,26),("2p3/2",2,-2,26),("1s1/2",1,-1,79),
                         ("2s1/2",2,-1,79),("1s1/2",1,-1,92),("2p1/2",2,1,92),("3d5/2",3,-3,92)]:
    E, bexp, f2, E0 = solve_state(n, kap, Z)
    print(f"{lab:6s} {Z:3d} {E:.13f} {bexp:.13f} {abs(bexp-E):.1e} {f2:.9f} {(1-E)/2:.9f}")
    ok &= abs(E-E0) < 1e-10 and abs(bexp-E) < 1e-9 and abs(f2-(1-E)/2) < 1e-9
Rf = 7.561/386.15926796
E, bexp, f2, E0 = solve_state(1, -1, 92, R=Rf)
print(f"finite nucleus Z=92: E={E:.7f}  <beta>={bexp:.7f}  int f^2={f2:.6f}  B/2mc^2={(1-E)/2:.6f}")
check("finite nucleus E", E, 0.7415241, 2e-6)
check("finite nucleus <beta>", bexp, 0.7420920, 2e-6)

# ---- 5. composition: Eotvos parameters ----------------------------------
mat = {'Be':(4,9.0121831),'Al':(13,26.9815384),'Ti':(22,47.867),'Cu':(29,63.546),
       'Pt':(78,195.084),'Pb':(82,207.2)}
xe = {k: Z*me_u/A for k,(Z,A) in mat.items()}
r = b/beta['proton']
def eta_species(A, B): return abs((xe[A]-xe[B])*(r-1))
check("x_e(Ti)", xe['Ti'], 2.521e-4, 1e-3); check("x_e(Pt)", xe['Pt'], 2.193e-4, 1e-3)
check("eta(Ti,Pt), species lever", eta_species('Ti','Pt'), 3.13e-5, 3e-3)
check("excess over MICROSCOPE 2.7e-15", eta_species('Ti','Pt')/2.7e-15, 1.16e10, 1e-2)
for p in [('Be','Ti'),('Be','Al'),('Cu','Pb'),('Al','Pt')]:
    print(f"    eta{p} species lever = {eta_species(*p):.3e}")
BA = {'Be9':(6462.668,9.012183065),'Al27':(8331.553,26.98153841),'Ti48':(8723.011,47.94794198),
      'Cu63':(8752.140,62.92959772),'Pt195':(7926.553,194.9647917),'Pb208':(7867.453,207.9766525),
      'U238':(7570.126,238.0507870)}
fB = {k: ba*round(m)/(m*u_keV) for k,(ba,m) in BA.items()}
check("f_B(Ti48)", fB['Ti48'], 9.375e-3, 2e-3); check("f_B(Pt195)", fB['Pt195'], 8.511e-3, 2e-3)
check("eta(Ti,Pt), E^2 lever", fB['Ti48']-fB['Pt195'], 8.64e-4, 3e-3)
check("eta(Be,U), E^2 lever", fB['U238']-fB['Be9'], 1.20e-3, 1e-2)
for p in [('Be9','Ti48'),('Be9','Al27'),('Cu63','Pb208'),('Al27','Pt195')]:
    print(f"    eta{p} E^2 lever = {abs(fB[p[0]]-fB[p[1]]):.3e}")
dH = 13.598434/ (u_keV*1e3)
check("H atom: doubled defect [u]", dH, 1.46e-8, 1e-2)
print(f"    vs AME2020 uncertainty 1.4e-11 u: {dH/1.4e-11:.0f} sigma")
gD = ions[92]
check("E^2 reading shortfall at Z=92 [keV]", mec2_keV*gD*(1-gD), 98.0, 1e-3)
check("E^3 reading shortfall at Z=92 [keV]", mec2_keV*gD*(1-gD**2), 170.7, 1e-3)

# ---- 6. local position invariance (#62 vs #63) --------------------------
dPhi = 2*0.0167086*1.32712440018e20/(1.495978707e11*c**2)
check("annual dPhi/c^2", dPhi, 3.299e-10, 2e-3)
check("Reading B annual modulation of g/2", a['electron']*2*dPhi, 7.65e-13, 2e-3)
print(f"    ratio to 1.3e-13: {a['electron']*2*dPhi/1.3e-13:.1f}")

# ---- 7. corrections C1 ---------------------------------------------------
Fc = e**2/(4*np.pi*eps0*a0**2)
check("C1 Coulomb force at a0 [N]", Fc, 8.24e-8, 2e-3)
check("C1 ratio to m_e g", Fc/(me*9.80665), 9.22e21, 2e-3)
check("C1 G m_p / a0^2", G*mp/a0**2, 3.99e-17, 2e-3)
check("C1 ratio e^2/(4 pi eps0 G me mp)", e**2/(4*np.pi*eps0*G*me*mp), 2.27e39, 2e-3)
check("C1 2 pi nu_ZB [rad/s]", 2*np.pi*nuZB, 3.142e19, 1e-3)
check("C1 2 pi nu_C  [rad/s]", 2*np.pi*nuC, 7.763e20, 1e-3)

# ---- 8. Part I: the guide to Paper #65 -----------------------------------
th = np.array([0, np.pi/2, 2*np.pi/3, np.pi])
nA = np.cos(th/2)**2; TA = nA**2; TB = (1-nA)**2; K = 0.5*np.sin(th)**2
ok &= np.allclose(TA+TB+K, 1); ok &= np.allclose([TA[2],TB[2],K[2]], [1/16, 9/16, 3/8])
print("ok  energy split at four moments, rows sum to one" if np.allclose(TA+TB+K,1) else "BAD energy split")
t = np.linspace(0, 2*np.pi, 200001)
for p, q, ref in [(1,1,1), (1,3,-1), (2,3,0), (3,5,1)]:
    z = np.cos(p*t) + 1j*np.sin(q*t)
    W = np.sum(np.diff(np.unwrap(np.angle(z))))/(2*np.pi)
    check(f"winding of cos({p}t)+i sin({q}t)", round(W)+1e-12 if ref==0 else W, ref if ref!=0 else 1e-12, 1e-6)
lamZB = lamC/(4*np.pi)
check("lambda_ZB = lambda_C/4pi  [m]", lamZB, 1.931e-13, 1e-3)
check("beta c / (lambda_C/2pi)  [Hz]", b*c/(lamC/(2*np.pi)), 3.142e19, 1e-3)
check("beta c / lambda_ZB  [Hz]", b*c/lamZB, 6.284e19, 1e-3)
check("h nu with lambda_ZB  [keV]", h*b*c/lamZB/e/1e3, 260, 2e-3)
check("hydrogen n=1->2 [eV]", 13.598434*(1-1/4), 10.2, 3e-3)
f_rev = c/1436.0
check("storage ring revolution, 1436 m  [kHz]", f_rev/1e3, 208.8, 1e-3)
check("storage ring level spacing h f  [eV]", h*f_rev/e, 8.6e-10, 1e-2)
check("Dirac beat 2 mc^2/h  [Hz]", 2*nuC, 2.4712e20, 1e-4)

print("\nall checks passed" if ok else "\nSOME CHECKS FAILED")
