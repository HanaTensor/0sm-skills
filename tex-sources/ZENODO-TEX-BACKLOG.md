# Zenodo tex 追補チェックリスト(2026-07-19 作成)

> 目的: 各 Zenodo レコードに LaTeX ソース(main.tex)を追補し、後続研究者の再現と AI 可読性を確保する。
> 全 32 件が清書・コンパイル検証済み(2026-07-19)で品質統一されている。アップロードするファイルは常に `https://raw.githubusercontent.com/HanaTensor/0sm-skills/main/tex-sources/NN/main.tex`(= 本 repo の清書版)。

## 手順メモ(User 手作業・Web UI)

1. 対象レコードを開く → **New version** を作成(公開済みレコードへの直接ファイル追加は不可)。
2. main.tex を追加(既存 PDF 等は引き継がれる)。メタデータは変更不要。
3. Publish。**version DOI は新しく発番される**が concept DOI は不変。repo の `doi-canonical.md` / `index.md` が version DOI を指している論文は、新 version DOI へ更新するか従来 DOI のままにするか方針を決めてから着手する(全 32 件で同じ扱いに統一すること)。

## 対象 32 レコード(tex 未収録)

| 済 | # | Zenodo record | 清書版の状態 |
|---|---|---|---|
| ☐ | 1 | [zenodo.org/records/16759284](https://zenodo.org/records/16759284) | 2026-07-19 スキル清書・コンパイル検証済み |
| ☐ | 2 | [zenodo.org/records/16783727](https://zenodo.org/records/16783727) | 2026-07-19 スキル清書・コンパイル検証済み |
| ☐ | 3 | [zenodo.org/records/17759634](https://zenodo.org/records/17759634) | 2026-07-19 スキル清書・コンパイル検証済み |
| ☐ | 4 | [zenodo.org/records/17759699](https://zenodo.org/records/17759699) | 2026-07-19 スキル清書・コンパイル検証済み |
| ☐ | 5 | [zenodo.org/records/17759726](https://zenodo.org/records/17759726) | 2026-07-19 スキル清書・コンパイル検証済み |
| ☐ | 6 | [zenodo.org/records/17759908](https://zenodo.org/records/17759908) | 2026-07-19 スキル清書・コンパイル検証済み |
| ☐ | 7 | [zenodo.org/records/17760132](https://zenodo.org/records/17760132) | 2026-07-19 スキル清書・コンパイル検証済み |
| ☐ | 8 | [zenodo.org/records/17760445](https://zenodo.org/records/17760445) | 2026-07-19 スキル清書・コンパイル検証済み |
| ☐ | 9 | [zenodo.org/records/17764952](https://zenodo.org/records/17764952) | 2026-07-19 スキル清書・コンパイル検証済み |
| ☐ | 10 | [zenodo.org/records/17764997](https://zenodo.org/records/17764997) | 2026-07-19 スキル清書・コンパイル検証済み |
| ☐ | 11 | [zenodo.org/records/17765017](https://zenodo.org/records/17765017) | 2026-07-19 スキル清書・コンパイル検証済み |
| ☐ | 12 | [zenodo.org/records/17765039](https://zenodo.org/records/17765039) | 2026-07-19 スキル清書・コンパイル検証済み |
| ☐ | 13 | [zenodo.org/records/17765079](https://zenodo.org/records/17765079) | 2026-07-19 スキル清書・コンパイル検証済み |
| ☐ | 14 | [zenodo.org/records/17765097](https://zenodo.org/records/17765097) | 2026-07-19 スキル清書・コンパイル検証済み |
| ☐ | 15 | [zenodo.org/records/17765121](https://zenodo.org/records/17765121) | 2026-07-19 規約統一・コンパイル検証済み |
| ☐ | 17 | [zenodo.org/records/17765136](https://zenodo.org/records/17765136) | 2026-07-19 規約統一・コンパイル検証済み |
| ☐ | 18 | [zenodo.org/records/17765200](https://zenodo.org/records/17765200) | 2026-07-19 規約統一・コンパイル検証済み |
| ☐ | 19 | [zenodo.org/records/17765238](https://zenodo.org/records/17765238) | 2026-07-19 規約統一・コンパイル検証済み |
| ☐ | 20 | [zenodo.org/records/17765244](https://zenodo.org/records/17765244) | 2026-07-19 規約統一・コンパイル検証済み |
| ☐ | 21 | [zenodo.org/records/17765305](https://zenodo.org/records/17765305) | 2026-07-19 規約統一・コンパイル検証済み |
| ☐ | 22 | [zenodo.org/records/17765318](https://zenodo.org/records/17765318) | 2026-07-19 規約統一・コンパイル検証済み |
| ☐ | 23 | [zenodo.org/records/17765336](https://zenodo.org/records/17765336) | 2026-07-19 規約統一・コンパイル検証済み |
| ☐ | 24 | [zenodo.org/records/17765349](https://zenodo.org/records/17765349) | 2026-07-19 規約統一・コンパイル検証済み |
| ☐ | 25 | [zenodo.org/records/18064535](https://zenodo.org/records/18064535) | 2026-07-19 規約統一・コンパイル検証済み |
| ☐ | 26 | [zenodo.org/records/17765409](https://zenodo.org/records/17765409) | 2026-07-19 規約統一・コンパイル検証済み |
| ☐ | 27 | [zenodo.org/records/17765439](https://zenodo.org/records/17765439) | 2026-07-19 規約統一・コンパイル検証済み |
| ☐ | 29 | [zenodo.org/records/18067760](https://zenodo.org/records/18067760) | 2026-07-19 規約統一・コンパイル検証済み |
| ☐ | 31 | [zenodo.org/records/18203433](https://zenodo.org/records/18203433) | 2026-07-19 規約統一・コンパイル検証済み |
| ☐ | 32 | [zenodo.org/records/18275142](https://zenodo.org/records/18275142) | 2026-07-19 規約統一・コンパイル検証済み |
| ☐ | 33 | [zenodo.org/records/18356895](https://zenodo.org/records/18356895) | 2026-07-19 規約統一・コンパイル検証済み。**3 ファイル同梱**: [main.tex](https://raw.githubusercontent.com/HanaTensor/0sm-skills/main/tex-sources/33/main.tex) + [fig_thermal.tex](https://raw.githubusercontent.com/HanaTensor/0sm-skills/main/tex-sources/33/fig_thermal.tex) + [fig_TotalHamiltonian.tex](https://raw.githubusercontent.com/HanaTensor/0sm-skills/main/tex-sources/33/fig_TotalHamiltonian.tex)(main.tex が \input 参照。いずれも英訳清書済み・組合せでコンパイル検証済み) |
| ☐ | 49 | [zenodo.org/records/19393391](https://zenodo.org/records/19393391) | 2026-07-19 スキル清書・コンパイル検証済み |
| ☐ | 63 | [zenodo.org/records/20767589](https://zenodo.org/records/20767589) | 2026-07-19 スキル清書・コンパイル検証済み |

## 複数ファイル論文の注意

- `\input` 依存があるのは全 64 論文中 **#33 のみ**(2026-07-19 全数掃引で確認)。他は main.tex 単体で完結。

## 対象外

- tex 収録済み(31 レコード): #28, #30, #34–48, #50–62, #64(2026-07-19 API 照合で確認)
- 旧 #67(99-1 Research Summary)は 2026-07-19 廃棄(コーパスと全面重複のため)
