---
name: hbs-ima
description: |
  Compatibility entry for IMA retrieval with Huberman Lab workflows. Use when the user explicitly invokes $hbs-ima or asks to search, read, cite, quote-check, summarize, or troubleshoot Huberman Lab podcast, interview, X/Twitter, booklist, protocol, neuroscience, health, supplement, sleep, focus, exercise, or research materials from IMA. This skill uses the default IMA knowledge base named "Huberman Lab 知识库".
---

# hbs-ima

Use this skill as a thin compatibility entry for users who explicitly ask for IMA retrieval.

Default IMA knowledge base:

```text
Huberman Lab 知识库
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
