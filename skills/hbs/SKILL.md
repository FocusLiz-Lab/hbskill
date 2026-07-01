---
name: hbs
description: |
  Huberman Lab 科学健康 Skill 工具箱主入口。用于神经科学、睡眠、昼夜节律、专注、多巴胺、压力、心理健康、训练、恢复、营养、补剂、激素、健康协议、播客检索、访谈要点、学习路径、内容选题、研究综合和健康行动计划。默认使用 IMA 知识库「Huberman知识库｜科学改善生活（持续更新）」，并可在 IMA 不可用时读取本地原子库。触发词包括 $hbs、/hbs、Huberman、Andrew Huberman、神经科学、睡眠、专注、多巴胺、压力、补剂、训练、协议、学习地图、播客访谈和健康计划。
---

# hbs Huberman 科学健康工具箱

这是 Huberman Lab 科学健康工具箱的主入口。先判断用户意图，再路由到最相关的 workflow skill；如果上下文足够，直接在同一回答中完成对应工作流。

## 默认 IMA 知识库

所有 workflow skills 默认读取：

```text
Huberman知识库｜科学改善生活（持续更新）
```

用户不需要每次输入这个知识库名称。如果用户明确指定其他 IMA 知识库，则优先使用用户指定的知识库。

## 必要依赖

所有需要资料依据的 workflow 都使用 `ima-skill` 做检索：

- `ima-skill/SKILL.md`
- `ima-skill/knowledge-base/SKILL.md`

不要臆造 IMA API。不要向用户暴露 IMA 内部 ID。

如果没有安装 `ima-skill` 或凭证缺失，先提示用户安装并配置 IMA：

```text
请安装 ima 技能
下载地址：https://app-dl.ima.qq.com/skills/ima-skills-1.1.7.zip
API Key 获取：https://ima.qq.com/agent-interface
```

## 路由表

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
