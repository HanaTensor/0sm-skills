"""幹 T2 の T2.13（電荷＝保護された巻き数）の検算 ── 2026-09-14。sympy / numpy。§3 の 2026-09-14 追加行を命題番号順に再現する"""
import numpy as np, sympy as sp
from math import gcd

# ---- 1. 規格化 a^2+b^2=1 (a=A cos t, b=B sin(t+δ)) は A=B, δ∈{0,π} を強制する
t,A,B,d=sp.symbols('t A B delta',real=True)
expr=sp.expand_trig((A*sp.cos(t))**2+(B*sp.sin(t+d))**2)
c=sp.Poly(sp.expand(sp.simplify(expr).rewrite(sp.cos)), sp.cos(2*t), sp.sin(2*t)) if False else None
# 直接: expr = (A^2+B^2)/2 + (A^2-B^2 cos2δ)/2 cos2t - (B^2 sin2δ)/2 sin2t
e2=sp.simplify(expr - ((A**2+B**2)/2 + (A**2-B**2*sp.cos(2*d))/2*sp.cos(2*t) - (B**2*sp.sin(2*d))/2*sp.sin(2*t)))
print("1. a^2+b^2 の展開残差 =",sp.simplify(e2))
print("   一定 ⟺ A^2 = B^2 cos2δ かつ B^2 sin2δ = 0 ⟹ A=B, δ∈{0,π}（δ=π/2 は A=0 で退化）")

# ---- 2. 巻き数（観測層 Bloch ベクトル s=(2ab, a^2-b^2) = z^2 の巻き数 = 2×振幅層）
def W_amp(p,q,delta=0.0,N=400000):
    tt=np.linspace(0,2*np.pi,N,endpoint=False)
    z=np.cos(p*tt)+1j*np.sin(q*tt+delta)
    ang=np.unwrap(np.angle(z))
    return (ang[-1]-ang[0]+(ang[1]-ang[0]))/(2*np.pi), np.abs(z).min()

print("\n2. 1:1 ロックで δ を回す（振幅層の巻き数 / min|z|）")
for dd in [0,0.5,1.4,np.pi/2,1.8,np.pi,4.5,3*np.pi/2]:
    W,r=W_amp(1,1,dd); print(f"   δ={dd:6.3f}  W={W:+.3f}  min|z|={r:.3f}")

print("\n3. 有理比 p:q（δ=0）: 一方が偶数→W=0、奇:奇→W 奇数（保護なし）")
for p in range(1,8):
    for q in range(1,8):
        if gcd(p,q)!=1: continue
        W,r=W_amp(p,q)
        tag='even' if (p%2==0 or q%2==0) else 'odd:odd'
        print(f"   {p}:{q} {tag:7s} W={W:+.3f} min|z|={r:.3f}")

print("\n4. 奇:奇 の保護されなさ（3:5, δ を回す）")
for dd in np.linspace(0,np.pi,9):
    W,r=W_amp(3,5,dd); print(f"   δ={dd:.3f} W={W:+.3f} min|z|={r:.3e}")

print("\n5. 無理数比（黄金比）: 原点への最接近距離が時間とともに 0 へ")
phi=(1+5**0.5)/2
for T in [10,100,1000,10000]:
    tt=np.linspace(0,T,int(T*400)); z=np.cos(tt)+1j*np.sin(phi*tt)
    print(f"   T={T:6d}  min|z|={np.abs(z).min():.3e}")

print("\n6. 床とギャップは同じもの: |z|^2 = 𝒯_A+𝒯_B、T_A+T_B = 𝒯_A^2+𝒯_B^2 ≥ (𝒯_A+𝒯_B)^2/2")
th=sp.symbols('theta',real=True)
TA=sp.cos(th/2)**2; TB=sp.sin(th/2)**2
print("   電子: 𝒯_A+𝒯_B =",sp.simplify(TA+TB),"  min(T_A+T_B) =",sp.nsimplify(sp.minimum(TA**2+TB**2,th)))

print("\n7. 符号の住処: 2ab は δ=0/π で符号反転、エネルギー層の交差項 2𝒯_A𝒯_B は不変")
for dd in [0,sp.pi]:
    a=sp.cos(t); b=sp.sin(t+dd)
    print(f"   δ={dd}: 2ab = {sp.simplify(2*a*b)},  2a^2b^2 = {sp.simplify(2*a**2*b**2)}")

print("\n8. 層の梯子（観測周期 2π あたりの巻き数）")
for name,f in [("振幅 (cos θ/2, sin θ/2)",lambda th:np.cos(th/2)+1j*np.sin(th/2)),
               ("温度/Bloch (sin θ, cos θ)",lambda th:np.sin(th)+1j*np.cos(th)),
               ("2ω 成分 (sin 2θ, cos 2θ)",lambda th:np.sin(2*th)+1j*np.cos(2*th))]:
    tt=np.linspace(0,2*np.pi,200001); ang=np.unwrap(np.angle(f(tt)))
    print(f"   {name}: {abs(ang[-1]-ang[0])/(2*np.pi):.3f}")

# ---------- 2026-09-14b 追加（Opus 5 の独立検算を再現） ----------
print("\n9. 循環 L = u v' − v u'（u = cos(ω_A t/2), v = sin(ω_B t/2)）")
def L_stats(wA,wB,T=20000.0,dt=0.01):
    tt=np.arange(0,T,dt); u=np.cos(wA*tt/2); v=np.sin(wB*tt/2)
    du=-wA/2*np.sin(wA*tt/2); dv=wB/2*np.cos(wB*tt/2)
    L=u*dv-v*du
    return L.mean(), np.sqrt((L**2).mean())
m,r=L_stats(1,1); print(f"   1:1        ⟨L⟩={m:+.4f}  rms={r:.4f}  （ω/2 = 0.5 で一定）")
for nm,wB in [("黄金比",(1+5**0.5)/2),("√2",2**0.5),("π/4",np.pi/4),("1:1.0001",1.0001)]:
    m,r=L_stats(1,wB); print(f"   1:{nm:8s} ⟨L⟩={m:+.2e}  rms={r:.3f}  rms/0.5={r/0.5:.2f}")
print("   → 離調で一次（平均）は 1/T で零、二次（rms）は電子の 6–9 割が残る")
for T in [2000,20000,200000]:
    m,_=L_stats(1,(1+5**0.5)/2,T=T,dt=0.02); print(f"   黄金比 T={T:6d}: T·⟨L⟩ = {T*m:+.3f}（O(1) に留まる）")

print("\n10. 全数走査 p,q ≤ 60（互いに素）: |W| ≤ 1 か、原点通過は何通りか")
import itertools
cnt={ -1:0,0:0,1:0}; through=0; other=0
for p in range(1,61):
    for q in range(1,61):
        if gcd(p,q)!=1: continue
        W,r=W_amp(p,q,0.0,N=200000)
        if r<1e-6: through+=1; continue
        Wi=int(round(W))
        if abs(Wi)>1: other+=1
        else: cnt[Wi]+=1
print(f"   W=+1: {cnt[1]}  W=−1: {cnt[-1]}  W=0: {cnt[0]}  原点通過: {through}  |W|≥2: {other}")
print("   規則: q 偶 → 原点通過（cos(pτ)=0 かつ sin(qτ)=0 は q(2k+1)=2pm を要し q 偶で可）／p 偶 q 奇 → W=0／奇:奇 → ±1")

# ---------- 2026-09-14c 追加（K15 の閉じた式と指標和） ----------
print("\n11. K15: 巻き数の有限和（正 y 軸の符号付き横断数）と指標和の閉じた式")
def W_sum(p,q):   # W = ½ Σ_k (−1)^k sign sin(πq(2k+1)/2p)
    return 0.5*sum((-1)**k*np.sign(np.sin(np.pi*q*(2*k+1)/(2*p))) for k in range(2*p))
def W_char(p,q):  # 指標和の評価: q 偶 → 原点通過（未定義）／p 偶 → 0／奇:奇 → χ₄(q) = (−1)^((q−1)/2)
    if q%2==0: return None
    return 0 if p%2==0 else (-1)**((q-1)//2)
bad=0;n=0
for p in range(1,61):
    for q in range(1,61):
        if gcd(p,q)!=1: continue
        wn,r=W_amp(p,q,0.0,N=200000); n+=1
        if r<1e-6:
            if W_char(p,q) is not None: bad+=1
            continue
        if int(round(wn))!=int(round(W_sum(p,q))) or int(round(wn))!=W_char(p,q): bad+=1
print(f"   直接計算 vs 有限和 vs 指標式（p,q ≤ 60、{n} 通り）: 不一致 {bad}")
bad=0;n=0
for p in range(1,302):
    for q in range(1,302):
        if gcd(p,q)!=1 or q%2==0: continue
        n+=1
        if int(round(W_sum(p,q)))!=W_char(p,q): bad+=1
print(f"   有限和 vs 指標式（p,q ≤ 301、q 奇、{n} 通り）: 不一致 {bad}")
print("   → W ∈ {−1, 0, +1} は定理。奇:奇の符号は q の mod 4 の類で決まる（1:3 → −1、1:5 → +1、3:5 → +1、3:7 → −1）")
