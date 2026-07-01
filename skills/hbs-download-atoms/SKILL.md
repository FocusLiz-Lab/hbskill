---
name: hbs-download-atoms
description: 下载或更新 Huberman Lab / hbskill 的全量本地原子库。用于用户安装 SkillHub 轻量包后，需要从 GitHub 拉取完整 `知识库/原子库/atoms.jsonl` 和按年份/季度拆分的 `atoms_*.jsonl` 文件。
---

# hbs-download-atoms 全量原子库下载

当用户要求下载、补全、更新或修复 hbskill 本地原子库时，运行：

```powershell
python tools/download_full_atoms.py
```

下载完成后，原子库应位于：

```text
知识库/原子库/atoms.jsonl
```

以及同目录下的 `atoms_*.jsonl` 文件。
