# 照合表：新 #67「回転楕円体のホース」第 1 稿 × コーパス（2026-11-27）

- 草稿の行番号は第 1 稿（`draft1/main.tex`）のもの。コーパスは `0sm-skills/tex-sources/NN/main.tex:行`、幹は `trunks/…:行`。
- 判定：**一致**／**食い違い**／**新**（草稿が新しく言っていること）／**要引用**（コーパスがすでに言っていて、草稿が引用すべきこと）。
- 幹と Thermal Rays 論文（現 `tex-sources/67`、改番後 #68）は未公開なので、引用先ではなく整合の情報として扱う。
- 照合は四つの読み役（#1・#62・#65／#2・#10・#15・#50／#6・#7・#11・#29・#51 v3／#22・Thermal Rays・幹 T1・T3・T4・T8・README §0）と、主の対話（#48・#51・#66 と要所の再確認）で行った。要所の引用は主の対話で原文に当たり直した（★印）。

---

## A. 核の距離 d = λ_C/2 と横の半径 ƛ_C

| 草稿の節と主張 | コーパスの該当箇所 | 判定 |
|---|---|---|
| I l.122・II l.150「核の距離 λ_C/2 は #66 で使った値」 | ★66:352「The kernels are separated by λ_C/2 … ~\cite{H51}」。★51:208「The kernels are separated by λ_C/2 along the transport path, so that one cycle … a round trip … covers a path of length λ_C」 | **要引用**：#66 自身が #51 v3 を出典にしている。**#51 v3 と #66 を並べて引く** |
| 同上（それ以前の論文） | ★2:72「separated by a distance of 2a, which is the same length of the electron's Compton wavelength」。★10:199「this distance was assumed to be the Compton wavelength」。1:70「apart from a distance of Compton wavelength presumably」。★65:248「separated by about one Compton wavelength」。65:1455「One completed transfer from kernel A to kernel B」（周期を片道とする） | **食い違い**：#1・#2・#10・寄託済みの #65 の本文では距離は λ_C。#65 冒頭のコメント（l.4–7）に「λ_C/2・往復」への改訂予定があるが、未反映 |
| 同上（#51 の内部） | 51:215「Δx ∼ λ_C is a proper length」。51:387「0 < \|x_A − x_B\| ≤ πλ_C」 | **食い違い**（#51 の内部で λ_C/2 と ∼λ_C が混在） |
| I l.124「なぜ λ_C/2 かは未決だった」・II 節の導出（一つの光子を往復で一度持つ） | #51 は上限（Bonnet–Myers）と非対蹠性を示すだけで値は導いていない（51:385–399）。Thermal Rays:291–307 は「往復に一波長＝共振器の基本モード」を書くが、往復 λ_C は入力として受け取る | **新**（寄託済みの論文で d = λ_C/2 を導いたものは無い）。B1 の答え：**「寄託済みの論文に記述はあるが、導出は無い」** |
| II 節 l.152–163 横の半径 ƛ_C、d = πƛ_C、縦横比 π/2 | 2:257「virtual photons with a radius equal to the Compton wavelength」。51:370「r ∼ λ_C」。ƛ_C を半径に置く箇所は無い | **新**（#2 の半径 λ_C とは食い違う） |
| II 節 前提 E₀ = m_ec² | 65:2018「Whether E₀ … is mc² or 2mc² is an open bookkeeping question」。幹 T1 の K4（E₀ の層、著者判断待ち） | **食い違いの種**：E₀ = 2mc² なら前提の波長が λ_C/2 に変わる。草稿は K4 の一択を黙って選んでいる |

## B. ホースと螺旋（#51・#50・#62・#11）

| 草稿の節と主張 | コーパスの該当箇所 | 判定 |
|---|---|---|
| I l.124「#51 が導入した螺旋が載る面を本稿が定める」 | ★51:1175「v_ZB ≈ 0.04c transverse and v_pitch ∼ c longitudinal」（表 II も同じ）。50:773「v_ZB ≈ 0.04c … is the equatorial speed of the photon-sphere rotation in the yz-plane」。幹 T3:45「v_ZB は螺旋の横断回転速度」 | **食い違い（最重要）**：#51・#50・幹 T3 では横が亜光速で縦が ∼c。草稿では縦が v_p < c、横が ≈ c と正反対。草稿はこれを書いていない |
| III 節 粒は速さ c で進む | ★51:1177「Alternative 1: uniform helical speed c … was rejected … would require discarding the most precise numerical prediction」 | **食い違い**：#51 が退けた形に近い。草稿は軸の成分を亜光速にして v_ZB との接点を残しているが、#51 の退けた理由にどう答えるかを書いていない |
| III 節 ホースは実空間の面、粒は実空間の螺旋を描く | ★50:426「The apparent rotation resides entirely in internal phase space … no physical object, executes a circular orbit in real space」。51:236「not the classical worldline … the internal phase trajectory」。51:923 | **食い違い（重要）**：#50・#51 の但し書きと正面からぶつかる。SPH の立場（著者 §3.1）とは整合 |
| III 節 熱測地線＝軸（赤線）、担い手＝螺旋（青線） | 29:165「thermal geodesic … reduces to a straight trajectory in real space」（その上を光子球が動く）。51:429「along the unique helical arc」（熱測地線＝螺旋の弧） | **食い違い**：#29 とも #51 とも役割の割り振りが違う |
| III 節 エネルギーは螺旋を通り、直線上にあるのは影だけ | 11:191「energy is transmitted along a single, shortest path between points A and B」。11:926。10:203「would travel in a straight line with the shortest path」 | **食い違い** |
| III 節 核は極にある | 51:397–399「The kernels therefore do not sit at antipodal positions」（一意性の根拠） | **食い違い（構造）**：回転楕円体の両極はすべての子午線で結ばれる。軸を熱測地線に置くことで一意性は保たれるが、草稿はそう書いていない |
| III 節 回転楕円体という形 | 62:271–302 脈動する螺旋 R(θ) = \|sin θ\|/√2、R² = ½sin²θ。x = cos θ とすると x² + 2R² = 1（主の検算）＝**縦横比 √2 の回転楕円体** | **要引用**：#62 の螺旋はすでに回転楕円体の上にある（#62 は「楕円体」とは書いていない）。草稿の π/2 との違いを書く |
| III 節 弧の速さを c にする | 62:406「treating the arc-length speed of the helix as the speed of light … longitudinal velocity is c/2 … set aside」 | **食い違い**（#62 付録 C は検討して保留） |
| III 節 l.196 v_x = v_p sin θ が #1 の単振動 | 1:603–650「grad(T_e2 − T_e1) = E₀ sin θ」「produces a force F … simple harmonic motion」。1:650 u = −E₀ sin θ。66:615–623（輻射勾配＝核のエネルギーの微分の差） | **一致**（#1 の sin θ は速度の項 u）。読み役の一人は「コーパスは sin θ を力として読む」と指摘（7:829、51:328）。#1 は力 F を名前だけ出し、速度 u = −E₀ sin θ を式にしているので、草稿の読みは #1 と合う |
| III 節 l.198「赤線は往復で元に戻り、電子全体は動かない」 | ★66:374「The speed β_ZB c is not the speed of the electron as a whole; the electron may be at rest while the energy inside it is carried」。1:519 核は位置を変えない | **一致・要引用**（#66 l.374） |
| 同上（運動する電子） | 51:213「a net advance in x per half-cycle」、51:114・62:215「A→B→A′ with A′ ≠ A」、11 の尺取虫（A→B→C） | **食い違い（運動する電子の描き方）**：#51・#62・#11 は核そのものが前へ移る。草稿は核ごとホースを並進させる |
| 同上（核の固定） | 幹 T4:100–103（T4.4）「核固定は不可能である」（質量双極子の保存） | **不整合**（幹）：草稿は核の反跳を扱っていない |
| — | 1:718「do not have a definite surface」 | **注意**：ホースは物の表面ではなく、粒の通り道の面と断る必要がある |
| 草稿は photon sphere の語を使っていない | 66:352、51:357–361、65:248 | **要引用**：ホースと光子球の関係を一言で定める |

## C. 恒等式の層（#65・#66・#62・#1）

| 草稿の節と主張 | コーパスの該当箇所 | 判定 |
|---|---|---|
| IV 節 ψ_A = cos(θ/2)、ψ_B = sin(θ/2) を「occupation layer」の見出しで定義 | 65:294 三層＝amplitude（a, b）／occupation（n_A = a²）／energy（T_A = E₀n_A²）。README §0.3 | **食い違い（用語）**：ψ は #65 の振幅層。草稿は振幅層と占有層を一つの見出しにまとめている |
| IV 節「quartic layer」 | 65:294・759「energy layer」 | **食い違い（用語）** |
| IV 節「energy in flight」＝½sin²θ | 65:253・570「transit energy」、66:352「energy in transit」、62:82「momentum-carrying term」、1:330・11:199「kinetic energy of the virtual photon / photon sphere」 | **一致（中身）**、用語は揃える |
| IV 節 式 (4.3) 二乗した恒等式の三分割、#65 が幾何学的起源を与えた | 65:565–570、65:1337「quartic = Hopf pullback … No independent Stefan–Boltzmann assumption」 | **一致** |
| IV 節 重心 x̄ = −(d/2)cos θ | 65:859「D = (T_A − T_B)/E₀ = cos θ」。幹 T1:135（熱双極子＝質量双極子） | **一致・要引用**（#65 の D） |
| IV 節 E_flight/E₀ = ½(v_x/v_p)² | 65:859「the kinetic energy of the photon sphere is ½(dD/dθ)² = ½sin²θ」 | **要引用** |
| IV 節 l.248 赤線は ω、飛行中のエネルギーは 2ω | 66:640–648（T_A/E₀ = 3/8 + ½cos θ + ⅛cos 2θ、K/E₀ = ¼ − ¼cos 2θ）。65:1563–1571 | **一致・要引用**（#66 の周波数分解） |
| IV 節 二重被覆 | 65:608（(a, b) が戻るのは 4π） | 草稿は触れていない（範囲内で触れる必要は無い） |
| 位相原点 θ = 0 ＝核 A | 65:585・734 | **一致**（#1・#62 は θ = 0 を +x に置き、草稿は −d/2。向きの約束だけの違い） |
| Stefan–Boltzmann の T⁴ | 65:1348「We withdraw it」 | **一致**（草稿は持ち込んでいない） |

## D. 赤道の輪：ħ/2、μ_B、g = 2（#10・#11・#15・#48・#50）

| 草稿の節と主張 | コーパスの該当箇所 | 判定 |
|---|---|---|
| V 節 電荷 e が輪を回る円電流で μ、g = 2 は「電荷は全部回り、エネルギーは半分だけ回る」から | ★11:1021・10:134「This property could not be explained by theories based on circular currents」。★10:92「the image of a spinning top with precession in uniform circular motion has been discarded」。★11:107「rather than in circular motion. This overturned the concept …」。15:298 | **食い違い（最重要）**：#10・#11・#15 は円電流による説明をはっきり退けた。草稿 V 節はその説明そのもの |
| V 節 g = 2 の出どころ | 48 要旨「the Berry phase γ_intrinsic = π … geometrically necessitating g = 2」。10:163・15:193（ħ/2 は Thomas 歳差の倍角から） | **食い違い（経路）**：既発表の経路は Thomas 歳差（#10・#15）と Berry 位相（#48）。草稿は三本目の経路を出している。三本の関係が書かれていない |
| V 節 電荷が輪とともに回るという仮定 | 50:965「No circular force law and no pre-assigned charge are introduced」。Thermal Rays:458「cannot carry an oscillating charge dipole … leaves the centre of charge fixed」。幹 T4.2（電荷の双極子なら EDM で 20 桁） | **新**（根拠は無い）。電荷が粒とともに軸方向にも動くなら EDM と矛盾するので、「電荷の中心は動かない」かどうかの明記が要る |
| V 節 L = ħ/2、ħ は Hestenes の像と同型 | 11:1234（Hestenes の引用「circular motion … radius equal to the Compton wavelength × 1/2π」） | **要引用**（Hestenes の円運動と同型。どこが違うかを書く） |
| V 節 半分の ½ は交差項の最大値 | 50:472–478「E_ph ≤ ½E₀」。★51:331「bounded below by the floor E₀/2」 | **一致**（#50）／**食い違い**（#51 は ½E₀ を下限と書く。恒等式からは草稿の「最大」が正しい。#51 側の問題） |
| V 節 v_p = 0.05c で L・μ が 1/γ_p だけ小さい | 15:206–211 γ = 1 + a は「the maximum internal oscillation velocity」の γ | **注意**：γ_p を #15 の γ と同じものと読むと μ = μ_B/(1 + a) で、異常分と向きが逆になる。草稿の γ_p は #15 の γ ではないと断る必要がある |
| V 節 赤道で ħ/2 を全部出す | 幹 T3:127–137（T3.9）「軌道角運動量 0.127ħ … ħ/2 の約 3/4 は核の側」 | **不整合**（幹。速度の割り当てが逆であることの帰結） |

## E. 往復と振動数（#10・#62・#65・#66）

| 草稿の節と主張 | コーパスの該当箇所 | 判定 |
|---|---|---|
| VI 節 ν = v̄/λ_C、v̄ = (2/π)v_p（算術平均） | ★62:263「A simple-average treatment of \|sin θ\| would instead give 2/π ≈ 0.637 … neither equals the identity-intrinsic value 1/√2」。66:386–389（#62 の RMS）。51:220「effective RMS velocity」。10:256–261 式 III.5 | **食い違い（重要）**：コーパスは速さを二乗平均で読み、#62 は算術平均 2/π をはっきり退けた。草稿の「平均」は #62 が退けた量。草稿 X 節の「最大か平均か」には二乗平均が入っていない |
| VI 節 l.292「#66 は ZB 振動数を内部の速さ ÷ λ_C と書いた」 | 66:135・374、51:208、10:305–314 式 III.10（初出。ただし #10 は間隔 λ_C なので v/λ_C は片道の頻度）、22:119 | **一致・要引用**（#51 v3 も同じ式） |
| X 節 速さの値は扱わない | 62:85・260（2^{1/4} の食い違いを未解決として記帳）、65:2065「Origin of 1/√2」open | **要引用** |

## F. 特殊相対性理論（#10・#51・#2・Thermal Rays）

| 草稿の節と主張 | コーパスの該当箇所 | 判定 |
|---|---|---|
| VII 節 核の距離は静止長で、軸方向の運動で 1/Γ に縮む | ★51:215「Δx ∼ λ_C is a proper length … Δx_obs = Δx_proper/γ」 | **一致・要引用** |
| VII 節 電子全体の収縮（V は外から） | 10:181「bicycle wheel … length contraction … no Lorentz contraction occurs in the direction of the tangential spokes」。10:183・224・246（縮むのは内部の移送の速さによる回転の周） | **矛盾しない**（対象が別。#10 は内部の移送による周の縮み、草稿は電子全体の並進による縮み） |
| VII 節 横の半軸は不変 | 2:257「the Compton wavelength reduces … shortening of the radius of the virtual photon」 | **食い違い**（#2 は定性的な初期論文） |
| VII 節 ν_C の時計 → de Broglie の h/p | ★51:234「ν_C = m_ec²/h is the one de Broglie attached … It equals c/λ_C, the frequency that a carrier would have if it covered the round trip λ_C at the invariant speed」。Thermal Rays:277・296 | **要引用**（#51 v3）。#51 は ν_C を「往復 λ_C を c で回る」、草稿は「周 λ_C の輪を c で一周」と読む。〔レッドチームの指摘で訂正：初版は「数は同じ」。草稿の赤道の粒は c/γ_p で回るので、一周の刻みは ν_C/γ_p。第 3 稿では「光が周を一周する刻み」と書き直した〕 |
| VII 節 0.7712c で球、表 2 | 該当なし | **新** |
| VII 節 実験室の歩幅 | 幹 T4:236「(βγ/β_ZB)·λ_C」 | **一致**（形） |

## G. 一般相対性理論（#22・#51・#65・幹 T8）

| 草稿の節と主張 | コーパスの該当箇所 | 判定 |
|---|---|---|
| VIII 節 局所の長さと比は不変 | 幹 T8:79–89（T8.1）、T3:24。**22:197「v_{e,ZB} itself should therefore differ slightly depending on the gravitational context」、22:247「the true, proper-time-based ZB velocity is inherently slower in deeper gravitational potentials」** | **一致（幹）／食い違い（#22）**〔レッドチームの指摘で訂正：初版は「一致」〕。草稿は #22 の §3.2・§3.3 の主張を採らないので、そう明記する必要がある |
| VIII 節 係数 1 の時計の因子 | 幹 T8（核の距離が固有長のときだけ係数 1） | **一致**（草稿は静止長と明記している） |
| VIII 節 地表と GPS 軌道で 5.29×10⁻¹⁰、軌道の方が高い | 22:145・150・180・185 | **一致**（5.291 を再計算） |
| VIII 節 v_p の値に依らない | 22:156–174（比で速度が消える）。index §2「#22 は無傷」 | **一致** |
| VIII 節 #22 からの引き方 | 22:197・225「the intrinsic ZB velocity … should differ slightly depending on the gravitational context」。#22 は撤回済みの 0.040374c を含む（22:55 ほか） | **注意**：草稿は撤回部分を引いていない。#22 から取るのは時計の比の結果だけ、と断る必要がある。#22 は重力の項だけを計算している（軌道上の運動の項は入れていない） |
| VIII 節 | ★51:227「the predicted ZB oscillation frequency is lower at Earth's surface than at high altitude」。65:1496–1498 | **要引用**（#51 v3、#65 Sec. VII D） |

## H. 双曲幾何（#29・#62）

| 草稿の節と主張 | コーパスの該当箇所 | 判定 |
|---|---|---|
| IX 節「#29 は双曲平面の接続で位相を記述した」 | 29:87・111「presented as an intuitive prototype」「By drawing an analogy」。29:241「plane … spanned by the propagation direction and time」 | **食い違い（軽）**：#29 の双曲平面は類比で、平面は（伝播方向, 時間）。草稿の（軸, 半径）の実空間の半平面は新しい読み |
| IX 節 赤線 π・飛行中 2π が #29 の外 π・内 2π に一致 | 29:169・222（一致）。★62:319「the spinorial connection … accumulates 2π over a one-way traversal … that is the amplitude-level statement」 | **一致（数）／食い違い（層）**：#62 は #29 の内側の 2π を振幅層に割り当てる。草稿はエネルギー層（飛行中のエネルギー）に当てている |
| IX 節 核を理想点とする | 該当なし | **新** |

## I. 範囲と書式

| 項目 | コーパス・規約 | 判定 |
|---|---|---|
| X 節 螺旋の巻き方とカイラリティは範囲外 | 50:709・745（χ ≡ sign(da/dt)、h = χ·sign(p_x)）、65:2012 | **要引用**（#50 を名指し） |
| 引用は DOI が確定した論文だけ | 草稿の引用は #1・#10・#22・#29・#51 v3・#65・#66。DOI と年は index.md と一致（主の確認）。#51 は v3 の DOI 24521440（#62・#65・#66 が引くのは v2 の 20388056） | **一致** |
| 疑問文・読者案内・前方参照・GitHub の名前 | 草稿に無い（主の確認） | **一致**。レッドチームは本文の中の節への先送りの参照（「Sec. VII で」など）を前方参照として挙げたが、規約の前方参照は「未寄託の論文への参照」（index §0、2026-11-13 著者決定）を指すので、違反ではないと判断した。節の道案内を減らすかどうかは著者判断 |
| 0.040374c | 草稿に無い | **一致** |
| 番号 | ★65:2463「\bibitem{ref:p67} … The 0-Sphere Model: A Structural Overview, Zenodo (2026), in preparation」（寄託済みの #65 の中） | **食い違い（事務）**：寄託済みの #65 が「#67 ＝構造総説」と書いている。新 #67 と番号がぶつかる |
| 検算スクリプト | `verify67.py` は NumPy 1.x で最終行が止まっていた（`np.trapezoid`）。直した。本文の「standard Python libraries」は NumPy を使うので不正確 | **直した** |

---

## 照合の後で見つかった食い違い（レッドチームによる）

| 草稿の節と主張 | コーパスの該当箇所 | 判定 |
|---|---|---|
| I・III 節 エネルギーの要素は c で動き、遅いのは軸への射影だけ | 66:103「the group velocity of the internal carrier, which it sets to c/n」、66:493「The energy travels with the envelope」 | **食い違い（重大。照合表の見落とし）**：#66 は遅さを内部の媒質の屈折率で説明し、草稿は経路の幾何で説明する。#66 を 7 か所で引きながら、この置き換えを書いていない |
| II 節 d = πƛ_C | 51:385–399（非対蹠性から熱測地線の一意性。r ∼ λ_C） | **食い違い（構造）**：r = ƛ_C と読むと Bonnet–Myers の評価が等号になり、核は対蹠点になる |
| III 節 極で φ̇ → ∞（巻き数が対数で発散） | 62:319「the relevant internal winding number … is unity」 | **食い違い** |
| II 節 軸方向の「両端を閉じた管・固定端の弦」 | 1:372「A bare electron is a perfect blackbody」 | **食い違い**：定在波の節には反射端が要る。完全な吸収体の端では定在波が立たない |
| V 節 回るエネルギーを交差項に置く | 65:859「at this layer nothing circulates」 | **食い違い** |
| 第 2 稿 l.130「一つの光子ではない」 | 65:248「a captured photon, the photon sphere」 | **食い違い**（改めたと書いていない） |

## 要約

1. **d = λ_C/2 は、寄託済みの #51 v3（l.208）と #66（l.352）に記述があるが、どこにも導出は無い。** 草稿の導出（一つの光子を往復で一度持つ）は新しい。#1・#2・#10・寄託済みの #65 の本文では距離は λ_C。横の半径 ƛ_C と d = πƛ_C は新しい。
2. **草稿は、既発表の論文の三つの立場を改めているのに、それを書いていない。** (i) #51・#50 の速さの割り当て（横 0.04c・縦 ∼c）を逆にしている。(ii) #50・#51 の「回転は内部の位相空間にあり、実空間の軌道ではない」に反して、実空間の面に載せている。(iii) #10・#11・#15 が退けた円電流で g = 2 を出している（既発表の経路は Thomas 歳差と #48 の Berry 位相）。
3. **振動数の式の「平均」は、#62 がはっきり退けた算術平均 2/π である。** コーパスは二乗平均で読む。
4. **一致して引用を足すべき箇所が多い。** #51 v3（λ_C/2、静止長の収縮、ν_C ＝ de Broglie の時計、重力の時計）、#62（回転楕円体の上の螺旋、交差項＝運動量を運ぶ項）、#65（D = cos θ、三層の用語）、#66（電子全体は静止してよい、周波数分解）。
5. **幹との不整合は二つ。** 核の固定（T4.4 の定理）と、E₀ の層の一択（T1 の K4、T3 §4 の著者撤回）。
