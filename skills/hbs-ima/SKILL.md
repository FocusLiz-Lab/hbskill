---
name: hbs-ima
description: |
  Compatibility entry for IMA retrieval with Huberman Lab workflows. Use when the user explicitly invokes $hbs-ima or asks to search, read, cite, quote-check, summarize, or troubleshoot Huberman Lab podcast, interview, X/Twitter, booklist, protocol, neuroscience, health, supplement, sleep, focus, exercise, or research materials from IMA. This skill uses the default IMA knowledge base named "Huberman知识库｜科学改善生活（持续更新）".
---

## 手动更新路由

用户明确要求“更新 skill / 检查更新 / 同步最新原子库”时，先执行此路由。使用当前 SKILL.md 所在目录解析脚本绝对路径：

```text
python "{skillDir}/tools/update_skill.py"
```

只检查时加 `--check`。脚本从 GitHub main 的固定提交同步本仓库整套 skill 和原子资料，覆盖前备份，写入失败回滚；不需要 Git 或 GitHub 登录。根据脚本实际结果报告当前提交、更新状态与失败原因。普通业务问题不自动更新。更新后重新读取相关 SKILL.md。


# hbs-ima

Use this skill as a thin compatibility entry for users who explicitly ask for IMA retrieval.

Default IMA knowledge base:

```text
Huberman知识库｜科学改善生活（持续更新）
```

For the actual workflow, follow `$hbs`:

```text
IMA search/read -> evidence summary -> relevant workflow selection -> final answer
```

Required dependency:

- `ima-skill/SKILL.md`
- `ima-skill/knowledge-base/SKILL.md`

Rules:

- Use the default knowledge base unless the user explicitly names another IMA knowledge base.
- Do not expose IMA internal IDs.
- Do not claim to have read IMA content unless retrieval actually happened.
- Use IMA as the retrieval source. Do not add non-IMA fallback instructions to this skill.
- If IMA credentials are missing, explain setup and do not silently use unverified materials.
- For health claims, label evidence strength and avoid individualized medical advice.

Output a compact template:

```markdown
## IMA 检索摘要
- 知识库：
- 检索词：
- 命中的材料：
- 可用证据：
- 不确定/缺失：

## 处理结果

## 下一步
```
