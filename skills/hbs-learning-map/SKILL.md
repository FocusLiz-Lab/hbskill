---
name: hbs-learning-map
description: |
  Build Huberman Lab learning maps with default IMA knowledge-base retrieval. Use when the user invokes $hbs-learning-map or asks what to study first, how to learn Huberman Lab systematically, which episodes/topics to prioritize, how to build a neuroscience, sleep, focus, stress, exercise, nutrition, supplement, or mental health learning path, or how to navigate the Huberman知识库｜科学改善生活（持续更新）.
---

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
