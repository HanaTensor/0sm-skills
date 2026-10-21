import math
import numpy as np
from scipy.integrate import quad
G=6.674e-11; c=2.998e8; h=6.626e-34; me=9.109e-31
lam=h/(me*c); R=lam/2; m=me
E=m*c**2
nu=5.0e18; w=2*math.pi*nu
# 1) corpus check: single-harmonic power P=(G/5c^5)(Q w^3)^2 with Q=1/2 m lam^2
Qc=0.5*m*lam**2
P1=G/(5*c**5)*(Qc*w**3)**2
print("lambda_C",lam,"Q_corpus",Qc)
print("P_single(nu=5e18)",P1,"  x2.6 =",2.6*P1,"  quoted 1.00e-43")
# 2) required effective Q for P_total=1.00e-43 (use single-harmonic normalisation at nu)
Ptot=1.00e-43
Qreq=math.sqrt(Ptot*5*c**5/G)/w**3
print("Q_req(eff)",Qreq,"ratio to Q_corpus",Qreq/Qc)
# 3) bubble: gamma = E/(8 pi R^2)
gamma=E/(8*math.pi*R**2)
print("gamma (N/m)",gamma)
# 4) area change of r=R(1+a P2) to O(a^2), numeric coefficient cA: dA/(4piR^2)=cA a^2
def P2(x): return 0.5*(3*x*x-1)
def dP2(x): return 3*x
def area_integrand(th,a):
    x=math.cos(th); eps=a*P2(x); dr=a*dP2(x)*(-math.sin(th))  # d/dtheta of P2(cos)
    r=1+eps; rth=dr
    return 2*math.pi*r*math.sqrt(r*r+rth*rth)*math.sin(th)
a=1e-3
A=quad(lambda t: area_integrand(t,a),0,math.pi,limit=200)[0]
cA=(A/(4*math.pi)-1)/a**2
print("cA (area coefficient, dA/4piR^2 = cA a^2)",cA)
# 5) quadrupole coefficient for solid-angle-uniform mass: Qzz = (4/15) m R^2 a
cQ=4/15
a_req=Qreq/(cQ*m*R**2)
print("a_req (deformation needed)",a_req)
# 6) energy fraction stored in membrane deformation: E_osc/E = cA*a^2/2
f=cA*a_req**2/2
print("required oscillation energy fraction f = E_osc/E:",f)
