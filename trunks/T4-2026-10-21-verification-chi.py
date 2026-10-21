import math
import numpy as np
# (1) harmonic shares of the corpus closure: J(th)=sin^4 th (1+sin^2 th)/16
#     Fourier amplitudes of third derivative weighted by n^6 (cos 2n th basis)
th=np.linspace(0,2*np.pi,20001)[:-1]
J=np.sin(th)**4*(1+np.sin(th)**2)/16
# coefficients c_n of cos(2n th) in J
coef={}
for n in range(0,5):
    coef[n]=2*np.mean(J*np.cos(2*n*th)) if n>0 else np.mean(J)
    print(f"n={n}: c={coef[n]:+.6f}")
def shares(absorb):   # absorb(n) = amplitude factor for harmonic n (frequency 2n*nu)
    w={}
    for n in range(1,5):
        w[n]=(coef[n]*absorb(n)*(2*n)**3)**2  # n^6 weighting
    tot=sum(w.values())
    return {n: round(100*w[n]/tot,2) for n in w}
print("uniform chi (amplitude factor const):", shares(lambda n:0.7))
print("frequency-dependent chi (absorb ~ 1/n):", shares(lambda n:0.7/n))
# (2) bubble energy partition under radiation-pressure balance
R=1.0; E=1.0
p=E/(4*math.pi*R**3)          # massless gas, E=4 pi R^3 p
for name,k in [("single membrane p=2g/R",2),("double membrane p=4g/R",4)]:
    g=k and p*R/k
    A_total=4*math.pi*R**2*(1 if k==2 else 2)
    print(name, "gamma*A/E =", round(g*A_total/E,6))
# (3) P predictions for absorption-amplitude chi (P ∝ amplitude^2)
P0=1.00e-43
for chi in [0.0, 1-math.sqrt(0.5), 0.5]:
    print(f"chi={chi:.3f}  energy absorbed={1-(1-chi)**2:.3f}  P={P0*(1-chi)**2:.3e} W")
