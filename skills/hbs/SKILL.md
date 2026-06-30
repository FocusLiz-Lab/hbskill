---
name: hbs
description: |
  Huberman Lab podcast interview and science-based health workflow router with default IMA knowledge-base grounding. Use when the user asks about Huberman Lab, Andrew Huberman, neuroscience, sleep, circadian rhythm, focus, dopamine, stress, mental health, exercise, recovery, nutrition, supplements, hormones, protocols, episode search, interview takeaways, learning paths, content ideas, research synthesis, or habit/health roadmaps. By default, use the IMA knowledge base named "Huberman知识库｜科学改善生活（持续更新）". Triggers include $hbs, /hbs, Huberman, Huberman Lab, Andrew Huberman, 神经科学, 睡眠, 专注, 多巴胺, 压力, 补剂, 训练, 协议, 学习地图, 播客访谈, and 健康计划.
---

# hbs

Act as the main router for the Huberman Lab skill toolbox. Identify the user's intent and route to the most relevant workflow skill. If enough context exists, execute the routed workflow in the same answer.

## Default IMA Knowledge Base

All workflow skills default to:

```text
Huberman知识库｜科学改善生活（持续更新）
```

Users do not need to mention this knowledge-base name. If they explicitly name another IMA knowledge base, use that name instead.

## Required Dependency

All source-grounded workflows use `ima-skill` for retrieval:

- `ima-skill/SKILL.md`
- `ima-skill/knowledge-base/SKILL.md`

Do not invent IMA APIs. Do not expose IMA internal IDs to the user.

If `ima-skill` is not installed or credentials are missing, tell the user to install/configure IMA first:

```text
请安装 ima 技能
下载地址：https://app-dl.ima.qq.com/skills/ima-skills-1.1.7.zip
API Key 获取：https://ima.qq.com/agent-interface
```

## Route Map

| User intent | Route to | Use when |
|---|---|---|
| Learning path, topic order, where to start | `$hbs-learning-map` | User asks how to study Huberman Lab, what episodes/topics to prioritize, or how to navigate the knowledge base. |
| Protocol extraction, daily tools, habit design | `$hbs-protocol` | User wants sleep, focus, stress, training, recovery, nutrition, supplement, light, breathing, or routine protocols. |
| Content ideas, episode summaries, scripts, posts | `$hbs-content` | User wants to turn the knowledge base into articles, short videos, newsletters, threads, or interview takeaways. |
| Evidence synthesis, episode/interview comparison | `$hbs-research` | User asks to compare claims, summarize studies mentioned in episodes, find source-backed evidence, or analyze a topic. |
| 7/30/90-day personal implementation plan | `$hbs-roadmap` | User wants a structured plan, self-experiment, habit stack, review loop, or project roadmap. |
| Explicit IMA search/read/cite/troubleshooting | `$hbs-ima` | User specifically asks to search, read, cite IMA, or debug IMA retrieval. |

## Clarify Once

If the user is vague, ask one question:

```text
你现在最想处理哪一块：学习地图、协议/日常工具、内容创作、研究整理、行动计划，还是从 IMA 资料里找原文？
```

After the answer, route immediately.

## Health and Safety Boundary

- Treat Huberman Lab material as educational, not medical diagnosis or individualized treatment.
- For pregnancy, medications, endocrine disorders, psychiatric symptoms, pain, injury, sleep apnea, eating disorders, addiction, or supplements/drugs, recommend discussing the plan with a licensed clinician.
- Do not prescribe dosages, contraindication decisions, or medication changes unless the retrieved source explicitly supports a general educational statement; still frame it as clinician-discussion material.
- Do not invent quotes, studies, guest credentials, episode titles, dates, mechanisms, supplement effects, or protocols.

## Handoff Format

```text
这个问题交给 $skill-name。
原因：{one sentence}
需要输入：{what the user should provide next, if anything}
```

## Quality Bar

- Default to IMA-grounded workflow skills for substantive claims.
- Separate "source says", "inference", and "practical next step".
- Prefer simple, testable protocols over broad lifestyle advice.
- Do not imitate Andrew Huberman's persona.
- Do not expose IMA internal IDs unless the user explicitly asks for debugging.
