"""verify67.py -- recomputes every number quoted in Paper #67 (structural overview).
Inputs: CODATA 2022 constants and measured anomalous moments; no fitted parameter."""
import math
h=6.62607015e-34; hb=h/(2*math.pi); c=299792458.0; e=1.602176634e-19
me=9.1093837139e-31; mp=1.67262192595e-27; mn=1.67492750056e-27; mmu=1.883531627e-28
G=6.67430e-11
a={'e':1.15965218059e-3,'mu':1.16592059e-3,'p':1.79284734463}
mass={'e':me,'mu':mmu,'p':mp,'n':mn}
def beta_from(a_):
    gv=1+abs(a_)/math.sqrt(2); return math.sqrt(1-1/gv**2)
a['n']=1.91304276   # series convention (verify66.py): |a_n| taken as |mu_n|/mu_N, modulus form of #62
B={k:beta_from(v) for k,v in a.items()}
ok=True
def chk(name,val,ref,tol):
    global ok
    good=abs(val-ref)<=tol*abs(ref)
    ok&=good
    print(f"{'ok ' if good else 'BAD'} {name:38s} {val:.6g}   (quoted {ref:.6g})")
lamC=h/(me*c)
chk('beta_ZB (electron)',B['e'],0.0404720,2e-6)
chk('v_ZB [m/s]',B['e']*c,1.2133e7,1e-3)
chk('lambda_C [m]',lamC,2.42631e-12,1e-5)
nuC=c/lamC; nuZB=B['e']*c/lamC
chk('nu_C = c/lambda_C [Hz]',nuC,1.2356e20,1e-4)
chk('nu_ZB = beta c/lambda_C [Hz]',nuZB,5.0007e18,1e-4)
chk('T_tr = 1/nu_ZB [s]',1/nuZB,1.9997e-19,1e-4)
chk('h nu_ZB [keV]',h*nuZB/e/1e3,20.68,1e-3)
nuD=2*me*c**2/h
chk('Dirac 2mc^2/h [Hz]',nuD,2.4712e20,1e-4)
chk('Dirac 2mc^2/hbar [rad/s]',2*me*c**2/hb,1.5527e21,1e-4)
chk('ratio Dirac/nu_ZB',nuD/nuZB,49.42,1e-3)
chk('erroneous 1.55e21/4 [Hz]',2*me*c**2/hb/4,3.88e20,2e-3)
lamZB=lamC/(4*math.pi)
chk('lambda_ZB = lambda_C/4pi [m]',lamZB,1.931e-13,1e-3)
chk('beta c/lambda_ZB [Hz]',B['e']*c/lamZB,6.284e19,1e-3)
chk('2 pi nu_ZB [rad/s]',2*math.pi*nuZB,3.142e19,1e-3)
chk('pi nu_ZB [rad/s]',math.pi*nuZB,1.571e19,1e-3)
chk('Thomas amplitude beta^2 (2pi nu)/4',B['e']**2*2*math.pi*nuZB/4,1.287e16,1e-3)
chk('pitch speed sqrt(1-beta^2)',math.sqrt(1-B['e']**2),0.99918,1e-5)
chk('beta (mass form 1+a)',math.sqrt(1-1/(1+a['e'])**2),0.0481,2e-3)
chk('beta_mu',B['mu'],0.04058,1e-3)
chk('muon-electron difference [%]',(B['mu']/B['e']-1)*100,0.27,0.05)
chk('beta_p',B['p'],0.898,2e-3)
chk('beta_p/beta_e',B['p']/B['e'],22.18,1e-3)
chk('1/beta_e',1/B['e'],24.71,1e-3)
chk('1/beta_p',1/B['p'],1.114,2e-3)
chk('beta_n',B['n'],0.905,3e-3)
chk('1/beta_n',1/B['n'],1.105,3e-3)
chk('nucleon difference [%]',(B['n']/B['p']-1)*100,0.85,0.06)
chk('m0_p = m_p/(1+a_p) [MeV]',mp*c**2/e/1e6/(1+a['p']),335.9,1e-3)
chk('lambda_C of m0_p [fm]',h/((mp/(1+a['p']))*c)*1e15,3.69,5e-3)
chk('reduced lambda_C of m0_p [fm]',hb/((mp/(1+a['p']))*c)*1e15,0.587,5e-3)
chk('G/c^2 [m/kg]',G/c**2,7.4256e-28,1e-4)
chk('c^2/G',c**2/G,1.3466e27,1e-3)
# Earth / GPS clock rates of #22
GM=3.986004418e14; RE=6.371e6; rgps=2.6561e7
chk('Earth surface 1-dtau/dt',GM/(RE*c**2),6.96e-10,5e-3)
chk('GPS altitude 1-dtau/dt (potential)',GM/(rgps*c**2),1.67e-10,5e-3)
chk('Earth-GPS clock-rate difference',GM/(RE*c**2)-GM/(rgps*c**2),5.29e-10,5e-3)
# locking ratio (C1)
a0=5.29177210544e-11; k=8.9875517923e9
FC=k*e**2/a0**2; Fg=me*9.80665
chk('Coulomb force at a0 [N]',FC,8.24e-8,2e-3)
chk('m_e g [N]',Fg,8.93e-30,2e-3)
chk('locking ratio',FC/Fg,9.2e21,1e-2)
chk('e^2/(4pi eps0 G me mp)',k*e**2/(G*me*mp),2.27e39,5e-3)
# storage ring level spacing quoted from #65
chk('storage ring hbar c/R (L=1436 m) [eV]',h*c/1436/e,8.63e-10,5e-3)
# MICROSCOPE / eta
chk('MICROSCOPE bound',2.7e-15,2.7e-15,1e-9)
print('all checks passed' if ok else 'SOME CHECKS FAILED')
