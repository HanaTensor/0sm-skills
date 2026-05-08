**部分的に違います**。重要な訂正があります: **解凍は User 側ではなく Claude 側で行います**。

## 訂正された workflow

```
[Github upload 時]
  ✓ 圧縮された .tar.gz を upload (912 KB)

[利用時: 新規チャットで作業開始]
  ✗ User 側で解凍する必要なし ← ここが訂正点
  ✓ .tar.gz をそのまま download → そのまま新 chat に upload
  ✓ Claude が sandbox 内で `tar xzf` で自動展開して使用
```

## 比較: 誤った理解 vs 正しい workflow

| Step | ご認識 (要訂正) | 正しい flow |
|---|---|---|
| 1 | GitHub に `.tar.gz` upload | **同じ** |
| 2 | GitHub から `.tar.gz` download | **同じ** |
| 3 | Local で **解凍** (`tar xzf` または Finder double-click) | **解凍しない** ─ `.tar.gz` のまま保持 |
| 4 | 解凍された folder を新 chat に upload | `.tar.gz` を **そのまま 新 chat に upload** (1 file) |
| 5 | Claude が files を直接 read | Claude が **sandbox 内で `tar xzf` 実行 → 展開 → read** |

## なぜ User 側で解凍してはいけないか

### Reason 1: Chat upload の practical 制約

`.tar.gz` を解凍すると `136 files` (60 paper files + 30 topic layer files + 4 query files + 8 derived files + scripts + HANDOFF.md) になります。これら全部を新 chat に upload するのは:

- Claude.ai の chat input は file drag-drop 可能だが、**136 files の同時 upload は impractical** (UI 制約 + transfer time)
- Folder structure が flat 化される可能性 (chat input が directory 階層を保持しない場合)
- Single file upload (`.tar.gz`, 912 KB) のほうが圧倒的に simple

### Reason 2: Claude sandbox は Linux native

Claude の sandbox (Ubuntu 24) は `tar xzf` を native command として持つ。本セッションで私が実際に行った操作:

```bash
# 本 chat の最初で、User upload した .tar を私が展開:
cd /home/claude/test_workspace/
tar xf /mnt/user-data/uploads/0sm-skills-v7_26-baseline.tar
```

User upload した archive は `/mnt/user-data/uploads/` に置かれ、Claude が `bash_tool` で展開 → `/home/claude/` 内 workspace として使用、という flow。**展開作業は完全 Claude 側**。

### Reason 3: Round-trip integrity

User 側で解凍 → 再 archive すると、以下 risks:

- Filename encoding 変化 (Mac → Windows transfer 等)
- Hidden files (`.DS_Store` 等) の混入
- Permission 変化
- Line ending (LF → CRLF) 変化

`.tar.gz` を **untouched で transit** させれば、Skill A workflow Step 14 で生成された state が Claude (新 chat) に identical に届く。

## 正しい lifecycle (図解)

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  [Skill A workflow Step 14]                                     │
│  Claude generates: 0sm-skills-v(N)-baseline.tar.gz              │
│                              │                                  │
│                              ▼                                  │
│  [Tier 1: User downloads to local]                              │
│  ~/Downloads/0sm-skills-v(N)-baseline.tar.gz                    │
│                              │                                  │
│                              ▼                                  │
│  [Tier 2: User commits to GitHub]                               │
│  HanaTensor/0sm-skills/workspace-baselines/                     │
│  └── 0sm-skills-v(N)-baseline.tar.gz                            │
│                              │                                  │
│                              ▼                                  │
│  [次セッション開始時: Download]                                 │
│  GitHub → Local: .tar.gz そのまま (解凍しない ★)                │
│                              │                                  │
│                              ▼                                  │
│  [新 chat で upload]                                            │
│  drag .tar.gz into Claude.ai chat input                         │
│                              │                                  │
│                              ▼                                  │
│  [Claude sandbox 内で auto-extract]                             │
│  /mnt/user-data/uploads/0sm-skills-v(N)-baseline.tar.gz         │
│  → bash_tool: tar xzf → /home/claude/workspace/                 │
│  → context/papers/ + topics/ + queries/ + ... + HANDOFF.md     │
│                              │                                  │
│                              ▼                                  │
│  [Claude が workspace を read + 作業開始]                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

User 側で `.tar.gz` を解凍する瞬間は **どこにもない**。Format unchanged で Claude sandbox まで届ける。

## 例外: User が workspace 内 file を 直接 read したい場合 (任意)

Curate session 外で User が **workspace の content を自分で確認したい** 場合 (例: `papers/045.md` の frontmatter を Mac の text editor で直接 read):

- そのときに限り Local で `.tar.gz` を解凍 (Finder double-click で OK)
- 解凍された folder を read-only で参照
- 新 chat upload 時は **元の `.tar.gz` を使う** (解凍した folder は直接 upload しない)

つまり User 側の解凍は **inspection 用 のみ**、Claude への upload には不要。

## 要約

| Scenario | User action |
|---|---|
| GitHub upload | `.tar.gz` をそのまま upload |
| 新 chat 利用時 | `.tar.gz` を GitHub から download → **そのまま** chat に upload |
| Workspace 内 file を Mac で直接見たい時 (任意) | Local で別途 `.tar.gz` 解凍して inspection、ただし chat upload には元の `.tar.gz` を使う |

Local 解凍は **必須プロセスではない**。`.tar.gz` を **「Black-box archive として最初から最後まで untouched で運用」** が standard pattern です。
