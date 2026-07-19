# Zenodo tex 追補チェックリスト(2026-07-19 作成)

> 目的: 各 Zenodo レコードに LaTeX ソース(main.tex)を追補し、後続研究者の再現と AI 可読性を確保する。
> アップロードするファイルは常に `https://raw.githubusercontent.com/HanaTensor/0sm-skills/main/tex-sources/NN/main.tex`(= 本 repo の清書版)。

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
| ☐ | 13 | [zenodo.org/records/17765079](https://zenodo.org/records/17765079) | ⚠ 現 main.tex は Overleaf 版と実質同一(清書し直し推奨) |
| ☐ | 14 | [zenodo.org/records/17765097](https://zenodo.org/records/17765097) | ⚠ 現 main.tex は Overleaf 版と実質同一(清書し直し推奨) |
| ☐ | 15 | [zenodo.org/records/17765121](https://zenodo.org/records/17765121) | 既存清書版(過去セッション生成・Zenodo 未収録) |
| ☐ | 17 | [zenodo.org/records/17765136](https://zenodo.org/records/17765136) | 既存清書版(過去セッション生成・Zenodo 未収録) |
| ☐ | 18 | [zenodo.org/records/17765200](https://zenodo.org/records/17765200) | 既存清書版(過去セッション生成・Zenodo 未収録) |
| ☐ | 19 | [zenodo.org/records/17765238](https://zenodo.org/records/17765238) | 既存清書版(過去セッション生成・Zenodo 未収録) |
| ☐ | 20 | [zenodo.org/records/17765244](https://zenodo.org/records/17765244) | 既存清書版(過去セッション生成・Zenodo 未収録) |
| ☐ | 21 | [zenodo.org/records/17765305](https://zenodo.org/records/17765305) | 既存清書版(過去セッション生成・Zenodo 未収録) |
| ☐ | 22 | [zenodo.org/records/17765318](https://zenodo.org/records/17765318) | 既存清書版(過去セッション生成・Zenodo 未収録) |
| ☐ | 23 | [zenodo.org/records/17765336](https://zenodo.org/records/17765336) | 既存清書版(過去セッション生成・Zenodo 未収録) |
| ☐ | 24 | [zenodo.org/records/17765349](https://zenodo.org/records/17765349) | 既存清書版(過去セッション生成・Zenodo 未収録) |
| ☐ | 25 | [zenodo.org/records/18064535](https://zenodo.org/records/18064535) | 既存清書版(過去セッション生成・Zenodo 未収録) |
| ☐ | 26 | [zenodo.org/records/17765409](https://zenodo.org/records/17765409) | 既存清書版(過去セッション生成・Zenodo 未収録) |
| ☐ | 27 | [zenodo.org/records/17765439](https://zenodo.org/records/17765439) | 既存清書版(過去セッション生成・Zenodo 未収録) |
| ☐ | 29 | [zenodo.org/records/18067760](https://zenodo.org/records/18067760) | 既存清書版(過去セッション生成・Zenodo 未収録) |
| ☐ | 31 | [zenodo.org/records/18203433](https://zenodo.org/records/18203433) | 既存清書版(過去セッション生成・Zenodo 未収録) |
| ☐ | 32 | [zenodo.org/records/18275142](https://zenodo.org/records/18275142) | 既存清書版(過去セッション生成・Zenodo 未収録) |
| ☐ | 33 | [zenodo.org/records/18356895](https://zenodo.org/records/18356895) | 既存清書版(過去セッション生成・Zenodo 未収録) |
| ☐ | 49 | [zenodo.org/records/19393391](https://zenodo.org/records/19393391) | ⚠ 現 main.tex は Overleaf 版と実質同一(清書し直し推奨) |
| ☐ | 63 | [zenodo.org/records/20767589](https://zenodo.org/records/20767589) | 2026-07-19 スキル清書・コンパイル検証済み |

## 対象外

- tex 収録済み(31 レコード): #28, #30, #34–48, #50–62, #64(2026-07-19 API 照合で確認)
- #67: Zenodo 未公開(清書版 main.tex は repo に準備済み。公開時は本チェックリスト同様に tex 同梱で)
