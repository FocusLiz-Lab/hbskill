# hbs IMA Query Map

Default IMA knowledge base: `Huberman Lab 知识库`

Use this query map when a user explicitly asks for search, citation, or source checking.

## Search Expansion

| Intent | Query expansions |
|---|---|
| Sleep | sleep, circadian rhythm, sunlight, caffeine, NSDR, melatonin, 睡眠, 节律 |
| Focus | focus, attention, dopamine, acetylcholine, neuroplasticity, motivation, 专注, 多巴胺 |
| Stress | stress, anxiety, physiological sigh, breathing, cortisol, 压力, 焦虑 |
| Training | strength, hypertrophy, endurance, recovery, soreness, mobility, 训练, 恢复 |
| Nutrition | nutrition, fasting, glucose, satiety, metabolism, supplements, 营养, 代谢, 补剂 |
| Mental health | depression, trauma, emotion, social connection, therapy, 情绪, 心理 |
| Interviews | guest name, episode title, interview, conversation, 访谈 |
| X posts | date, keyword, protocol term, post, tweet, 推文 |

## Retrieval Output Rules

- Report which materials were found and which were not.
- Quote only short excerpts when necessary.
- Prefer paraphrase plus source identifier.
- Do not expose internal IDs.
- If the user asks for a claim check, state: supported, partially supported, not found, or contradictory evidence found.
