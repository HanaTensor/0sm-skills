# 依頼：0SM コーパスの再改番（#67〜#71 → #68〜#72）と #67 の空け（2026-11-27）

リポジトリ `HanaTensor/0sm-skills` のローカルの clone（`~/Desktop/Claude Code/0sm-skills`）で作業してください。目的は、未寄託の原稿五本の番号を一つずつ後ろへずらし、**#67 を新しい論文のために空ける**ことです。

## 0. 現状（2026-11-27 17:47 に確認済み）

- いまいるブランチは `renumber-2026-11-13` で、`origin/renumber-2026-11-13` と一致しています（ずれ 0）。`main` にはまだマージしていない 33 コミットがあります。**`main` ではなく、このブランチを土台にしてください。**
- `translations-ja/README.md` に、別のセッションの未コミットの変更（4 行の追加）があります。**触らないでください。** stash もしないでください。
- `.git` に錠（`*.lock`）は残っていません。
- 寄託済みの **#66**（亜光速 ZB、DOI 10.5281/zenodo.23750210）は動かしません。

| 現在 | 論文 | 状態 | 移動先 |
|---|---|---|---|
| #67 | From Thermal Rays to Matter Waves（Hamilton の類比、位相と群の屈折率、Schrödinger の包絡線） | 第 3 稿、寄託用の一式あり（`HANDOFF.md`、`readme.txt`、`verify67.py`、`zenodo_description.html`） | **#68** |
| #68 | Why the 0-Sphere Electron Begins at the Quadrupole | 未寄託（`verify68.py`） | **#69** |
| #69 | Three Tests of the Weak Equivalence Principle（旧 #66、旧 #68） | 未寄託（`REVISION-MEMO.md`、`verify69.py`） | **#70** |
| #70 | A Five-Term Chain from the Energy Identity（核子） | 未寄託（`main.pdf`、`fig_five_terms.png`、`verify70.py`） | **#71** |
| #71 | The 0-Sphere Model: A Structural Overview | 未寄託（`verify71.py`） | **#72** |
| （空き）#67 | 新しい論文：回転楕円体のホース（2026-11-27 の壁練の成果。仮題は下の §4） | 起草中 | — |

## 守ること（このリポジトリの規約。`~/Desktop/Claude Code/CLAUDE.md` も先に読むこと）

- `git add -A` と `git add .` は使わない。追加するファイルは NFC に正規化した名前で明示して渡す。
- 錠が残っていても許可なく消さない。消すときは CLAUDE.md §2 の手順に従う。
- **commit と push は、私が求めたときだけ行う。** 作業はいまのブランチから `renumber-2026-11-27` を切ってから始める。
- 書き換えは、**一覧を私に見せて承認を得てから**行う。いきなり置換しない。

## 1. 事前確認

1. `find .git -name "*.lock"` と `git status` で、上の「現状」と一致することを確かめる。違っていたら報告して止まる。
2. ブランチ `renumber-2026-11-27` を切る。

## 2. 参照の棚卸し（書き換えの前に必ず）

次のパターンでリポジトリ全体を検索し、**ファイル・行番号・前後の文脈・判定**を表にして見せてください。

- `#67`〜`#72`、`#067`〜`#072`、`\#67`〜`\#72`、`Paper~\#67` など、`Paper #67` など
- `tex-sources/67`〜`tex-sources/71`、`verify67.py`〜`verify71.py`、ファイル名やディレクトリ名に含まれる番号
- bib のキー、`zenodo_description.html`・`readme.txt` の中の番号
- 日本語の文中の言及（「#67 の」「総説 #71」など）

判定は三つに分けてください。

| 判定 | 意味 |
|---|---|
| 書き換える | 現行の文書（`index.md`、`wall-practice-index.md`、現行版の幹、handouts、`skill-updates/`、`tex-sources/67`〜`71` の中身）で、上の表の論文を指しているもの |
| 書き換えない（誤検出） | DOI の数字、式番号、行番号、年号、数値、O 番号・K 番号の一部など、論文番号ではないもの |
| 著者判断 | 履歴として残している文書（`archive/` 配下、日付つきの旧版の幹、`SESSION-*.md`・`HANDOFF*.md` などの作業記録、tex の冒頭にある「renumbered from …」の改番履歴のコメント）。原則は**書き換えない**が、一覧に挙げて判断を仰ぐ |

**注意**：寄託済みの #65（DOI 10.5281/zenodo.23257458）は、等価原理の論文を作業時の番号「#66」で引用しています。これは寄託済みの論文の中の記述なので、変えられません。現 #69 の冒頭のコメントにその説明があります。このコメントは残し、番号の部分だけ新しい番号に合わせるかどうかを判断に挙げてください。

## 3. 書き換え（承認後）

二重にずれるのを防ぐため、**後ろから順に**、仮の札を経由して置き換えてください。

1. ディレクトリの移動（この順）：
   - `git mv tex-sources/71 tex-sources/72`
   - `git mv tex-sources/70 tex-sources/71`
   - `git mv tex-sources/69 tex-sources/70`
   - `git mv tex-sources/68 tex-sources/69`
   - `git mv tex-sources/67 tex-sources/68`

   各ディレクトリの中の `verifyNN.py` も新しい番号に `git mv` する。
2. 本文の置換：旧 #71 → `@@P72@@`、旧 #70 → `@@P71@@`、旧 #69 → `@@P70@@`、旧 #68 → `@@P69@@`、旧 #67 → `@@P68@@` の順に札へ置き換える。最後に札を正式な表記（`#72` や、各ファイルの書式に合わせた `\#72` など）に戻す。
3. 各 tex の冒頭のコメントに「(renumbered from #NN on 2026-11-27)」を足し、本文中の自己言及を直す。
4. 旧 #67（新 #68）の寄託用の一式（`readme.txt`、`zenodo_description.html`、`HANDOFF.md` の番号の段）を直す。`HANDOFF.md` は作業記録なので、本文の履歴は残し、冒頭の「番号」の行だけを新しくする案を見せる。
5. `wall-practice-index.md` の冒頭の改番の段に「2026-11-27 再改番」の一行を足し、「番号と状態」を直す。skill の正本 `skill-updates/0sm-wall-practice-SKILL.md` の §7 の番号の記述も直す。
6. index の「番号と状態」に、**#67 ＝ 起草中（回転楕円体のホース。2026-11-27 の壁練の成果）**の一行を加える。文言は案を見せて承認を得ること。

## 4. 新 #67 について（参考。index の一行の案に使う）

- 仮題：*The Spheroidal Hose: A Kinematic Picture of the 0-Sphere Electron Consistent with Special and General Relativity*
- 内容：A–B の距離 d = λ_C/2 と赤道の輪の半径 ƛ_C を同じ一個の光子（E₀ をすべて変えた光子、波長 λ_C）から決め、x への射影が #1 の単振動になる回転楕円体のホースを描く。恒等式、赤道の輪（ħ/2、g = 2）、光時計、特殊相対性理論の収縮、一般相対性理論の刻みとの整合までに範囲を絞る。予言値の読み方には立ち入らない。
- 寄託の順は #67 → #72 を予定。

## 5. 書き換えの後の確認

1. §2 と同じ検索をもう一度かけ、旧い意味の番号が現行の文書に残っていないことを確かめる（「著者判断」で残すと決めたものを除く）。
2. `tectonic` で `tex-sources/68`〜`72` の `main.tex` をコンパイルし、エラーが 0 であることを確かめる。そのうえで、**PDF のページを目で見て**、表や参照が崩れていないことを確認する。
3. 各 `verifyNN.py` が新しい名前で動くことを確かめる。
4. `git diff --stat` と、変更したファイルの一覧を報告する。

## 6. 報告

次の四つをまとめて報告し、commit の指示を待ってください。

- 書き換えたファイルと箇所の数
- 「著者判断」として残したものの一覧
- コンパイル、目視、`verify` の結果
- 錠が残っていないこと（`find .git -name "*.lock"` の結果）
