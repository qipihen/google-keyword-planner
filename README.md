# 🚀 Google Keyword Planner & SEO Intelligence Toolkit

> **零第三方依赖 · 结合哥飞 SEO 选词方法论 · KGR 黄金法则 · 智能文章选题与大纲生成**  
> 一套彻底告别昂贵 SEO 工具（如 Ahrefs / Semrush）和第三方数据中介的开源关键词挖掘与内容规划利器。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/)

---

## 💡 为什么需要这个工具？

很多人在独立站出海、内容创作、做自媒体或程序化建站（Programmatic SEO）时，最常面临以下痛点：

1. **写文章不知道该用什么词？**  
   坐在电脑前构思选题，不知道用户在 Google 搜索框里真正搜什么、怎么问，拍脑袋写出的文章无人问津。
2. **好不容易挑中词，却打不过行业大站？**  
   直接冲大词（如 `ai photo`），结果首页前 10 全被 Canva、Adobe 或维基百科垄断，新站发布后几个月都排在 100 名开外。
3. **商用 SEO 软件太贵！**  
   Ahrefs、Semrush 每月至少 $99~$129 起步，对于独立创作者、出海新人来说是一笔不小的开销。
4. **网上现成的抓取脚本经常“翻车跑偏”？**  
   很多网传的 Google Suggest 爬虫使用弱子串判定，搜 `seo` 抓到 `seoul meat co`（首尔烤肉）、`seolleongtang`（雪浓汤），整个词库全部污染。

**本项目专为解决上述问题而生——开箱即用，零配置秒跑，让每个人都能免费掌握专业级关键词挖掘与内容策划能力！**

---

## 🌟 核心特性与哥飞 SEO 方法论融合

### 1. 零门槛免 Token 批量拓词 (Alphabet Soup 字母汤)
- **100% 免费**，不需要任何 API Key、不需要翻看文档或注册第三方中介平台。
- **杜绝跑偏**：内置 `\b{seed}\b` 严格词边界过滤，彻底消除 `seo -> seoul` 等子串误伤。
- **全方位搜索意图覆盖**：自动运行 A-Z 字母汤（前缀/后缀）、0-9 数字、9大疑问词（how/what/why/can/where 等）以及 20+ 商业意图修饰词（best/vs/tools/checklist/pricing 等），单次挖掘数百到上千个纯净长尾词。

### 2. 哥飞版启发式 KD 难度评估 (Keyword Difficulty 0-100)
不依赖商业工具的黑盒打分，基于哥飞真实操盘逻辑，从 4 个维度量化竞争难度：
- **词长与长尾效应**：1-2 词大词阻力极高；4-6 词长尾词由于全网缺乏针对性优化，新站极易反超。
- **意图特异性**：疑问词（how to、why）与精准对比词（A vs B）通常竞争较小、转化率高。
- **分级标签明确**：
  - 🟢 `0 - 20` 极低难度（**新站必写**，几乎无专门竞品覆盖，发布即排名前排）
  - 🟡 `21 - 40` 低难度（单篇深度文章极易拿下首页）
  - 🟠 `41 - 60` 中等难度（需要一定反向链接与内链拓扑）
  - 🔴 `61 - 100` 高难度（巨头大站垄断，新手避坑）

### 3. KGR (Keyword Golden Ratio) 金比率自动核算
经典 SEO 金法则深度工程化：
$$\text{KGR} = \frac{\text{Google Allintitle 搜索结果数}}{\text{月搜索量 Monthly Search Volume}}$$
- 🟢 **KGR < 0.25 (黄金机会)**：全网把该词完整写入网页标题的竞争对手极少。只要新文章包含该词，收录后**极速排进前 50 甚至首页前排**！
- 🟡 **0.25 <= KGR <= 1.00 (适度竞争)**：中等机会，内容深度足够即可突破。
- 🔴 **KGR > 1.00 (竞争饱和)**：竞品标题已经扎堆，不建议新手开荒。

### 4. “值不值得做”综合机会评分 (Opportunity Score 0-100)
权衡 **流量规模 × 商业变现潜力 (CPC/意图) ÷ 竞争阻力 (KD/KGR)**，终端直接给出清晰明确的**行动建议**：
- `【🔥 强烈推荐·核心文章必写】`：商业意图强、难度低，推荐作为核心支柱文章。
- `【⚡ 优质长尾·易拿下流量】`：长尾低阻力，新站快速拉升收录与搜索曝光。
- `【🛠️ 工具落地页·程序化】`：Tool/Calculator 类词，适合做轻量 Web 工具单页。
- `【⚖️ 评测对比·高转化】`：Commercial/Review 类词，适合联盟营销 (Affiliate) 变现。
- `【🛑 竞争偏大·不建议首发】`：大站垄断词，建议暂缓。

### 5. 自动生成文章选题与完整 H1/H2/H3 大纲方案
**“再也不用发愁写文章不知道写什么！”**  
拓词与评分完成后，算法会自动将长尾词语义聚类，为你输出 3 套开箱即用的 Markdown 方案：
- **方案一：核心支柱长文 (Pillar Guide)**：包含吸引点击的高转化 H1 标题、按逻辑排布的长尾词 H2/H3 目录骨架、FAQ 结构。
- **方案二：高转化评测横评文章 (Commercial Roundup)**：包含置顶核心推荐对比表、多维度参数矩阵架构。
- **方案三：极速见效长尾问答文章 (Quick-Win Post)**：针对 KGR 极佳的长尾问题精选列表，专攻 Google 精选摘要 (Featured Snippets)。

---

## ⚡ 快速上手 (Quick Start)

### 1. 克隆仓库与安装依赖 (仅需 10 秒)

```bash
git clone https://github.com/your-username/google-keyword-planner.git
cd google-keyword-planner
pip install -r requirements.txt
```
*(仅依赖标准库和轻量级 requests，无需臃肿复杂的浏览器驱动！)*

---

### 2. 一键拓词与机会分析 (开箱即用 · 零配置)

直接输入你感兴趣的主题或种子词：

```bash
# 示例 1：英文市场挖掘
python run.py "ai photo generator"

# 示例 2：中文市场挖掘
python run.py "独立站建站" --hl zh-CN --gl cn

# 示例 3：开启 KGR 金比率计算
python run.py "crochet pattern" --kgr
```

终端将打印美观的分析排行榜：

```text
========================================================================================
排名   | 关键词                            | 搜索意图         | 哥飞KD         | 机会评分     | 行动建议
----------------------------------------------------------------------------------------
1    | what is best ai headshot generator | Commercial   | 🟢 12 (极低)    | 57       | 【⚖️ 评测对比·可规划排期】
2    | which ai headshot generator is best | Commercial   | 🟢 12 (极低)    | 57       | 【⚖️ 评测对比·可规划排期】
3    | best ai headshot generator for linkedin | Commercial   | 🟢 12 (极低)    | 57       | 【⚖️ 评测对比·可规划排期】
4    | is ai headshot worth it        | Commercial   | 🟢 18 (极低)    | 54       | 【⚖️ 评测对比·可规划排期】
5    | free ai headshot generator no sign up | Tool         | 🟢 12 (极低)    | 54       | 【🛠️ 工具落地页·程序化】
...
========================================================================================
📊 完整分析数据已导出至: output/gefei_seo_analysis_ai_photo_generator_20261110.csv
💡 自动生成的文章选题与大纲方案已保存至: output/content_plan_ai_photo_generator_20261110.md
```

同时生成 `.csv` 分析大表与 `.md` 文章大纲，打开即可直接复制用于写文章！

---

## 🎯 自动生成的文章大纲示例 (截取)

查看 `output/content_plan_*.md`：

```markdown
# ✍️ 基于「ai headshot」的 SEO 文章选题与大纲规划方案

## 📌 方案一：核心支柱长文 (Pillar Guide)
- **目标主词**：what is best ai headshot generator (哥飞KD: 🟢 12)
- **建议文章 H1 标题**：The Ultimate Guide to Ai Headshot: Strategies, Best Practices, and Tools for Beginners
- **建议字数**：2,000 ~ 3,500 词
- **章节骨架 (建议 H2 / H3 目录)**：
  - **H2: What is Ai Headshot and Why Does It Matter?**
    - H3: What is best ai headshot generator?
    - H3: Is ai headshot worth it?
  - **H2: Step-by-Step Implementation Guide**
    - H3: How to Leverage Best Ai Headshot Generator For Linkedin
  - **H2: Essential Tools & Checklists**
    - H3: Free Ai Headshot Generator No Sign Up
  - **H2: Frequently Asked Questions (FAQ)**
    - H3: Is ai headshot generator free?
    - H3: Is ai headshot generator safe?
```

---

## 🔑 进阶：直连官方 Google Ads API (每天 15,000 次免费额度)

若你需要官方的**精确月搜索量、真实竞价指数、CPC 出价范围与近 12 个月搜索走势**，可以零成本直连 Google Ads 官方 API：

1. **运行内置交互式配置向导**：
   ```bash
   python run.py --setup
   ```
   向导会引导你输入自己的 Google Cloud OAuth Client ID / Secret，并自动开启本地监听（`http://127.0.0.1:8787`），浏览器弹出一键授权即可保存长期有效的 `refresh_token`。
   *(详细自建教程请见 [references/google_cloud_setup_guide.md](references/google_cloud_setup_guide.md))*

2. **直连官方数据分析**：
   ```bash
   python run.py "seo audit" --official
   ```

---

## 📁 目录结构

```text
google-keyword-planner/
├── run.py                      # 开源 CLI 主入口 (双模式开箱秒跑)
├── requirements.txt            # 极简依赖清单
├── pyproject.toml              # 标准 Python 项目打包配置
├── keyword_planner/            # 核心业务模块
│   ├── scraper.py              # Google Suggest 批量拓词引擎 (防跑偏算法)
│   ├── evaluator.py            # 哥飞 SEO 选词决策引擎 (意图/KD/机会评分)
│   ├── kgr.py                  # KGR (Keyword Golden Ratio) 金比率分析器
│   ├── content_generator.py    # 文章选题与 H1/H2/H3 大纲智能生成器
│   ├── official_ads.py         # Google Ads 官方 REST API 直连模块
│   └── setup_wizard.py         # 交互式 OAuth 2.0 凭证向导
├── SKILL.md                    # 兼容 Codex / Claude / Cursor 的 Agent Skill 说明
├── agents/openai.yaml          # Agent UI 元数据
└── references/
    ├── gefei_seo_methodology.md    # 哥飞选词与机会评估方法论深度拆解
    ├── google_cloud_setup_guide.md # 免费自建 Google Cloud 凭证全流程
    └── api_errors_and_limits.md    # 常见报错与排错手册
```

---

## 🤝 贡献与反馈

欢迎提交 PR 或创建 Issue！无论是补充更多的意图词库、优化 KGR 判定模型，还是贡献更多国家地区的语言规则，我们都非常欢迎。

## 📄 开源许可证

本项目采用 [MIT 许可证](LICENSE)。你可以自由商用、修改和分发，但请保留原作者版权声明。
