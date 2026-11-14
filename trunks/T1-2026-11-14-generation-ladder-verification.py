"""
T1.32 (2026-11-14) generation ladder: reproduction script.

Wall-practice session of 2026-11-14 (author: Satoshi Hanamura; Claude Opus 5.5).
Every number quoted in T1.32, K13 and K20-K23 of trunk T1 (2026-11-14) is
recomputed here. Run:  python3 T1-2026-11-14-generation-ladder-verification.py

G1  Koide's relation from measured lepton masses, and its phase (~2/9 rad)
G2  0SM kernel energy T_A sampled at three phases 120 deg apart:
    the equipartition condition cos(3 delta) = 1/8 gives Q = 2/3 exactly,
    but the mass ratios come out 1 : 1438 : 21584 (observed 1 : 207 : 3477)
G3  Naive samplings (m or sqrt(m) proportional to T_A, occupation, photon term)
G4  Winding number with a harmonic added to kernel A (closed form vs numeric)
G5  Selection rules in the amplitude layer (spinor antiperiodicity, parity,
    continuity of the charge sign)
G6  Occupation-layer spectrum and DC excess 1 + k^2/2 for the 3phi and 5phi ladders
G7  Amplitudes needed for the masses under several energy counts
G8  Model II: Larmor power of a unit charge carried by an oscillating kernel
G9  External gates: m^5 lifetime law, beat period vs lifetime, a_mu - a_e
G10 Channeling resonance energies (gamma = nu d / c, d = 3.84 Angstrom)
G11 Drag-corrected value of the morning (not adopted): beta (1 - beta^2)
G12 Quadrupole-type rate Gamma = C alpha w (w R)^4 fitted to the muon lifetime: length R
G13 Same-day revision: harmonic amplitudes follow the radiation gradient (envelope).
    Envelope x carrier as a fixed Fourier combination; winding protected for any K;
    DC excess, K needed for mu and tau, and leakage into the fundamental
G14 K20 formulations F1-F5: exact identity+gradient (F1), Hill/Mathieu (F3),
    quartic + lock (F4), quartic + cos-theta potential (F5); exponent the data require
"""
import numpy as np
import sympy as sp

OK = []


def check(label, cond):
    OK.append((label, bool(cond)))
    print(f"[{'OK' if cond else 'NG'}] {label}")


# ---------------------------------------------------------------- constants
me, mmu, mtau = 0.51099895, 105.6583755, 1776.86          # MeV (PDG)
a_e, a_mu = 0.00115965218059, 0.00116592059               # anomalies
tau_mu, tau_tau, br_tau_e = 2.1969811e-6, 290.3e-15, 0.1782
hbar_MeVs = 6.582119569e-22
h = 6.62607015e-34; c = 299792458.0; me_kg = 9.1093837015e-31
e = 1.602176634e-19; eps0 = 8.8541878128e-12; lamC = 2.42631023867e-12

g_e = 1 + a_e / np.sqrt(2)
beta2 = 1 - 1 / g_e**2
beta = np.sqrt(beta2)

# ---------------------------------------------------------------- G1 Koide
m = np.array([me, mmu, mtau]); s = np.sqrt(m)
Q = m.sum() / s.sum()**2
print(f"G1 Koide Q = {Q:.10f}  (2/3 = {2/3:.10f}, diff {Q-2/3:.2e})")
check("G1 Koide Q within 1e-5 of 2/3", abs(Q - 2/3) < 1e-5)
A = s.sum() / 3
cosv = (s / A - 1) / np.sqrt(2)
deltas = np.arccos(np.clip(cosv, -1, 1))
# reduce to the conventional delta in (0, 2pi/3)
d_conv = min([(x % (2*np.pi/3)) for x in deltas] + [((-x) % (2*np.pi/3)) for x in deltas],
             key=lambda v: abs(v - 2/9))
print(f"G1 Koide phase (mod 2pi/3) = {d_conv:.5f} rad  (2/9 = {2/9:.5f})")
check("G1 Koide phase near 2/9 rad (1e-3)", abs(d_conv - 2/9) < 1e-3)

# ---------------------------------------------------------------- G2 equipartition
TA = lambda t: 3/8 + 0.5*np.cos(t) + np.cos(2*t)/8
d0 = np.arccos(1/8) / 3
v = TA(d0 + 2*np.pi*np.arange(3)/3)
mm = np.sort(v**2)
Q2 = mm.sum() / np.sqrt(mm).sum()**2
print(f"G2 sqrt(m) ~ T_A, cos3d = 1/8: Q = {Q2:.12f}, ratios {mm/mm[0]}")
check("G2 Q = 2/3 exactly", abs(Q2 - 2/3) < 1e-12)
check("G2 ratios 1:1438:21584 (wrong by ~7)", abs(mm[1]/mm[0] - 1437.86) < 1 and abs(mm[2]/mm[0] - 21584) < 5)
# symbolic: r_eff^2 / a^2 = (17 + 8 cos 3d)/9
dd = sp.symbols('d', real=True)
k = sp.symbols('k', real=True)
samples = [sp.Rational(3, 8) + sp.cos(dd + 2*sp.pi*j/3)/2 + sp.cos(2*dd + 4*sp.pi*j/3)/8 for j in range(3)]
Qsym = sp.simplify(sum(x**2 for x in samples) / sum(samples)**2)
check("G2 symbolic Q = (1 + (17+8cos3d)/18)/3", sp.simplify(Qsym - (1 + (17 + 8*sp.cos(3*dd))/18)/3) == 0)

# ---------------------------------------------------------------- G3 naive forms
forms = {'T_A': lambda t: np.cos(t/2)**4, 'occ': lambda t: np.cos(t/2)**2,
         'photon': lambda t: 0.5*np.sin(t)**2}
grid = np.linspace(0, 2*np.pi, 200001)
for name, f in forms.items():
    for p, lab in [(1, 'm'), (2, 'sqrt m')]:
        best = (1e9, None)
        for d in grid:
            vv = np.sort(f(d + 2*np.pi*np.arange(3)/3)**p)
            if vv[0] <= 0:
                continue
            err = abs(np.log(vv[1]/vv[0]/(mmu/me)))
            if err < best[0]:
                best = (err, d)
        vv = np.sort(f(best[1] + 2*np.pi*np.arange(3)/3)**p)
        print(f"G3 {lab} ~ {name}: fit mu/e -> tau/e {vv[2]/vv[0]:9.1f} (obs {mtau/me:.1f}), Q={vv.sum()/np.sqrt(vv).sum()**2:.4f}")

# ---------------------------------------------------------------- G4 winding
phi = np.linspace(0, 2*np.pi, 400001)


def W_num(mh, kk, psi):
    a = np.cos(phi) + kk*np.cos(mh*phi + psi); b = np.sin(phi)
    ang = np.unwrap(np.arctan2(b, a))
    return int(round((ang[-1] - ang[0]) / (2*np.pi)))


def W_closed(mh, kk, psi):
    cc = np.cos(psi); a0 = 1 + kk*cc; ap = -1 + ((-1)**mh)*kk*cc
    if abs(a0) < 1e-12 or abs(ap) < 1e-12:
        return None
    if a0*ap < 0:
        return 1 if a0 > 0 else -1
    return 0


bad = 0
for mh in [2, 3, 4, 5]:
    for kk in [0.3, 0.9, 1.5, 7.17, 20.3, 207]:
        for psi in np.linspace(0.013, 2*np.pi, 37):
            wc = W_closed(mh, kk, psi)
            if wc is not None and wc != W_num(mh, kk, psi):
                bad += 1
check("G4 closed-form winding = numeric winding (all cases)", bad == 0)
for kk in [7.17, 14.3, 207]:
    print(f"G4 even harmonic k={kk}: charge kept iff |cos psi| < 1/k, window +/-{np.degrees(np.arcsin(1/kk)):.2f} deg")

# ---------------------------------------------------------------- G5 selection rules
p_, psi_ = sp.symbols('phi psi', real=True)
anti = {mh: sp.simplify(sp.expand_trig(sp.cos(mh*(p_+sp.pi)+psi_) + sp.cos(mh*p_+psi_))) == 0 for mh in range(1, 7)}
print("G5 spinor antiperiodicity f(phi+pi) = -f(phi):", anti)
check("G5 only odd harmonics are antiperiodic", all(anti[mh] == (mh % 2 == 1) for mh in anti))
par = sp.simplify(sp.cos(-3*p_+psi_) - sp.cos(3*p_+psi_))
check("G5 parity of kernel A forces psi in {0, pi}", par.subs(psi_, 0) == 0 and sp.simplify(par.subs(psi_, sp.pi)) == 0)
check("G5 psi = 0: W = +1 for every k >= 0", all(W_closed(3, kk, 0.0) == 1 and W_closed(5, kk, 0.0) == 1 for kk in [0, 0.5, 1, 7, 207]))
check("G5 psi = pi: W flips to -1 once k > 1", W_closed(3, 2.0, np.pi) == -1 and W_closed(3, 0.5, np.pi) == 1)

# ---------------------------------------------------------------- G6 occupation spectrum
for n, lab in [(3, 'mu (3phi)'), (5, 'tau (5phi)')]:
    a = sp.cos(p_) + k*sp.cos(n*p_)
    co = {}
    for j in range(0, n+1):
        val = sp.simplify(sp.integrate(sp.expand(a**2)*sp.cos(2*j*p_), (p_, 0, 2*sp.pi)) / (sp.pi if j else 2*sp.pi))
        if val != 0:
            co[f"{j}theta"] = val
    dc = sp.simplify(sp.integrate(sp.expand(a**2 + sp.sin(p_)**2), (p_, 0, 2*sp.pi)) / (2*sp.pi))
    print(f"G6 {lab}: occupation a^2 = {co};  DC(a^2+b^2) = {dc}")
    check(f"G6 {lab} DC excess = 1 + k^2/2", sp.simplify(dc - (1 + k**2/2)) == 0)

# ---------------------------------------------------------------- G7 amplitudes needed
for lab, ratio, n in [('mu', mmu/me, 3), ('tau', mtau/me, 5)]:
    print(f"G7 {lab}: E~1+k^2/2 -> k={np.sqrt(2*(ratio-1)):.2f};  E~1+n^2k^2 (n=2,3) -> k={np.sqrt((ratio-1))/(2 if lab=='mu' else 3):.2f};"
          f"  E~1+k^2 -> k={np.sqrt(ratio-1):.2f};  E~1+k -> k={ratio-1:.1f}")

# ---------------------------------------------------------------- G8 Model II radiation
w = 2*np.pi*beta*me_kg*c**2/h
x = lamC/4
P = e**2*(w**2*x)**2/(6*np.pi*eps0*c**3)/2
print(f"G8 Model II: nu_ZB = {w/2/np.pi:.4e} Hz, Larmor (time avg) = {P:.3g} W, rest energy lost in {me_kg*c**2/P:.2g} s")
check("G8 Larmor ~ 1 W, lifetime ~ 1e-13 s", 0.5 < P < 2 and me_kg*c**2/P < 1e-12)

# ---------------------------------------------------------------- G9 external gates
r_obs = tau_mu/tau_tau
r_m5 = (mtau/mmu)**5/br_tau_e
print(f"G9 tau_mu/tau_tau = {r_obs:.4e}; (m_tau/m_mu)^5/BR = {r_m5:.4e}; ratio {r_obs/r_m5:.4f}")
check("G9 m^5 law holds within 1%", abs(r_obs/r_m5 - 1) < 0.01)
beat = hbar_MeVs/(mmu - me)
print(f"G9 beat hbar/(m_mu-m_e)c^2 = {beat:.3e} s; tau_mu/beat = {tau_mu/beat:.2e}")
check("G9 beat is 3.5e17 shorter than the muon lifetime", 3e17 < tau_mu/beat < 4e17)
print(f"G9 a_mu - a_e = {a_mu-a_e:.3e} ({(a_mu/a_e-1)*100:.3f} %); beta_mu/beta_e = {np.sqrt(1-1/(1+a_mu/np.sqrt(2))**2)/beta:.5f}")

# ---------------------------------------------------------------- G10 channeling
d = 3.84e-10
nu_e = beta*me_kg*c**2/h
rows = [('Compton mc^2/h (e)', me_kg*c**2/h, me), ('Dirac ZB 2mc^2/h (e)', 2*me_kg*c**2/h, me),
        ('0SM fundamental (e)', nu_e, me), ('0SM fundamental (mu, ladder)', nu_e, mmu),
        ('0SM 2x (mu, ladder)', 2*nu_e, mmu), ('0SM lock at omega_mu (mu)', nu_e*mmu/me, mmu)]
for lab, nu, mass in rows:
    g = nu*d/c
    print(f"G10 {lab:30s} nu={nu:.4e} Hz gamma={g:8.2f} E={g*mass:10.2f} MeV")
check("G10 Compton resonance reproduces 80.87 MeV", abs((me_kg*c**2/h)*d/c*me - 80.874) < 0.05)

# ---------------------------------------------------------------- G11 drag value
print(f"G11 beta = {beta:.8f}, 1-beta^2 = {1-beta2:.8f}, beta(1-beta^2) = {beta*(1-beta2):.7f}, beta/gamma = {beta/g_e:.7f}")

# ---------------------------------------------------------------- G12 quadrupole length
GF = 1.1663787e-5; alpha = 1/137.035999; hbarc_fm = 0.1973269804; mmu_GeV = mmu/1000
Gam = GF**2*mmu_GeV**5/(192*np.pi**3)
print(f"G12 Fermi rate gives tau_mu = {6.582119569e-25/Gam:.4e} s")
check("G12 Fermi formula reproduces tau_mu within 1%", abs(6.582119569e-25/Gam/tau_mu - 1) < 0.01)
for C in [1, 0.1, 0.01]:
    R = (GF**2/(192*np.pi**3*C*alpha))**0.25*hbarc_fm*1e-15
    print(f"G12 C={C}: R = {R:.2e} m  (reduced Compton / R = {3.8615926796e-13/R:.3g}; 1/M_W = {hbarc_fm/80.38*1e-15:.2e} m)")
print(f"G12 power of beta needed (C=1): {np.log(3.8615926796e-13/((GF**2/(192*np.pi**3*alpha))**0.25*hbarc_fm*1e-15))/np.log(1/beta):.2f}")

# ---------------------------------------------------------------- G13 envelope
envs = {'photon 1/2 sin^2 theta': lambda x: 0.5*np.sin(2*x)**2, 'gradient sin theta': lambda x: np.sin(2*x)}
allone = True
for name, env in envs.items():
    for mh in [3, 5]:
        for KK in [0.5, 2, 20, 207, 3000]:
            for psi in np.linspace(0, 2*np.pi, 25)[:-1]:
                a = np.cos(phi) + KK*env(phi)*np.cos(mh*phi + psi); b = np.sin(phi)
                if np.min(np.hypot(a, b)) < 1e-9:
                    allone = False; continue
                ang = np.unwrap(np.arctan2(b, a))
                if int(round((ang[-1]-ang[0])/(2*np.pi))) != 1:
                    allone = False
check("G13 envelope: winding = +1 for all K <= 3000, all phases (3phi, 5phi, both envelopes)", allone)
const = set()
for psi in np.linspace(0, 2*np.pi, 25)[:-1]:
    a = np.cos(phi) + 20*np.cos(3*phi + psi); b = np.sin(phi)
    ang = np.unwrap(np.arctan2(b, a)); const.add(int(round((ang[-1]-ang[0])/(2*np.pi))))
print(f"G13 constant amplitude K=20, 3phi: windings {const}")
check("G13 constant amplitude does not protect the sign", -1 in const)
KK_ = sp.symbols('K', real=True)
for lab, env, car in [('1/2 sin^2(2phi) cos3phi', sp.sin(2*p_)**2/2, sp.cos(3*p_)), ('sin(2phi) sin3phi', sp.sin(2*p_), sp.sin(3*p_))]:
    co = {n: sp.simplify(sp.integrate(env*car*sp.cos(n*p_), (p_, 0, 2*sp.pi))/sp.pi) for n in range(0, 9)}
    co = {f"{n}phi": v for n, v in co.items() if v != 0}
    a = sp.cos(p_) + KK_*env*car
    dc = sp.expand(sp.simplify(sp.integrate(sp.expand(a**2 + sp.sin(p_)**2), (p_, 0, 2*sp.pi))/(2*sp.pi)))
    print(f"G13 {lab} = {co};  DC(a^2+b^2) = {dc}")
    for nm, ratio in [('mu', mmu/me), ('tau', mtau/me)]:
        sols = [float(x) for x in sp.solve(sp.Eq(dc, ratio), KK_) if float(x) > 0]
        leak = co.get('1phi', 0)*sols[0]
        print(f"      {nm}: K = {sols[0]:.1f}, leak into fundamental = {float(leak):+.1f}")
check("G13 photon envelope = -1/8 cos phi + 1/4 cos 3phi - 1/8 cos 7phi (max residual < 1e-14)",
      np.max(np.abs(0.5*np.sin(2*phi)**2*np.cos(3*phi) - (-np.cos(phi)/8 + np.cos(3*phi)/4 - np.cos(7*phi)/8))) < 1e-14)

# ---------------------------------------------------------------- G14 K20 formulations
th_, M_, c_, s_ = sp.symbols('theta M c s', real=True)
S_ = sp.sqrt(M_); D_ = (-s_*sp.cos(th_) + c_)/S_
amin = sp.simplify(((S_ - D_)/2).subs(th_, sp.pi)); bmin = sp.simplify(((S_ + D_)/2).subs(th_, 0))
sol = sp.solve([sp.Eq(amin, 0), sp.Eq(bmin, 0)], [c_, M_], dict=True)
print("G14 F1 exact identity + exact gradient, both amplitudes vanish only for:", sol)
check("G14 F1: only M = s, c = 0 (electron shape, scale free)", sol == [{M_: s_, c_: 0}])
# F3 Hill/Mathieu: q = 0 limit gives cos phi, cos 3phi, cos 5phi with lambda 1, 9, 25
msF = np.arange(1, 120, 2)
def hill(q, step):
    Hm = np.diag(msF.astype(float)**2); idx = {m: i for i, m in enumerate(msF)}
    for i, m in enumerate(msF):
        for mm in (m+step, abs(m-step)):
            if mm in idx: Hm[idx[mm], i] += q
    return np.linalg.eigh((Hm + Hm.T)/2)
w0, _ = hill(0.0, 2)
check("G14 F3: q=0 eigenvalues 1, 9, 25 (ce_1, ce_3, ce_5 = cos phi, cos 3phi, cos 5phi)", np.allclose(w0[:3], [1, 9, 25]))
# F4/F5: a'' = -(alpha - 2q cos 2phi) a - a^3, even, a(pi/2) = 0, levels n = 0,1,2 ; mass = <H>
def integ(A, alpha, q, nsteps=3000):
    A = np.atleast_1d(A).astype(float); a = A.copy(); v = np.zeros_like(a); hstep = (np.pi/2)/nsteps
    zc = np.zeros_like(a, dtype=int); Hs = np.zeros_like(a); pp = 0.0; prev = a.copy()
    acc = lambda p, x: -(alpha - 2*q*np.cos(2*p))*x - x**3
    Hf = lambda p, x, y: 0.5*y**2 + 0.5*(alpha - 2*q*np.cos(2*p))*x**2 + 0.25*x**4
    for i in range(nsteps):
        Hs += Hf(pp, a, v)*(0.5 if i == 0 else 1.0)
        k1a = v; k1v = acc(pp, a); k2a = v + hstep/2*k1v; k2v = acc(pp + hstep/2, a + hstep/2*k1a)
        k3a = v + hstep/2*k2v; k3v = acc(pp + hstep/2, a + hstep/2*k2a); k4a = v + hstep*k3v; k4v = acc(pp + hstep, a + hstep*k3a)
        a = a + hstep/6*(k1a + 2*k2a + 2*k3a + k4a); v = v + hstep/6*(k1v + 2*k2v + 2*k3v + k4v); pp += hstep
        if i < nsteps - 1: zc += (np.sign(a) != np.sign(prev)).astype(int)
        prev = a
    Hs += 0.5*Hf(pp, a, v)
    return a, zc, Hs*hstep/(np.pi/2)
def lev(alpha, q):
    Ag = np.concatenate([np.linspace(1e-3, 2, 150), np.linspace(2.01, 30, 260)])
    f, _, _ = integ(Ag, alpha, q)
    idx = np.where(np.sign(f[:-1]) != np.sign(f[1:]))[0]
    lo = Ag[idx].copy(); hi = Ag[idx+1].copy(); flo = f[idx].copy()
    for _ in range(40):
        mid = (lo + hi)/2; fm, _, _ = integ(mid, alpha, q)
        sm = np.sign(fm) == np.sign(flo); lo = np.where(sm, mid, lo); flo = np.where(sm, fm, flo); hi = np.where(sm, hi, mid)
    _, z, Hm = integ((lo + hi)/2, alpha, q, nsteps=6000)
    out = {}
    for zz, hm in zip(z, Hm):
        out.setdefault(int(zz), hm)
    return np.array([out[n] for n in range(3)])
for al, qq in [(0.0, 0.0), (0.7, 0.0), (0.25, -0.5), (-1.0, -1.5), (1.25, 0.5)]:
    E = lev(al, qq)
    print(f"G14 F4/F5 alpha={al:5.2f} q={qq:5.2f}: mu/e={E[1]/E[0]:8.2f} tau/e={E[2]/E[0]:9.2f} tau/mu={E[2]/E[1]:5.2f}")
E0 = lev(0.0, 0.0)
check("G14 F4 pure quartic: 81 and 625 (= 3^4, 5^4)", abs(E0[1]/E0[0] - 81) < 0.5 and abs(E0[2]/E0[0] - 625) < 3)
check("G14 F5: tau/mu stays near (5/3)^4 = 7.72 (observed 16.82)", 7 < lev(0.25, -0.5)[2]/lev(0.25, -0.5)[1] < 9)
for lab, kk in [('e->mu', np.log(mmu/me)/np.log(3)), ('mu->tau', np.log(mtau/mmu)/np.log(5/3))]:
    print(f"G14 data: E ~ omega^k needs k = {kk:.3f} ({lab}); pure power V ~ |a|^2p needs p = {kk/(kk-2):.3f}")

print()
print(f"{sum(o for _, o in OK)}/{len(OK)} checks OK")
