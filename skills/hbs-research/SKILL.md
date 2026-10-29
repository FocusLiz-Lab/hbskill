---
name: hbs-research
description: |
  Research and synthesize Huberman Lab topics with default IMA knowledge-base retrieval. Use when the user invokes $hbs-research or asks to compare episodes, summarize interviews, analyze evidence, map mechanisms, inspect claims, find citations, compare protocols, or produce a source-grounded briefing on neuroscience, sleep, stress, focus, nutrition, supplements, exercise, hormones, psychology, or health topics from the Huberman知识库｜科学改善生活（持续更新）.
---

## 手动更新路由

用户明确要求“更新 skill / 检查更新 / 同步最新原子库”时，先执行此路由。使用当前 SKILL.md 所在目录解析脚本绝对路径：

```text
python "{skillDir}/tools/update_skill.py"
```

只检查时加 `--check`。脚本从 GitHub main 的固定提交同步本仓库整套 skill 和原子资料，覆盖前备份，写入失败回滚；不需要 Git 或 GitHub 登录。根据脚本实际结果报告当前提交、更新状态与失败原因。普通业务问题不自动更新。更新后重新读取相关 SKILL.md。


# hbs-research

Produce source-grounded research briefs from Huberman Lab materials.

## Default IMA Knowledge Base

```text
Huberman知识库｜科学改善生活（持续更新）
```

## Workflow

1. Convert the user question into 3-8 search queries, including English mechanism terms when useful.
2. Search IMA for episodes, interviews, clips, X posts, and booklist references.
3. Cluster evidence by claim, mechanism, protocol, counterpoint, and uncertainty.
4. Distinguish source statements from synthesis and practical implication.
5. Flag claims needing external literature verification if IMA only contains commentary or summaries.

## Output Format

```markdown
## 问题

## 检索策略

## 证据表
| 主题 | IMA 命中材料 | 主要观点 | 证据强度 | 不确定点 |
|---|---|---|---|---|

## 综合结论

## 可执行启发

## 仍需核对
```

## Quality Standards

- Do not overstate causality from mechanistic explanations.
- Separate animal, observational, clinical, anecdotal, and expert-opinion evidence when the source allows it.
- Do not invent papers, PMID/DOI, guest credentials, or trial results.
- For high-stakes health choices, recommend clinician review and primary-source verification.
