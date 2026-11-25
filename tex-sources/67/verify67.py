import math
# CODATA 2022
c = 299792458.0; h = 6.62607015e-34; hbar = h/(2*math.pi)
me = 9.1093837139e-31; eV = 1.602176634e-19
e2 = 2.307077e-28            # e^2/(4 pi eps0) in J m
beta2 = 0.00163798087        # Paper #10
beta = math.sqrt(beta2); n = 1/beta
lamC = h/(me*c); mc2 = me*c**2
nuC = mc2/h; nuZB = beta*nuC; nuD = 2*nuC
print(f"beta = {beta:.6f}, n = 1/beta = {n:.3f}, 2/beta = {2/beta:.2f}")
print(f"lambda_C = {lamC:.5e} m, nu_C = {nuC:.4e} Hz, nu_ZB = {nuZB:.4e} Hz, nu_D = {nuD:.4e} Hz")
print(f"line energies: {beta*mc2/eV/1e3:.2f} keV and {2*beta*mc2/eV/1e3:.2f} keV")
# wavelengths and momenta
g = 1/math.sqrt(1-beta2)
lam_dB = h/(g*me*beta*c); KE = (g-1)*mc2/eV
print(f"de Broglie wavelength at v_ZB = {lam_dB*1e12:.2f} pm, kinetic energy = {KE:.1f} eV")
print(f"vacuum wavelength of nu_ZB line = {c/nuZB*1e12:.2f} pm")
print(f"medium wavelength (c/n)/nu_ZB = {c/n/nuZB:.5e} m  (lambda_C = {lamC:.5e})")
print(f"waves per round trip: carrier {lamC/(c/n/nuZB):.4f}, de Broglie {lamC/lam_dB:.4f}")
# phase indices
print(f"phase index (rest energy kept) = {beta:.4f}; (rest energy removed) = {2/beta:.2f}; group = {n:.2f}")
# diffusivity
print(f"hbar/2m = {hbar/(2*me):.4e} m^2/s ; (lambda_C/2)(c/2pi) = {lamC/2*c/(2*math.pi):.4e}")
# packet doubling
T = math.sqrt(3)*me*lamC**2/hbar
print(f"doubling time at a = lambda_C: {T:.3e} s ; T*nu_ZB = {T*nuZB:.4f} ; 2pi sqrt3 beta = {2*math.pi*math.sqrt(3)*beta:.4f}")
print(f"Yukawa check a=1e-10 m: {math.sqrt(3)*me*1e-20/hbar:.2e} s")
# ray-limit ratio
print(f"ray-limit ratio 2pi L/lambda: carrier {2*math.pi:.3f}, de Broglie {2*math.pi*beta:.3f}")
# dipole radiation at nu_ZB
w = 2*math.pi*nuZB
# |r| in (4/3)e^2 w^4 |r|^2/c^3 is a matrix element = half the classical amplitude x0
for x0 in (lamC/4, lamC/2):
    P = 4/3*e2*w**4*(x0/2)**2/c**3
    print(f"classical amplitude x0 = {x0:.3e} m: P = {P:.2f} W, rest energy lost in {mc2/P:.2e} s")
# closure: dispersive carrier of mass m_e/(gamma beta) at v_ZB has wavelength lambda_C
M = me/(g*beta); print(f"carrier mass m_e/(gamma beta) = {M/me:.2f} m_e, wavelength/lambda_C = {h/(g*M*beta*c)/lamC:.6f}")
print(f"de Broglie waves per round trip gamma*beta = {g*beta:.6f}; proper-time deficit 1-1/gamma = {1-1/g:.2e}")
print(f"doubling: T nu_ZB = 0.44 (a/lamC)^2 -> 1/2 at a = {math.sqrt(0.5/(2*math.pi*math.sqrt(3)*beta)):.3f} lamC, 1 at a = {math.sqrt(1/(2*math.pi*math.sqrt(3)*beta)):.3f} lamC")
# Fourier components of cos^4(theta/2) and of the detuned product
import cmath
N=4096; ts=[2*math.pi*k/N for k in range(N)]
def comp(f,m): return abs(sum(f(t)*cmath.exp(-1j*m*t) for t in ts))/N*(1 if m==0 else 2)
print("cos^4(th/2) components 0,1,2:", [round(comp(lambda t: math.cos(t/2)**4, m),4) for m in (0,1,2)])
wA,wB=5,3  # integer rates on the grid
print("detuned product at 0,|dA-B|,wB,wA,wA+wB:", [round(comp(lambda t: math.cos(wA*t/2)**2*math.cos(wB*t/2)**2, m),4) for m in (0,wA-wB,wB,wA,wA+wB)])
# Rayleigh suppression at 2.33 eV
print(f"Rayleigh factor at 2.33 eV: {(2.33/(beta*mc2/eV))**4:.2e}")
# correspondence-principle intensity ratio of the two lines (formal)
print(f"formal intensity ratio |c2/c1|^2 * 2^4 = {((1/8)/(1/2))**2*16:.3f}")
