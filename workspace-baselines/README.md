
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
