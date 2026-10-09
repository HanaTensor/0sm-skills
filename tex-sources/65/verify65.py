"""verify65.py — numerical checks for Paper #65 of the 0-Sphere model
"From Zero and One to the Electron" (S. Hanamura).
Seven independent checks; see Appendix A and Fig. "Map of the numerical checks".
Requires numpy. Expected output: beta=0.0404720  nu_tr=5.00068e+18 Hz / all checks passed
"""

# ---- Setup ----
import numpy as np, math
sx=np.array([[0,1],[1,0]]); sy=np.array([[0,-1j],[1j,0]]); sz=np.array([[1,0],[0,-1]])
w=1.0; E0=1.0
chi=lambda t: np.array([np.cos(w*t/2), np.sin(w*t/2)], dtype=complex)

# ---- Check 1: two solution sets ----
x=np.linspace(0,1,100001)
for p in [1.5,2,3]:
    f=x**p+(1-x)**p
    assert np.all(f[1:-1]<1) and f[0]==1 and f[-1]==1
assert sorted(np.round(np.roots([1,-3,2,0]).real,12))==[0,1,2]

# ---- Check 2: first-order equation ----
dt=1e-6
for t in np.linspace(0.1,5,7):
    d=(chi(t+dt)-chi(t-dt))/(2*dt)
    assert np.max(np.abs(1j*d-(w/2)*sy@chi(t)))<1e-6
assert np.allclose(np.linalg.eigvalsh((w/2)*sy),[-0.5,0.5])

# ---- Check 3: two Dirac branches ----
vals,V=np.linalg.eigh((w/2)*sy)
for t in np.linspace(0,2*np.pi,9):
    c=V.conj().T@chi(t)
    assert np.allclose(np.abs(c)**2,[0.5,0.5])
    assert abs((chi(t).conj()@((w/2)*sy)@chi(t)).real)<1e-12
    a=c[0]*V[:,0]; b=c[1]*V[:,1]
    assert abs(abs(a[0])**2+abs(b[0])**2-0.5)<1e-12
    assert abs(2*(a[0]*b[0].conjugate()).real-0.5*np.cos(w*t))<1e-12

# ---- Check 4: quartic as a pullback ----
for t in np.linspace(0,2*np.pi,50):
    c=chi(t); Sx=(c.conj()@sx@c).real; Sz=(c.conj()@sz@c).real
    assert abs(E0*np.cos(w*t/2)**4-E0*((1+Sz)/2)**2)<1e-12
    assert abs(0.5*E0*np.sin(w*t)**2-0.5*E0*Sx**2)<1e-12
    KE=0.5*E0*Sx**2; s=E0-KE; d=-E0*Sz
    assert abs((s-d)/2-E0*np.cos(w*t/2)**4)<1e-12

# ---- Check 5: Wronskian charge ----
t=np.linspace(0,10,1001); a=np.cos(w*t/2); b=np.sin(w*t/2)
ad=-(w/2)*np.sin(w*t/2); bd=(w/2)*np.cos(w*t/2)
assert np.allclose((2/w)*(a*bd-b*ad),1)
assert np.allclose((2/w)*(a*(-bd)-(-b)*ad),-1)
nA=a**2; nB=b**2; nd=2*a*ad
assert np.allclose(np.abs(nd), w*np.sqrt(nA*nB))

# ---- Check 6: winding of detuned pairs ----
def chi4(n): return 0 if n%2==0 else (1 if n%4==1 else -1)
def W(p,q): return 0.5*sum((-1)**k*math.copysign(1,
    math.sin(math.pi*q*(2*k+1)/(2*p))) for k in range(2*p))
for p in range(1,40,2):
    for q in range(1,40,2):
        if math.gcd(p,q)==1: assert W(p,q)==chi4(q)

# ---- Check 7: beta, two clocks, distance ----
ae=0.00115965218059
beta=math.sqrt(1-1/(1+ae/math.sqrt(2))**2)
h=6.62607015e-34; c=299792458; me=9.1093837015e-31
lamC=h/(me*c); nu_branch=me*c**2/h; nu_tr=beta*c/lamC
assert abs(beta-0.0404720)<1e-7
assert abs(nu_tr/nu_branch-beta)<1e-15
assert abs(beta*c/nu_tr-lamC)<1e-25
print(f"beta={beta:.7f}  nu_tr={nu_tr:.5e} Hz")
print("all checks passed")
