---
name: hbs-protocol
description: |
  Extract and adapt Huberman Lab protocols with default IMA knowledge-base retrieval. Use when the user invokes $hbs-protocol or asks for practical science-based tools, routines, daily protocols, habit design, self-experiments, or checklists for sleep, circadian rhythm, morning sunlight, focus, dopamine, stress, breathing, exercise, recovery, nutrition, supplements, hormones, learning, motivation, or mental health from the Huberman知识库｜科学改善生活（持续更新）.
---

## 手动更新路由

用户明确要求“更新 skill / 检查更新 / 同步最新原子库”时，先执行此路由。使用当前 SKILL.md 所在目录解析脚本绝对路径：

```text
python "{skillDir}/tools/update_skill.py"
```

只检查时加 `--check`。脚本从 GitHub main 的固定提交同步本仓库整套 skill 和原子资料，覆盖前备份，写入失败回滚；不需要 Git 或 GitHub 登录。根据脚本实际结果报告当前提交、更新状态与失败原因。普通业务问题不自动更新。更新后重新读取相关 SKILL.md。


# hbs-protocol

Create practical protocol cards from Huberman Lab materials. Ground claims in IMA retrieval and clearly separate evidence from adaptation.

## Default IMA Knowledge Base

```text
Huberman知识库｜科学改善生活（持续更新）
```

## Workflow

1. Clarify the target outcome, constraints, current routine, risk factors, and measurement window.
2. Search IMA for the topic and related mechanism terms.
3. Extract general protocol elements: trigger, timing, duration, frequency, constraints, expected mechanism, and evidence caveats.
4. Convert the material into a low-risk protocol card and a tracking plan.
5. Add safety boundaries and clinician-discussion prompts when needed.

## Output Format

```markdown
## 目标

## IMA 依据摘要
- 命中材料：
- 关键机制：
- 证据强度：
- 不确定点：

## 协议卡
| 项目 | 建议 |
|---|---|
| 适用场景 |  |
| 做法 |  |
| 时间/频率 |  |
| 观察指标 |  |
| 停止/调整信号 |  |

## 7 天执行表

## 安全边界
```

## Health Boundary

- Do not create individualized medical treatment plans.
- Do not recommend changing prescriptions, hormone therapy, psychiatric medication, or supplement stacks without clinician involvement.
- For supplements, state that purity, interactions, dosage, pregnancy status, age, medical conditions, and medications matter.
- For pain, injury, severe insomnia, apnea symptoms, mood crisis, addiction, eating disorder signs, or endocrine symptoms, advise professional evaluation.
