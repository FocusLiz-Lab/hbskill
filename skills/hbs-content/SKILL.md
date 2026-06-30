---
name: hbs-content
description: |
  Create Huberman Lab grounded content workflows with default IMA knowledge-base retrieval. Use when the user invokes $hbs-content or asks for episode summaries, interview takeaways, short-video scripts, article outlines, newsletter issues, X/Twitter threads, hooks, topic calendars, educational posts, or content repurposing based on the Huberman知识库｜科学改善生活（持续更新）.
---

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
