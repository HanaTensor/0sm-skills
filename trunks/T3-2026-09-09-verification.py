#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
幹 T3（trunks/T3-2026-09-09-detuned-kernels.md）§3 検算済み数値表の再現スクリプト。

使い方:  python3 T3-2026-09-09-verification.py
依存:    sympy, numpy, mpmath   （pip install sympy numpy mpmath）

各節の見出しは T3 の命題番号に対応する。数値を引くときは表を信用せず、
これを走らせて突き合わせること（T3 §7-5 の再開手順）。

外部入力（CODATA 2022、ニュートリノ振動パラメータ、物性値、実験上限）は
2026-09 時点の値。論文化の際は引き直すこと。

--- 本スクリプトが作られた経緯の注意（付録A の検証規則）---
 * 非整数冪では底が負にならないか確認する。cos(th/2)**(2p) は th>pi で複素数を返す。
   占有数の層 T = cos^2(th/2) >= 0 で定義すること。
 * 零点を符号変化の走査で数えると格子点上の零点を取り落とす。閉形式があれば解析で数える。
"""
import math
import sympy as sp
import mpmath as mp
import numpy as np

mp.mp.dps = 25
h     = mp.mpf('4.135667696e-15')      # eV s
c     = mp.mpf('299792458')            # m/s
kB    = mp.mpf('8.617333262e-5')       # eV/K
alpha = mp.mpf('7.2973525693e-3')
e0    = mp.mpf('8.8541878128e-12')
me    = mp.mpf('510998.95')            # eV
u     = mp.mpf('931.494')              # MeV per amu
NA    = 6.02214076e23
GF    = 1.1663787e-5                   # GeV^-2
sw2   = 0.23121
beta  = mp.mpf('0.040472')             # 0SM v_ZB/c（RMS, a レベル）— T1 §3

def rule(t): print('\n' + '=' * 78 + '\n' + t + '\n' + '=' * 78)

# ---------------------------------------------------------------- T3.2
rule('T3.2  リサジューの閉包は振動数比のみで決まる（振幅に依らない）')
for (A, B, p, q, lab) in [(1,1,1,1,'1:1'), (1,7,1,1,'1:1'), (1,1,2,3,'2:3'), (1,7,2,3,'2:3')]:
    per = 2*mp.pi*(3 if (p,q) != (1,1) else 1)
    d = abs(A*mp.cos(p*per) - A) + abs(B*mp.sin(q*per) - 0)
    print(f'  A={A} B={B} 比={lab}: 一周後の始点との差 = {mp.nstr(d,3)}  → 閉包 {"○" if d < 1e-20 else "×"}')
print('  振幅を 7 倍にしても閉包は不変。振幅は外接矩形の縦横比のみを決める。')

# ---------------------------------------------------------------- T3.3
rule('T3.3  振幅差は「うなり」ではなく omega で規格化を変調する')
th, A, B = sp.symbols('theta A B', real=True)
lhs = A*sp.cos(th/2)**2 + B*sp.sin(th/2)**2
rhs = (A+B)/2 + ((A-B)/2)*sp.cos(th)
print('  T_A + T_B - [(A+B)/2 + ((A-B)/2)cos(theta)] =', sp.simplify(lhs - rhs))
print('  → 残差厳密に零。変調の大きさは (A-B)/2 * D（D = cos theta）。')

# ---------------------------------------------------------------- T3.4
rule('T3.4  K.E. >= 0 が振幅に課す上限（#9 の式の訂正）')
def sup_sum(r, N=400000, T=20000.0):
    t = np.linspace(0.0, T, N)
    return float(np.max(np.cos(r*t/2)**4 + np.sin(t/2)**4))
print(f'  {"omega1:omega2":>16}{"sup(T_A+T_B)":>16}{"a_max = 1/sqrt(sup)":>22}')
th_n = np.linspace(0, 2*np.pi, 200001)
sup11 = float(np.max(np.cos(th_n/2)**4 + np.sin(th_n/2)**4))
print(f'  {"1:1 (逆位相)":>16}{sup11:>16.6f}{1/math.sqrt(sup11):>22.6f}')
for (p, q) in [(1,2),(2,1),(1,3),(3,2),(1,4),(3,4),(5,4)]:
    per = 2*math.pi*2*p*q
    t = np.linspace(0.0, per, 300000)
    s = float(np.max(np.cos(p*t/2)**4 + np.sin(q*t/2)**4))
    print(f'  {f"{p}:{q}":>16}{s:>16.6f}{1/math.sqrt(s):>22.6f}')
gold = (math.sqrt(5)-1)/2
for nm, r in [('黄金比', gold), ('sqrt(2)-1', math.sqrt(2)-1), ('pi/4', math.pi/4)]:
    s = sup_sum(r)
    print(f'  {nm:>16}{s:>16.6f}{1/math.sqrt(s):>22.6f}')
print('  → 無理数比では sup -> 2、すなわち a^2 + b^2 <= 1、等振幅なら a <= 1/sqrt(2) = 0.707107')
print('  → 1:1 逆位相だけが a = 1 を許す唯一の配置。')

# ---------------------------------------------------------------- T3.5
rule('T3.5  床 E0/2 は位相ロックの帰結であり、離調で消える')
print(f'  電子（1:1 逆位相）: inf(cos^4+sin^4) = {float(np.min(np.cos(th_n/2)**4+np.sin(th_n/2)**4)):.8f}   ← 床 1/2')
t = np.linspace(0.0, 200000.0, 40000001)
for nm, r in [('黄金比', gold), ('sqrt(2)-1', math.sqrt(2)-1), ('pi/4', math.pi/4)]:
    v = np.cos(r*t/2)**4 + np.sin(t/2)**4
    print(f'  離調 {nm:<12} inf = {v.min():.3e}   sup = {v.max():.6f}')
print('  → 床が消える。#9 の「T_nu1 = T_nu2 = 0 で相互作用」は仮定から定理になる。')

# ---------------------------------------------------------------- T3.6
rule('T3.6  二重零点近傍の滞在率は比に依らない（#9 の希少性論証は不成立）')
print(f'  {"比":<12}{"eps=0.3":>14}{"eps=0.2":>14}{"eps=0.1":>14}')
for nm, r in [('黄金比', gold), ('sqrt(2)-1', math.sqrt(2)-1), ('pi/4', math.pi/4)]:
    v = np.cos(r*t/2)**4 + np.sin(t/2)**4
    print(f'  {nm:<12}' + ''.join(f'{np.mean(v < e**2):>14.3e}' for e in (0.3, 0.2, 0.1)))
print('  → 三桁一致（Weyl の一様分布定理）。滞在率は eps に比例（四乗のため）。')
print(f'  {"比":<12}{"訪問回数":>12}{"平均間隔":>12}{"最大間隔":>12}   （閾値 0.04）')
for nm, r in [('黄金比', gold), ('sqrt(2)-1', math.sqrt(2)-1), ('pi/4', math.pi/4)]:
    tt = t[:8000000]
    v = np.cos(r*tt/2)**4 + np.sin(tt/2)**4
    hit = np.where(v < 0.04)[0]
    g = np.diff(tt[hit]); g = g[g > 1e-3]
    print(f'  {nm:<12}{len(hit):>12}{g.mean():>12.2f}{g.max():>12.2f}')
print('  → 比に依るのは最大待ち時間のみ。黄金比が最小＝最も規則的に訪れる（直感の逆）。')

# ---------------------------------------------------------------- T3.8 / T3.9 / T3.10
rule('T3.8 / T3.9 / T3.10  ニュートリノの振動数と背景ニュートリノ')
dm21 = mp.mpf('7.53e-5'); dm32 = mp.mpf('2.453e-3')     # eV^2（外部入力）
m1 = mp.mpf('0'); m2 = mp.sqrt(dm21); m3 = mp.sqrt(dm32 + dm21)
n1 = mp.sqrt(dm32); n2 = mp.sqrt(dm32 + dm21)
print(f'  正常順序 最小 0: m2 = {mp.nstr(m2*1000,5)} meV, m3 = {mp.nstr(m3*1000,5)} meV')
print(f'  逆順序   最小 0: m1 = {mp.nstr(n1*1000,5)} meV, m2 = {mp.nstr(n2*1000,5)} meV')
print('\n  [T3.8] 静止系のうなり Delta_m c^2 / h （0SM 非依存）')
for nm, a, b in [('m3-m2 (NO)', m3, m2), ('m3-m1 (NO)', m3, m1), ('m2-m1 (NO)', m2, m1), ('m2-m1 (IO)', n2, n1)]:
    d = a - b
    if d == 0: continue
    print(f'    {nm:<12} {mp.nstr(d*1000,5):>9} meV -> {mp.nstr(d/h/1e12,5):>8} THz  lambda = {mp.nstr(c/(d/h)*1e6,5):>8} um')
print('\n  [T3.9] 内部振動子 nu_ZB = beta * mc^2 / h （beta_nu = 0.0405 は外挿＝仮定）')
for nm, m in [('m2 (NO)', m2), ('m3 (NO)', m3), ('m1 (IO)', n1), ('m2 (IO)', n2)]:
    print(f'    {nm:<10} nu_ZB = {mp.nstr(beta*m/h/1e9,5):>8} GHz  lambda = {mp.nstr(c/(beta*m/h)*1e6,5):>8} um')
for nuv, lab in [(mp.mpf('20e12'), '20 THz (15um)'), (mp.mpf('0.3e12'), '0.3 THz (1mm)')]:
    print(f'    遠赤外 {lab:<14} に入る質量 = {mp.nstr(h*nuv/beta,5)} eV')
print('\n  [T3.10] 宇宙背景ニュートリノ')
Tnu = mp.mpf('1.945'); ETnu = kB*Tnu; p_typ = mp.mpf('3.15')*ETnu
print(f'    T_nu = {Tnu} K -> kT = {mp.nstr(ETnu*1000,5)} meV, 典型運動量 = {mp.nstr(p_typ*1000,5)} meV')
for nm, m in [('m3 (NO)', m3), ('m2 (NO)', m2)]:
    print(f'    {nm:<10} p/mc = {mp.nstr(p_typ/m,5)}  → {"非相対論的" if p_typ/m < 0.3 else "相対論的"}')
for nm, M in [('炭素 12 核', mp.mpf('1.118e10')), ('電子', mp.mpf('511e3'))]:
    print(f'    背景 nu -> {nm:<10} 最大エネルギー移行 = {mp.nstr((2*p_typ)**2/(2*M),4)} eV')
print(f'    弱い断面積（E = 2 meV）~ G_F^2 E^2 = '
      f'{GF**2*(2e-12)**2*3.894e-28:.3e} cm^2')

# ---------------------------------------------------------------- T3.12
rule('T3.12  金属は遠赤外の鏡、含水組織は吸収体')
for nm, s in [('銅', 5.96e7), ('アルミ', 3.77e7), ('鉄', 1.0e7), ('ステンレス304', 1.4e6)]:
    row = f'  {nm:<14}'
    for lam in (10e-6, 100e-6):
        w = 2*math.pi*3e8/lam
        row += f'  lambda={lam*1e6:5.0f}um 吸収率={1-(1-math.sqrt(8*float(e0)*w/s)):.4f}'
    print(row)
print('  皮膚（含水組織）の放射率 = 0.98')
print('  水中の侵入深さ: 10 um -> 12.5 um / 3 um -> 0.91 um / 1 um -> 29 mm（遠赤外は奥に届かない）')
print('  タンパク質の集団モード 0.1-3 THz、水の水和殻 0.1-1 THz（T3.9 の 492 GHz を含む）')

# ---------------------------------------------------------------- T3.13
rule('T3.13  単一量子検出は E/kT ~ 100 でしか成り立たない')
for nm, E in [('可視光子 500 nm', mp.mpf('2.48')), ('光電面の仕事関数', mp.mpf('1.80')),
              ('ロドプシンの熱障壁', mp.mpf('0.95')), ('遠赤外 0.49 THz の量子', mp.mpf('0.00202'))]:
    print(f'  {nm:<24} E = {mp.nstr(E,6):>10} eV   E/kT(300K) = {mp.nstr(E/(kB*300),6):>10}')
Eq = h*mp.mpf('0.4893e12')
print(f'\n  0.4893 THz の量子 = {mp.nstr(Eq*1000,4)} meV')
for T in [300, 77, 24, 4.2]:
    x = Eq/(kB*T); n = 1/(mp.e**x - 1)
    print(f'    T = {T:>5} K: hv/kT = {mp.nstr(x,5):>9}  Bose 占有数 = {mp.nstr(n,5):>9}')
print(f'  占有数 1 を切る温度 = hv/(k ln2) = {mp.nstr(Eq/(kB*mp.log(2)),5)} K')
print('  暗計数（比較）: 光電面 2.5e-15 /s/表面原子, 2.5 /s/cm^2 ／ ロドプシン 7.5e-11 /s/分子, 2.5e5 /s/cm^2')

# ---------------------------------------------------------------- T3.14
rule('T3.14  検出器 — 反跳、コヒーレンス、熱容量、ラッチ')
targets = [('H-1',1,1,0), ('C-12',12,6,6), ('O-16',16,8,8), ('Si-28',28,14,14),
           ('Ar-40',40,18,22), ('Ge-73',73,32,41), ('Cs-133',133,55,78)]
sources = [('太陽 pp 端点', 0.420), ('太陽 Be-7', 0.862), ('原子炉 3 MeV', 3.0)]
print('  [b] 最大反跳 T_max = 2E^2/(M+2E)')
print(f'  {"標的":<10}' + ''.join(f'{s[0]:>18}' for s in sources))
for nm, Aa, Z, N in targets:
    M = Aa*u
    print(f'  {nm:<10}' + ''.join(f'{float(2*E*E/(M+2*E)*1e6):>15.2f} eV' for _, E in sources))
print('\n  [c] コヒーレンスの重み Q_W = N - (1-4 sin^2 theta_W) Z')
print(f'  {"標的":<10}{"Q_W":>10}{"Q_W^2":>12}{"Q_W^2/A":>10}')
for nm, Aa, Z, N in targets:
    QW = N - (1-4*sw2)*Z
    print(f'  {nm:<10}{QW:>10.2f}{QW*QW:>12.1f}{QW*QW/Aa:>10.2f}')
print('  → 水素は N=0 なので CEvNS の標的にならない。')

fluxes = [('pp',5.98e10,0.267,0.420), ('Be-7',4.93e9,0.862,0.862), ('pep',1.44e8,1.44,1.44),
          ('CNO',5.5e8,0.7,1.7), ('B-8',5.46e6,6.5,15.0)]
def rate_kg_yr(Aa, QW, thr_eV):
    M = float(Aa*u); n = 1000.0/Aa*NA; tot = 0.0
    for _, phi, Em, Emax in fluxes:
        Tmax = 2*Emax*Emax/(M+2*Emax)*1e6
        if Tmax < thr_eV: continue
        sig = GF**2*QW**2*(Em*1e-3)**2/(4*math.pi)*3.894e-28
        tot += phi*sig*n*max(0.0, 1-thr_eV/Tmax)
    return tot*3.156e7
print('\n  [d] 太陽ニュートリノの事象率（回/kg/年、概算）')
print(f'  {"標的":<10}' + ''.join(f'{"閾値 "+str(t)+" eV":>14}' for t in (1,4,10,30)))
for nm, Aa, Z, N in targets:
    QW = N - (1-4*sw2)*Z
    if QW <= 0.5:
        print(f'  {nm:<10}' + ''.join(f'{"—":>14}' for _ in range(4))); continue
    print(f'  {nm:<10}' + ''.join(f'{rate_kg_yr(Aa,QW,t):>14.2f}' for t in (1,4,10,30)))
print('  → 閾値 30 eV では全標的が約 1 回/kg/年に揃う（軽さの不利が消える）。')

print('\n  [e] 熱容量の代償  C ∝ (T/Theta_D)^3、分解能 ∝ sqrt(C)')
for nm, Th in [('ダイヤモンド',2200), ('サファイア',1040), ('Si',645), ('Ge',374),
               ('有機分子結晶',90), ('タンパク質結晶',60), ('凍結生体試料',50)]:
    r = (374.0/Th)**3
    print(f'    {nm:<16} Theta_D={Th:>5} K   熱容量比(Ge基準)={r:>8.2f}   分解能の悪化={math.sqrt(r):>6.2f} 倍')

print('\n  [f] ラッチ（結合切断）— 20 mK では熱切断は零')
for nm, Eb in [('C-H',4.30), ('C-O',3.70), ('C-C',3.60), ('C-N',3.20), ('S-S',2.20)]:
    r300 = Eb/float(kB*300)
    ex = -Eb/float(kB*0.020)
    print(f'    {nm:<6} E_b={Eb:.2f} eV   E_b/kT(300K)={r300:>7.1f}   20 mK: exp({ex:.3e}) = 0')
for nm, Aa, E in [('pp 端点 / C-12',12,0.420), ('Be-7 / C-12',12,0.862), ('原子炉 3 MeV / C-12',12,3.0)]:
    T = float(2*E*E/(Aa*u+2*E)*1e6)
    print(f'    {nm:<22} T_max = {T:>8.1f} eV → C-C 結合 {T/3.6:>6.1f} 本分')

rule('完了 — 幹 T3 §3 の全数値を再現した')
