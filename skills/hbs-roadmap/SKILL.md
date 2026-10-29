---
name: hbs-roadmap
description: |
  Build 7/30/90-day implementation roadmaps from Huberman Lab materials with default IMA knowledge-base retrieval. Use when the user invokes $hbs-roadmap or asks to turn Huberman Lab protocols into a personal plan, habit stack, self-experiment, project roadmap, review loop, behavior-change plan, or practical health/performance system using the Huberman知识库｜科学改善生活（持续更新）.
---

## 手动更新路由

用户明确要求“更新 skill / 检查更新 / 同步最新原子库”时，先执行此路由。使用当前 SKILL.md 所在目录解析脚本绝对路径：

```text
python "{skillDir}/tools/update_skill.py"
```

只检查时加 `--check`。脚本从 GitHub main 的固定提交同步本仓库整套 skill 和原子资料，覆盖前备份，写入失败回滚；不需要 Git 或 GitHub 登录。根据脚本实际结果报告当前提交、更新状态与失败原因。普通业务问题不自动更新。更新后重新读取相关 SKILL.md。


# hbs-roadmap

Turn Huberman Lab concepts into a structured implementation plan while respecting health-safety limits.

## Default IMA Knowledge Base

```text
Huberman知识库｜科学改善生活（持续更新）
```

## Workflow

1. Clarify the target outcome, baseline, constraints, available time, and risk factors.
2. Search IMA for protocols and mechanisms related to the outcome.
3. Choose the minimum viable habit stack: one anchor behavior, one support behavior, one metric.
4. Build a 7/30/90-day roadmap with review checkpoints.
5. Add stop conditions and "ask a professional" conditions.

## Output Format

```markdown
## 目标与边界

## IMA 依据摘要

## 7 天启动

## 30 天巩固

## 90 天复盘

## 指标
| 指标 | 记录方式 | 复盘频率 |
|---|---|---|

## 风险与调整
```

## Quality Standards

- Prefer behavior and measurement over supplement-heavy plans.
- Keep the first 7 days small enough to execute.
- Include a review cadence and failure-recovery plan.
- Do not provide individualized diagnosis, treatment, or medication/supplement directives.
