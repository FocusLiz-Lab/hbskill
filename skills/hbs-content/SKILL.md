---
name: hbs-content
description: |
  Create Huberman Lab grounded content workflows with default IMA knowledge-base retrieval. Use when the user invokes $hbs-content or asks for episode summaries, interview takeaways, short-video scripts, article outlines, newsletter issues, X/Twitter threads, hooks, topic calendars, educational posts, or content repurposing based on the Huberman知识库｜科学改善生活（持续更新）.
---

## 手动更新路由

用户明确要求“更新 skill / 检查更新 / 同步最新原子库”时，先执行此路由。使用当前 SKILL.md 所在目录解析脚本绝对路径：

```text
python "{skillDir}/tools/update_skill.py"
```

只检查时加 `--check`。脚本从 GitHub main 的固定提交同步本仓库整套 skill 和原子资料，覆盖前备份，写入失败回滚；不需要 Git 或 GitHub 登录。根据脚本实际结果报告当前提交、更新状态与失败原因。普通业务问题不自动更新。更新后重新读取相关 SKILL.md。


# hbs-content

Turn Huberman Lab materials into educational content without copying source text or imitating Andrew Huberman's persona.

## Default IMA Knowledge Base

```text
Huberman知识库｜科学改善生活（持续更新）
```

## Workflow

1. Identify audience, platform, format, length, and desired action.
2. Search IMA for the topic, episode/interview, or protocol.
3. Extract only short evidence notes and practical takeaways; do not reproduce transcripts.
4. Build content around a clear promise, mechanism, practical tool, caveat, and next step.
5. Add source-check notes for claims that must be verified before publishing.

## Output Format

```markdown
## 内容定位

## IMA 依据
- 检索词：
- 命中材料：
- 可用观点：

## 选题/脚本

## 事实核对清单

## 发布边界
```

## Content Rules

- Do not output long transcript excerpts, full tweets, book passages, or paid material.
- Do not claim "Huberman said" unless IMA retrieval supports it.
- Avoid medical certainty and miracle claims.
- Mark each claim as source-backed, inferred, or needs verification when the content is public-facing.
