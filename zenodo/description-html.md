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

---

## 3. 必須セクション構成

以下の順序で記述する：

```
[1] 導入段落        <p> — 論文の主張を1〜2文で
[2] Core Result     コア方程式を <blockquote><code> で表示
[3] Key Contributions  <ul><li> で箇条書き（4〜6項目）
[4] シリーズ内位置づけ  先行論文へのDOIリンク付き説明
[5] 主要参照論文テーブル  <table> で通番・タイトル・DOIリンクを一覧
[6] Series Context  シリーズ全体へのZenodo検索リンク
```

---

## 4. 記述規則

### 数式変換表

| LaTeX | HTML |
|-------|------|
| `\gamma_L` | `γ<sub>L</sub>` |
| `\Delta[L]` | `Δ[L]` |
| `\approx` | `≈` |
| `v_{\text{ZB}}` | `<em>v</em><sub>ZB</sub>` |
| `a_e` | `<em>a</em><sub>e</sub>` |
| `a_e^{\text{exp}}` | `<em>a</em><sub>e</sub><sub>(exp)</sub>` |
| `2\pi r` | `2π<em>r</em>` |
| `\times` | `×` |
| `\sin(2\omega t)` | `sin(2ωt)` |
| `\Omega` | `Ω` |
| `\propto` | `∝` |

### コア方程式ブロック

```html
<blockquote>
<code>[数式をASCII/Unicode混在で記述]</code>
</blockquote>
```

### 主要参照テーブルの標準構造

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

### Series Contextの固定フォーマット（末尾）

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

## 5. タグ検証チェック（納品前必須）

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

## 6. ファイル納品

```
ファイル名: zenodo_description_[paper_number].html
           （例: zenodo_description_47.html）
用途: Zenodo登録画面のDescription欄に全文コピペ
注意: ファイル自体はZenodoにアップロードしない
```

---

*Last updated: 2026-03-22 | See also: `zenodo/WORKFLOW.md`*
