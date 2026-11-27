"""verify67.py -- numbers of Paper #67 (spheroidal hose). Run: python3 verify67.py"""
import numpy as np
h=6.62607015e-34; hbar=h/(2*np.pi); c=299792458.0; e=1.602176634e-19
m=9.1093837139e-31; lamC=h/(m*c); lbar=lamC/(2*np.pi); muB=e*hbar/(2*m)
GM=3.986004418e14; RE=6.371e6; rGPS=2.6560e7
d=lamC/2; R=lbar
print("1  lambda_C = %.6e m, d = %.6e m, R = %.6e m" % (lamC,d,R))
print("2  d/(pi R) = %.15f ; aspect (d/2)/R = %.12f ; pi/2 = %.12f" % (d/(np.pi*R),(d/2)/R,np.pi/2))
# 3 identities
th=np.linspace(0,np.pi,100001)
EA=np.cos(th/2)**4; EB=np.sin(th/2)**4; EF=0.5*np.sin(th)**2
print("3  max|E_A+E_B+E_F-1| = %.2e" % np.abs(EA+EB+EF-1).max())
xc=-(d/2)*np.cos(th); xo=(d/2)*(np.sin(th/2)**2-np.cos(th/2)**2)
print("4  centroid of occupation vs -(d/2)cos th : %.2e" % (np.abs(xc-xo).max()/d))
print("5  sin th - 2 cos(th/2) sin(th/2) : %.2e" % np.abs(np.sin(th)-2*np.cos(th/2)*np.sin(th/2)).max())
# 6 grain on spheroid, speed c, uniform theta; check surface and speed numerically
bp=0.05; Om=bp*c/(d/2); T=np.linspace(1e-3,np.pi-1e-3,400001); t=T/Om
rest=c**2-(d/2*Om*np.sin(T))**2-(R*Om*np.cos(T))**2
phidot=np.sqrt(rest)/(R*np.sin(T)); phi=np.concatenate([[0],np.cumsum(0.5*(phidot[1:]+phidot[:-1])*np.diff(t))])
X=-(d/2)*np.cos(T); Y=R*np.sin(T)*np.cos(phi); Z=R*np.sin(T)*np.sin(phi)
sp=np.sqrt(np.gradient(X,t)**2+np.gradient(Y,t)**2+np.gradient(Z,t)**2)/c
print("6  surface residual %.1e ; speed/c in [%.6f, %.6f] (interior)" % (np.abs((X/(d/2))**2+(np.hypot(Y,Z)/R)**2-1).max(), sp[1000:-1000].min(), sp[1000:-1000].max()))
print("   v_x/(beta_p c) - sin th : %.1e  (identity of the parametrization; numerical differentiation only)" % np.abs(np.gradient(X,t)/(bp*c)-np.sin(T))[1000:-1000].max())
# 7 equator ring: L, mu, g with transverse speed c/gamma_p
for b in [0.0,0.05]:
    g_=1/np.sqrt(1-b**2); v=c/g_; E=0.5*m*c**2
    L=E*v*R/c**2; mu=e*v*R/2; g=(mu/muB)/(L/hbar)
    print("7  beta_p=%.2f: L/(hbar/2)=%.8f  mu/muB=%.8f  g=%.12f" % (b,L/(hbar/2),mu/muB,g))
print("   ring circumference/lambda_C = %.12f ; ring frequency (v=c) / nu_C = %.12f" % (2*np.pi*R/lamC,(c/(2*np.pi*R))/(m*c**2/h)))
# 8 round trip and frequency
tm=(np.arange(200000)+0.5)*np.pi/200000; vp=0.05*c; vbar=np.mean(np.abs(vp*np.sin(tm)))
print("8  mean|sin| = %.10f (2/pi = %.10f); period*vbar/lambda_C = %.10f" % (np.mean(np.abs(np.sin(tm))),2/np.pi,(2*np.pi/(vp/(d/2)))*vbar/lamC))
# 9 SR: spheroid becomes a sphere
Vs=np.sqrt(1-4/np.pi**2); print("9  sphere at V = %.6f c (Gamma = %.6f)" % (Vs,1/np.sqrt(1-Vs**2)))
# 10 de Broglie from the ring clock
for V in [0.01,0.5]:
    G=1/np.sqrt(1-V**2); lam=lamC/(G*V); print("10 V=%.2f c: lambda_phase = lambda_C/(Gamma beta) = %.6e m ; h/p = %.6e m" % (V,lam,h/(G*m*V*c)))
# 11 GR
fE=GM/(RE*c**2); fS=GM/(rGPS*c**2); print("11 Phi/c^2 surface %.3e, GPS %.3e, difference %.3e" % (fE,fS,fE-fS))
# 12 hyperbolic length along the meridian of the sphere
a,b=0.4,2.9; s=np.linspace(a,b,200001); trap=getattr(np,'trapezoid',None) or np.trapz; ds=trap(np.ones_like(s)/np.sin(s),s)
print("12 int dtheta/sin = %.10f ; ln tan(b/2)-ln tan(a/2) = %.10f" % (ds,np.log(np.tan(b/2))-np.log(np.tan(a/2))))
# 13 contraction of the axial semi-axis, 1 - 1/Gamma, for the electrons of Table 2 (K in keV)
mc2=m*c**2/e/1e3
for K in [1,30,292,300]:
    G=1+K/mc2; print("13 K=%5.0f keV: V/c=%.4f Gamma=%.4f shortened by %.1f%%  aspect pi/(2Gamma)=%.4f" % (K,np.sqrt(1-1/G**2),G,100*(1-1/G),np.pi/(2*G)))
# 14 the pulsating helix of Paper #62, R = |sin th|/sqrt2 about x = cos th, lies on x^2 + 2 R^2 = 1 (aspect sqrt2)
print("14 max|x^2+2R^2-1| = %.1e ; aspect = %.6f (sqrt2 = %.6f)" % (np.abs(np.cos(th)**2+2*(np.sin(th)/np.sqrt(2))**2-1).max(),1/(1/np.sqrt(2)),np.sqrt(2)))
# 15 if the charge and the whole energy E0 circulated together at the equator, the ratio would be the orbital g = 1
for b in [0.0,0.05]:
    v=c*np.sqrt(1-b**2); L=m*c**2*v*R/c**2; mu=e*v*R/2; print("15 beta_p=%.2f: whole energy circulating -> g = %.12f" % (b,(mu/muB)/(L/hbar)))
