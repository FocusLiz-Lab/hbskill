---
name: hbs-learning-map
description: |
  Build Huberman Lab learning maps with default IMA knowledge-base retrieval. Use when the user invokes $hbs-learning-map or asks what to study first, how to learn Huberman Lab systematically, which episodes/topics to prioritize, how to build a neuroscience, sleep, focus, stress, exercise, nutrition, supplement, or mental health learning path, or how to navigate the Huberman知识库｜科学改善生活（持续更新）.
---

## 手动更新路由

用户明确要求“更新 skill / 检查更新 / 同步最新原子库”时，先执行此路由。使用当前 SKILL.md 所在目录解析脚本绝对路径：

```text
python "{skillDir}/tools/update_skill.py"
```

只检查时加 `--check`。脚本从 GitHub main 的固定提交同步本仓库整套 skill 和原子资料，覆盖前备份，写入失败回滚；不需要 Git 或 GitHub 登录。根据脚本实际结果报告当前提交、更新状态与失败原因。普通业务问题不自动更新。更新后重新读取相关 SKILL.md。


# hbs-learning-map

Design a learning path through Huberman Lab materials. Ground substantive claims in the default IMA knowledge base.

## Default IMA Knowledge Base

```text
Huberman知识库｜科学改善生活（持续更新）
```

## Workflow

1. Identify the user's goal: general literacy, protocol implementation, content creation, research, or a specific health/performance topic.
2. Search IMA for relevant episodes, interview notes, X posts, and booklist references.
3. Group materials into levels: foundation, applied protocols, deep dives, and review.
4. Sequence the path by dependency: concepts before mechanisms, mechanisms before protocols, protocols before self-experiments.
5. Add a small output task for each stage, such as a summary, checklist, protocol card, or experiment log.

## Output Format

```markdown
## 学习目标

## 推荐路径
| 阶段 | 学什么 | IMA 检索方向 | 产出 |
|---|---|---|---|

## 关键概念

## 7 天开始方式

## 需要回到 IMA 核对的点
```

## Quality Standards

- Prefer 3-6 stages, not a giant curriculum.
- Include likely search terms in Chinese and English.
- Do not invent episode titles or dates; mark uncertain items as search targets.
- Add medical-safety caveats when a topic involves supplements, medications, disease, pregnancy, injury, or psychiatric symptoms.
