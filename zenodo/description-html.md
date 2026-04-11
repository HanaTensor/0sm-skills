# Zenodo Description HTML Standard

> File: `zenodo/description-html.md` | Repository: `HanaTensor/0sm-skills`
> 用途：ZenodoのDescription欄に記述するHTMLの作成標準。LLMクローラーおよびZenodo検索エンジン向けに最適化。

---

## 1. 概要と位置づけ

ZenodoのDescription欄はHTML入力に対応しており、LLMクローラーおよびZenodo検索エンジンが本文テキストとして取得する。プレーンテキストの羅列よりも、**見出し・リスト・テーブル・リンクを組み合わせたHTML**を記述することで、可読性と被発見性の両方が向上する。

作業フローでの位置づけ：Step 3（zenodo_relations.txt）完了後、Step 4ファイル納品の前に作成する。

---

## 2. Zenodo許可タグ一覧

Zenodoのdescriptionフィールドに使用できるHTMLタグは以下に限定される。

```
a, abbr, acronym, b, blockquote, br, code, caption,
div, em, i, li, ol, p, pre, span, strike, strong,
sub, table, caption, tbody, thead, th, td, tr, u, ul
```

**注意：**
- `<sup>` は許可リストに含まれない。上付き文字は `<sub>` の代替表現（例: `a<sub>(exp)</sub>`）またはUnicode文字（例: `²`）を用いる。
- `h1`〜`h4`、`style`、`script` 等は使用不可。
- 見出しは `<p><b>— [見出し] —</b></p>` 形式で代替する。
- **`style` 属性はZenodoのサニタイザーにより除去される。** タグに `style="..."` を付与しても無効となるため、インラインスタイルで色・フォント等を制御することはできない。色制御を前提とした回避策（例: `color:inherit`）は機能しない。

---

## 3. 必須セクション構成

以下の順序で記述する：

```
[1] 導入段落          <p> — 論文の主張を1〜2文で
[2] Core Equations    コア方程式を <p><b>ラベル</b><br>Unicode数式 で表示
[3] Key Contributions <ul><li> で箇条書き（4〜6項目）
[4] シリーズ内位置づけ  先行論文へのDOIリンク付き説明
[5] 主要参照論文テーブル  <table> で通番・タイトル・DOIリンクを一覧
[6] Series Context    シリーズ全体へのZenodo検索リンク
```

---

## 4. 数式表示ルール

### ZenodoにおけるMathJax・LaTeX数式レンダリングの可否

**結論：現在のZenodo（InvenioRDM、2023年10月〜）では、MathJax・LaTeX数式レンダリングはDescription欄で使用できない。**

| 手段 | 可否 | 理由 |
|------|------|------|
| `$$...$$` / `\(...\)` デリミタ | ✗ | MathJaxがページに読み込まれていない |
| MathMLタグ `<math>`, `<mrow>` | ✗ | Zenodo許可タグリスト外のためstrip |
| `<img src="...">` で数式画像埋め込み | ✗ | `<img>` タグが許可タグ外 |
| `<script>` でMathJaxを外部ロード | ✗ | `<script>` タグが許可タグ外、かつ `style` 属性もstrip |
| **Unicode文字 + `<sub>` / `<em>` / `<b>`** | **✓** | **現状の唯一の実用手段** |

> **補足：旧Zenodoとの違い**
> 旧Zenodo（〜2023年10月）はCKEditorにMathJaxプラグインを組み込んでおり（`window.CKEDITOR.config.mathJaxLib`）、`$$...$$` による数式レンダリングが可能だった。InvenioRDMへの移行後、この機能は引き継がれていない。

### 禁止：`<blockquote><code>` による数式ブロック

Zenodoのエディタでは `<blockquote><code>` はグレー反転背景・等幅フォントでレンダリングされ、視認性が著しく低下する。数式ブロックへの使用を禁止する。

```html
<!-- 禁止 -->
<blockquote><code>E_0 = cos^4(theta/2) + sin^4(theta/2) + (1/2)sin^2(theta)</code></blockquote>
```

### 推奨：`<p>` + `<b>ラベル</b>` + `<br>` + Unicode数式

各数式を独立した `<p>` ブロックとし、太字ラベルで識別する。数式本体はUnicode文字と `<sub>` / `<em>` を用いてインライン表記する。

```html
<!-- 推奨 -->
<p>
<b>Hamiltonian identity</b> (Paper #1):<br>
<em>E</em><sub>0</sub> = <em>E</em><sub>0</sub> cos⁴(θ/2) + <em>E</em><sub>0</sub> sin⁴(θ/2) + (<em>E</em><sub>0</sub>/2) sin²θ
</p>
```

`<code>` タグはファイル名等の非数式用途（例: `<code>zenodo_XXXXXXX_guide.docx</code>`）には引き続き使用可。

### 擬似コード・複数行アルゴリズム表記：`<pre>` を使用

数式ではなく複数行の擬似コード・変数定義ブロック（例: `x(τ) = ...` 形式の記述）を表示したい場合は `<pre>` タグを使用する。

```html
<!-- 擬似コード・複数行ブロック -->
<pre>x(τ) = v_pitch · τ,  y(τ) = cos(ω_ZB τ),  z(τ) = sin(ω_ZB τ)
v_ZB ≈ 0.04c   (transverse)
v_pitch ∼ c    (longitudinal)</pre>
```

**`<pre>` 使用上の注意：**

- `<pre>` はZenodo許可タグであり、等幅フォント・改行保持でレンダリングされる。
- **`style` 属性はZenodoにより除去されるため `<pre style="color:inherit">` 等は無効。** インラインスタイルで文字色を制御することはできない。
- **ピンク色問題の根本原因：** `<blockquote><code>` を使用した場合、ZenodoのCSSテーマが `<code>` タグにピンク（マゼンタ系）の文字色を付与するために発生する。`<pre>` 単体ではこの問題は生じない。
- **`<pre><code>…</code></pre>` の組み合わせも禁止。** `<pre>` の子要素として `<code>` を入れると、`<code>` へのテーマ着色が再発する可能性がある。複数行ブロックは `<pre>…</pre>` のみで記述すること。

---

## 5. LaTeX → HTML 数式変換表

### 5.1 記号対照表（LaTeX → HTML）

| LaTeX | HTML |
|-------|------|
| `\gamma_L` | `γ<sub>L</sub>` |
| `\Delta L` | `Δ<em>L</em>` |
| `\approx` | `≈` |
| `v_{\text{ZB}}` | `<em>v</em><sub>ZB</sub>` |
| `a_e` | `<em>a</em><sub>e</sub>` |
| `a_e^{\text{exp}}` | `<em>a</em><sub>e(exp)</sub>` |
| `2\pi r` | `2π<em>r</em>` |
| `\times` | `×` |
| `\sin(2\omega t)` | `sin(2ωt)` |
| `\Omega` | `Ω` |
| `\propto` | `∝` |
| `\cos^4(\theta/2)` | `cos⁴(θ/2)` |
| `\sin^2\theta` | `sin²θ` |
| `\hbar\omega` | `ℏω` |
| `\geq` | `≥` |
| `\neq` | `≠` |
| `\leq` | `≤` |
| `\to` | `→` |
| `\leftrightarrow` | `↔` |
| `n \to n-1` | `<em>n</em> → <em>n</em>−1` |

### 5.2 物理数式向けUnicode対照表

| 記号 | Unicode | 用途例 |
|------|---------|--------|
| `⁴` | U+2074 | cos⁴, sin⁴ |
| `²` | U+00B2 | v², c² |
| `√` | U+221A | √(1 − v²/c²) |
| `θ` | U+03B8 | internal phase |
| `π` | U+03C0 | periodicity |
| `ω` | U+03C9 | angular frequency |
| `Ω` | U+03A9 | Thomas angular velocity |
| `γ` | U+03B3 | Lorentz factor |
| `Δ` | U+0394 | difference |
| `ℏ` | U+210F | reduced Planck constant |
| `→` | U+2192 | implication / cascade |
| `↔` | U+2194 | equivalence |
| `≥` | U+2265 | floor inequality |
| `≤` | U+2264 | upper bound |
| `≈` | U+2248 | approximate equality |
| `≠` | U+2260 | not equal |
| `−` | U+2212 | minus (not hyphen) |
| `×` | U+00D7 | multiplication |
| `∝` | U+221D | proportional to |
| `∞` | U+221E | infinity |

---

## 6. 固定テンプレート

### 主要参照テーブル

```html
<table>
  <thead>
    <tr><th>#</th><th>Title (abbreviated)</th><th>DOI</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>[通番]</td>
      <td>[タイトル略記]</td>
      <td><a href="https://doi.org/10.5281/zenodo.[ID]">10.5281/zenodo.[ID]</a></td>
    </tr>
  </tbody>
</table>
```

### Series Context（末尾固定）

```html
<p>
The 0-Sphere Model is an ongoing research programme (2018–present) that derives
spin, anomalous magnetic moment, Zitterbewegung, and emergent spacetime from the
geometry and thermodynamics of a two-kernel electron model.
All papers in the series are archived on Zenodo:
</p>
<p>
<a href="https://zenodo.org/search?q=metadata.creators.person_or_org.name%3A%22Hanamura%2C+Satoshi%22">Zenodo search: Hanamura, Satoshi</a>
</p>
```

---

## 7. タグ検証チェック（納品前必須）

作成後、以下のPythonスニペットで許可タグ外のタグが含まれていないか確認する：

```python
from html.parser import HTMLParser

class Validator(HTMLParser):
    ALLOWED = {'a','abbr','acronym','b','blockquote','br','code','caption',
               'div','em','i','li','ol','p','pre','span','strike','strong',
               'sub','table','tbody','thead','th','td','tr','u','ul'}
    def __init__(self):
        super().__init__()
        self.errors = []
    def handle_starttag(self, tag, attrs):
        if tag not in self.ALLOWED:
            self.errors.append(f'DISALLOWED TAG: <{tag}>')

v = Validator()
with open('zenodo_description_[N].html') as f:
    v.feed(f.read())
if v.errors:
    for e in v.errors: print(e)
else:
    print('OK — all tags within Zenodo allowed set')
```

---

## 8. ファイル納品

```
ファイル名: zenodo_description_[paper_number].html
           （例: zenodo_description_49.html）
用途: Zenodo登録画面のDescription欄に全文コピペ
注意: ファイル自体はZenodoにアップロードしない
```

---

*Last updated: 2026-04-12 | See also: `zenodo/WORKFLOW.md`*
