# Thomas Precession in the 0-Sphere Model: Physical Framing
# Based on Tomonaga's "The Story of Spin" (スピンはめぐる)
# Created: 2026-04-03 | Applies to: #19, #47, #48, #49 and all subsequent papers

---

## 1. Source: Tomonaga's Explanation (朝永振一郎「スピンはめぐる」)

Nobel Laureate Sin-Itiro Tomonaga's description of Thomas precession,
which provides the physical foundation for how the 0-Sphere model
treats Thomas precession:

---

『トーマスのやった計算は恐ろしくややこしいので、ここでお話しするにはしんどすぎます。
しかしとにかく、"電子が静止していて核が回っている座標系"というのをそう簡単に扱って
はいかん、ということなのです。電子が等速運動をしているなら、そういう座標系は実験室系
からローレンツ変換で簡単に与えられます。しかし電子に加速度があると面倒なことが起こる。
確かに電子がじっとしている座標系は存在しています。詳しくいうと、電子の上に原点を載せ
ながら電子と一緒に動いてゆく座標系がそれです。しかし、原点が電子と一緒に動いている、
というだけでは座標系は一つに決まりません。つまりその時、x, y, z軸の向きをどうとるかが
問題です。そこで、原点が電子と一緒に動いてゆく、という条件の他に、x, y, z軸が常に並行
に移動してゆく、といった条件をつける必要があるでしょう。ところがこの"平行"ということは、
等速運動の電子に対しては明白なのですが、電子に加速度があると、それほど明白なことでは
ない。こういう点にトーマスは気づいたのです。

　そこでまずトーマスは、座標軸の平行な移動とは何か、ということを論じました。そして、
軸の平行な移動とは、各瞬間ごとに、その瞬間での軸が無限小時間前の軸と平行になっている
ことだ、と結論しました。電子と一緒に動く原点を持ち、かつこの意味において並行に移動し
てゆく軸を持つ座標系は、電子の固有座標系とでもいうべきものです。トーマスは、この系の
軸を実験室系からみると、電子に加速度があるときには、それは決して平行に移動していなく
て、そこには"回転"が伴っていることを導いたのです。彼はしんどい計算をやって、固有座標
系の軸が、実験室系からみると

    Omega = 1/(2c^2) [a x v]

という角速度で回転していることを見つけたのです。』

---

## 2. Core Principle (Tomonaga's Key Insight)

Thomas precession is NOT caused by the spatial path being curved.
It is a kinematic inevitability of relativistic ACCELERATED motion:

  - For uniform motion: the rest frame is unambiguously given by
    a Lorentz transformation from the lab frame.
  - For accelerated motion: even when the coordinate axes are
    transported "in parallel" (each instant parallel to the
    infinitesimally preceding instant), the axes as seen from
    the lab frame are NOT in parallel transport — they rotate.
  - This rotation appears whenever v x a != 0,
    i.e., whenever acceleration has a component perpendicular
    to the velocity.

The formula:   Omega_T = -(1/2c^2)(a x v)

is the angular velocity of this rotation as seen from the lab frame.


## 3. Causal Chain in the 0-Sphere Model

CORRECT order (as of #49 v3):

  [1] Radiation gradient F = E_0 sin(theta)
        --> photon sphere is continuously ACCELERATED
            throughout the A->B traversal (Paper #1)

  [2] ZB sustains this oscillation at v_ZB ≈ 0.04c (relativistic)

  [3] Tomonaga mechanism:
        --> because the photon sphere is perpetually accelerated
            at relativistic speed, Thomas precession NATURALLY
            ARISES as a structural feature of the 0-Sphere
            internal dynamics, rather than being introduced
            as an additional assumption.

  [4] The radiation gradient acts within the geometry of the
      internal thermal phase space:
        --> a(t) = -v_0 * omega * sin(omega*t) * e_y  (transverse)
        --> v(t) =  v_0 * cos(omega*t)         * e_x
        --> v x a = -(v_0^2 * omega / 2) sin(2*omega*t) * e_z  != 0
            (as realized in the present construction)

  [5] Substituting into Thomas formula:
        --> Omega_T = -(v_0^2 * omega / 4c^2) sin(2*omega*t) * e_z
            (established in Paper #19)

  [6] Quantitative derivation of the transverse geometry of the
      thermal geodesic from first principles:
        --> OPEN TASK (item viii, Paper #49 Section 7)


## 4. Anti-Pattern (AVOID this explanation order)

  WRONG:
    Path is arc-connected in 3D space
      --> thermal geodesic has geometric curvature
        --> acceleration has transverse component
          --> v x a != 0
            --> Thomas precession

  CORRECT:
    Photon sphere undergoes accelerated motion (radiation gradient)
      --> Tomonaga mechanism: proper frame rotates in lab frame
        --> Thomas precession naturally arises
          --> v x a != 0 expresses this concretely
            --> Omega_T = -(v_0^2*omega/4c^2) sin(2*omega*t) * e_z


## 5. Reference Implementation

Paper #49 main.tex v3, Section 3.2.1 (Sec. ejection_thomas),
paragraph beginning:
  "The justification is provided by Thomas precession,
   understood in the sense made precise by Tomonaga..."

Key phrases established in #49 v3:
  - "naturally arises as a structural feature ... rather than
     being introduced as an additional assumption"
  - "as realized in the present construction"
  - "a kinematic consequence of the radiation-gradient-driven
     ZB acceleration, not of circular rotation"


## 6. Cross-References

  Paper #19: Omega_T(t) vector form established (e_z correction to #10)
  Paper #47: Thomas precession -> g=2 geometric basis (double-angle)
  Paper #48: pi-periodicity of Omega_T -> spin-2 candidate
  Paper #49: ejection mechanism via Thomas-precession stress;
             Tomonaga framing first introduced in series

  global-concept.md Section B-3: Thomas precession equation index
