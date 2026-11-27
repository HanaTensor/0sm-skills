# 採用した描像の静止図：回転楕円体のホース、光速の代表の粒、x 軸への射影（赤線の単振動）
import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
plt.rcParams['font.family']='DejaVu Sans'
a,b,f=2.2,0.9,0.30                       # 表示用（実際の x 方向の割合は最大 6.4%）
th=np.linspace(0.03,np.pi-0.03,6000)
mer=f*np.sqrt(np.sin(th)**2+(b/a)**2*np.cos(th)**2)
dphi=(a/(f*b))*np.sqrt(1-mer**2)/np.sin(th)*np.gradient(th)*1.0
phi=np.cumsum(dphi)
x=-a*np.cos(th); y=b*np.sin(th)*np.cos(phi); z=b*np.sin(th)*np.sin(phi)
fig=plt.figure(figsize=(11,5))
ax=fig.add_subplot(121,projection='3d')
u,v=np.mgrid[0:2*np.pi:36j,0:np.pi:18j]
ax.plot_wireframe(-a*np.cos(v),b*np.sin(v)*np.cos(u),b*np.sin(v)*np.sin(u),color='0.85',lw=0.4)
ax.plot(x,y,z,color='#EF9F27',lw=0.9,label='hose: path of a representative grain (speed $c$)')
ax.plot([-a-.3,a+.3],[0,0],[0,0],color='#E24B4A',lw=2,label='$x$ axis: thermal geodesic (red line)')
k=2300; ax.scatter([x[k]],[y[k]],[z[k]],color='#D85A30',s=40); ax.scatter([x[k]],[0],[0],color='#E24B4A',s=30)
ax.plot([x[k],x[k]],[y[k],0],[z[k],0],'k--',lw=0.6)
ax.text(-a-.45,0,0,'A'); ax.text(a+.3,0,0,'B')
ax.set_box_aspect((a,b,b)); ax.set_axis_off(); ax.view_init(18,-60)
ax.legend(loc='upper left',fontsize=8)
ax.set_title('(a) Spheroidal hose: semi-axes $d/2=\\lambda_C/4$ and $\\bar\\lambda_C=\\lambda_C/2\\pi$',fontsize=10)
ax2=fig.add_subplot(122)
T=np.linspace(0,np.pi,400)
ax2.plot(np.degrees(T),np.sin(T),color='0.5',lw=2,label='$\\sin\\theta$ (radiation gradient of Paper #1)')
ax2.plot(np.degrees(th[::150]),np.gradient(x,th)[::150]/a,'o',color='#E24B4A',ms=4,label='$v_x$ of the grain (projection, normalized)')
ax2.plot(np.degrees(T),0.5*np.sin(T)**2,color='#EF9F27',lw=1.5,label='$\\frac{1}{2}\\sin^2\\theta$ (energy in flight)')
ax2.set_xlabel('phase $\\theta$ (deg)'); ax2.set_xlim(0,180); ax2.legend(fontsize=8); ax2.grid(alpha=.3)
ax2.set_title('(b) The projection is the harmonic motion of the red line',fontsize=10)
plt.tight_layout(); plt.savefig('fig_hose.png',dpi=150)
