# hbskill

Huberman Lab 风格播客访谈、神经科学学习与健康协议 Skill 工具箱。

`hbskill` 是一组面向 Agent 的 workflow skills，用来基于 IMA 知识库学习 Huberman Lab 资料，整理播客访谈和研究观点，提炼健康/表现协议，生成内容资产，并把协议转成可执行行动计划。

适用于 Codex、Claude Code、Cursor、Trae Solo 等支持 skill / system prompt 工作流的 Agent。

---

## 安装

发布后，可以用下面的命令安装整套 skills：

```bash
npx -y skills add FocusLiz-Lab/hbskill -g --all
```

安装后可以直接使用：

```text
$hbs 我想系统学习 Huberman Lab 的睡眠和专注主题，先从哪里开始？
```

也可以手动复制或导入 `skills/` 目录下的 skill 文件夹：

```text
skills/
├── hbs/
├── hbs-learning-map/
├── hbs-protocol/
├── hbs-content/
├── hbs-research/
├── hbs-roadmap/
└── hbs-ima/
```

---

## IMA 配置

整套 workflow skills 默认读取这个 IMA 知识库：

```text
Huberman知识库｜科学改善生活（持续更新）
```

用户不需要在每次提问时输入知识库名称。如果想使用其他 IMA 知识库，在问题里直接写知识库名称即可。

### 加入 / 访问知识库

扫码获取知识库：

![知识库二维码](docs/knowledge-base-qrcode.png)

### 安装 IMA Skill

```text
请安装 ima 技能
下载地址：https://app-dl.ima.qq.com/skills/ima-skills-1.1.7.zip
API Key 获取：https://ima.qq.com/agent-interface
```

使用前需要满足：

- 已安装官方 `ima-skill`
- 已配置 IMA `Client ID` 和 `API Key`
- 当前 IMA 账号有权限访问目标知识库

本仓库不包含、也不会保存任何 IMA API Key。

---

## 工具箱

| Skill | 用途 |
|---|---|
| `$hbs` | 主入口。根据用户问题自动路由到合适的 Huberman Lab workflow。 |
| `$hbs-learning-map` | 学习地图：主题顺序、 episode/访谈检索方向、学习产出。 |
| `$hbs-protocol` | 协议工具：睡眠、专注、压力、训练、营养、补剂等协议卡。 |
| `$hbs-content` | 内容系统：选题、脚本、文章、newsletter、访谈要点整理。 |
| `$hbs-research` | 研究整理：证据表、机制图、主张核对、访谈对比。 |
| `$hbs-roadmap` | 行动计划：7/30/90 天自我实验、习惯栈和复盘指标。 |
| `$hbs-ima` | IMA 检索入口：搜索、阅读、引用或排查 IMA。 |

---

## 常见路径

### 从系统学习到执行

```text
hbs-learning-map
    ↓
hbs-protocol
    ↓
hbs-roadmap
```

### 从资料整理到内容发布

```text
hbs-research
    ↓
hbs-content
    ↓
事实核对
```

### 显式 IMA 检索

```text
hbs-ima
    ↓
对应 workflow skill
```

---

## 使用示例

```text
$hbs-learning-map 系统学习 Huberman Lab 的睡眠、节律和日常能量主题，先看哪些？
```

```text
$hbs-protocol 把早晨光照、咖啡因和晚上睡眠整理成一个 7 天协议卡。
```

```text
$hbs-research 比较几期关于多巴胺和动机的内容，整理证据表和不确定点。
```

```text
$hbs-content 围绕压力调节和 physiological sigh 做 10 个短视频选题。
```

```text
$hbs-roadmap 我想用 30 天改善睡眠和专注，帮我做行动计划。
```

---

## SkillHub 轻量包与全量原子库

SkillHub 单个上传包限制小于 10MB，因此 SkillHub 压缩包是轻量包，不直接内置完整 `atoms.jsonl`。安装后如果需要本地离线兜底检索，调用：

```text
$hbs-download-atoms
```

或在 hbskill 安装目录中运行：

```powershell
python tools/download_full_atoms.py
```

它会自动从 GitHub 下载并安装完整原子库到：

```text
知识库/原子库/atoms.jsonl
知识库/原子库/atoms_*.jsonl
```

如果需要手动下载，也可以在 GitHub Release 中下载 `hbs-local.zip`，它包含完整本地原子库。

## 知识库 / 原子库

本仓库包含一个发布安全的抽象原子库：

```text
知识库/原子库/atoms.jsonl
```

它用于保存 Huberman Lab workflow 的方法论单元，不包含原始转录稿、X/Twitter 原文、PDF、书籍正文或付费材料。涉及具体原文、出处、嘉宾、日期和研究细节时，仍应优先使用 IMA 知识库检索。

---

## 资料边界

本仓库只包含 skill instructions、workflow 抽象、知识库索引和二维码。

本仓库不包含 Huberman Lab 的原始 YouTube 转录稿、X/Twitter 归档、PDF 书籍、私有资料文件夹或任何受版权保护的原始资料库。

这些 skills 会在运行时从用户自己的 IMA 知识库检索资料。用户需要自行确保有权上传和使用自己的资料。

健康相关输出仅用于教育和信息整理，不构成医疗诊断、治疗或个性化用药/补剂建议。

请不要提交：

- IMA API Key
- 私有资料文件
- 原始 PDF、转录稿、视频或归档
- 个人环境配置
- 任何未经授权的第三方内容

---

## 许可证

本项目默认采用 CC BY-NC 4.0 许可证，除非后续另行添加其他许可证。

许可证只覆盖本仓库原创的 skill instructions 和 workflow 抽象，不授权任何第三方原始资料。
