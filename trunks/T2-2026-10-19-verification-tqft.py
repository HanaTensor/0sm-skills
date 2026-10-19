"""幹 T2 の T2.8（TQFT との接点、2026-10-19）の検算。
(1) D = cos(theta) を超ポテンシャルとする Witten 変形: 0-形式・1-形式ラプラシアンの低い固有値と零モードの局在
(2) 移送一回の作用 int sqrt(1-D^2) dD と一往復の相平面面積
(3) 緯度 theta0 の Berry 位相 = -Omega/2（スピン s=1/2 の Wess-Zumino 項）
実行: python3 T2-2026-10-19-verification-tqft.py"""
import numpy as np
from scipy.integrate import quad
# (1) Witten deformation of D=cos(theta) on S^1: low spectrum of 0-form and 1-form Laplacians
N=2000; th=np.linspace(0,2*np.pi,N,endpoint=False); h=th[1]-th[0]
L=(np.diag(-2*np.ones(N))+np.diag(np.ones(N-1),1)+np.diag(np.ones(N-1),-1)); L[0,-1]=L[-1,0]=1; L/=h*h
for t in (2.0,8.0):
    V0=t*t*np.sin(th)**2 + t*np.cos(th)   # Delta_t on functions
    V1=t*t*np.sin(th)**2 - t*np.cos(th)   # Delta_t on 1-forms
    for name,V in (("0-form",V0),("1-form",V1)):
        w,v=np.linalg.eigh(-L+np.diag(V)); i=np.argmax(np.abs(v[:,0]))
        print(f"t={t} {name}: lowest eig {w[:3].round(6)}  ground state peaks at theta/pi={th[i]/np.pi:.3f}")
# (2) action per A->B transfer: int sqrt(1-D^2) dD over [-1,1]; full cycle phase-space area
a,_=quad(lambda x:np.sqrt(1-x*x),-1,1); print("A->B action",a,"pi/2=",np.pi/2,"; full cycle",2*a)
# (3) Berry phase on latitude theta0: gamma=-Omega/2
for t0 in (np.pi/3,np.pi/2):
    Om=2*np.pi*(1-np.cos(t0)); print("theta0/pi",t0/np.pi,"gamma",-Om/2,"= -2pi sin^2(t0/2)",-2*np.pi*np.sin(t0/2)**2)
