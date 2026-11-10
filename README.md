# 🏭 Google Keyword Planner & B2B SEO Intelligence Toolkit

> **专为乙方 SEO 机构、出海代运营团队与 B 端外贸/工业独立站量身定制的关键词武器库**  
> 彻底解决「Semrush / Ahrefs 在 B 端搜不出词、话题枯竭、泛流量转化低」的痛点。  
> **零第三方依赖 · 内置 Google 官方 API 网关 · 结合哥飞选词决策模型 · KGR 黄金法则 · 自动生成 B2B 采购与选型文章大纲**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/)

---

## ⚡ 痛点直击：为什么做 B 端/外贸客户的 SEO，用 Semrush 越来越找不到词？

如果你在乙方 SEO 机构、出海代运营公司操盘过 **制造外贸、机械设备、OEM/ODM 定制、工业耗材、化工电子** 等 B 端客户，你一定遇到过这些崩溃瞬间：

1. **“Semrush / Ahrefs 搜不出词，词库两三个月就枯竭了”**  
   - 三方商业工具依赖消费级 **点击流 (Clickstream)** 反推，对 B2C 大宗消费品有效；但在细分工业 B 端领域，全球每月只有几百个专业采购经理、工厂工程师搜索。三方工具往往粗暴判定为 `Volume: 0` 或搜不出词，导致编辑团队没话题可写。
2. **“写的文章有虚荣流量，但客户一个询盘 (RFQ) 都没有”**  
   - 为了 Semrush 上的搜索量数字，编辑去写了《什么是塑料》、《化妆品瓶的历史》等泛科普大词，招来一堆写作业的学生，客户网站跳出率高达 85%，续费面临巨大危机。
3. **“昂贵的账号坐席成本”**  
   - Semrush 基础账号 $130/月，多开团队坐席每月几千美金，极大地压缩了乙方团队的利润率。
4. **“网络公版爬虫频频跑偏”**  
   - 普通抓取脚本用弱子串匹配，搜 `seo` 跑偏成首尔烤肉（`seoul meat co`），搜工业管材 `pipe` 跑偏成烟斗游戏，词库全毁。

---

## 💎 破局之道：Google Keyword Planner (第一手真源) 的绝对优势

本项目通过**直连 Google 官方第一手广告竞价数据 (Google Ads API v26) + 严格词边界防跑偏的 Google 实时联想下拉建议 (Google Suggest)**，实现对三方工具的降维打击：

- 🎯 **连 10 次月搜索量的工业长尾采购词也能挖出**：  
  只要曾有海外采购商在 Google 搜索框敲过、或有工业品牌在后台竞价，Google Ads 官方第一方数据就有精确记录！
- 💼 **B 端专精：采购转化价值远大于虚荣流量**：  
  消费品词月搜 10 万，客单价 15 美元；而工业词 `custom airless cosmetic bottle manufacturer low moq` 即使月搜只有 40 次，**一个海外大客户询盘往往就是数十万美金的采购大单**！
- 🛡️ **所有人开箱即用，免配任何 Key**：  
  内置已部署在全球 Cloudflare 边缘的专属 API 网关，任何员工、文案作者克隆仓库即可秒级查询，无需申请 Google 凭证，不泄露任何私密秘钥。

---

## 🧠 深度融合：哥飞 SEO 选词体系在 B 端实战中的落地

### 1. B2B 供应链与采购意图增强引擎 (B2B Sourcing Modifiers)
不仅运行标准的 A-Z 字母汤与 0-9 数字，更自动叠加 **4 大工业采购意图词库**：
- **供应商寻源**：`manufacturer`, `supplier`, `factory`, `wholesale`, `vendor`, `contract manufacturing`
- **定制与产能模式**：`custom`, `oem`, `odm`, `private label`, `bulk`, `moq`, `low moq`
- **采购核价与商机**：`cost`, `price`, `pricing`, `quote`, `rfq`, `lead time`, `catalog`
- **技术标准与认证**：`fda approved`, `iso certified`, `ce certified`, `gmp compliant`, `specs`, `materials`

### 2. 哥飞版启发式 KD 难度评估 (0-100)
哥飞选词体系核心精髓：**新站/新内容绝不硬拼高 KD 大词，先从低阻力长尾切入**。
- 🟢 **0 - 20 (极低难度)**：**开荒必写词**！大厂（如 Alibaba、Made-in-China）只有大分类聚合页，全网几乎没有针对该词专门撰写的 3000 字深度技术长文。
- 🟡 **21 - 40 (低难度)**：一篇结构严谨、解答详实的产品/技术指南极易在 2~4 周冲上 Google 首页。
- 🟠 **41 - 60 (中等难度)**：需搭配内链集群与专题支撑。
- 🔴 **61 - 100 (高难度)**：行业巨头与维基百科盘踞，新手避坑。

### 3. KGR (Keyword Golden Ratio) 金比率判定
$$\text{KGR} = \frac{\text{Google Allintitle 搜索结果数}}{\text{月搜索量 Monthly Search Volume}}$$
- 🟢 **KGR < 0.25 (黄金捡钱词)**：全网把该词完整写入 `<title>` 的网页屈指可数。新文章只要标题和 H1 包含该词，收录后**极速排进 Google 前排**！

### 4. 自动生成 B2B 采购指南与工艺选型大纲
**彻底解决内容团队“不知道写什么话题”的难题！**  
算法自动完成语义聚类，一键在 `output/content_plan_*.md` 产出 3 套专业交付级大纲：
- **方案一：B2B 采购寻源指南 (Buyer's Guide)**：包含吸引采购总监的 H1、工厂审核标准、MOQ 阶梯定价、质检认证（ISO/CE）与采购 FAQ 问答架构。
- **方案二：工程选型与材质工艺参数文章 (Technical Specs Guide)**：面向海外研发工程师、工艺师的参数对比矩阵与材质选型指南。
- **方案三：低竞争开荒长尾文章 (Quick-Win Q&A)**：专挑哥飞 KD 最低或 KGR < 0.25 的精准采购词，专攻 Google 首页精选摘要 (Featured Snippets)。

---

## ⚡ 极速上手 (10 秒开箱即用)

### 1. 克隆与安装依赖

```bash
git clone https://github.com/qipihen/google-keyword-planner.git
cd google-keyword-planner
pip install -r requirements.txt
```

---

### 2. 一键执行 B 端关键词挖掘与机会分析

直接传入客户的主营品类词（例如 `airless bottle` 或 `tablet press`）：

```bash
# 示例 1：B 端品类拓词 + 官方搜索量/CPC + 哥飞KD + 采购文章大纲 (免配 Key 开箱即用)
python run.py "airless bottle"

# 示例 2：开启 KGR 金比率计算
python run.py "rotary tablet press" --kgr

# 示例 3：指定多语言或特定国家市场
python run.py "injection molding" --hl en --gl uk
```

---

## 📊 终端实测输出样例

```text
==================================================================================
🎯 正在针对种子词「airless bottle」进行多维度 SEO 智能挖掘与机会分析...
语言: en | 地区: us | 模式: 开箱即用 (官方 API 网关就绪)
==================================================================================
🔍 正在抓取 Google 实时搜索下拉联想词...
✅ 成功捕获 412 个纯净长尾词！
📡 正在调用内置 Google Ads 官方网关获取真实月搜索量、竞争指数与 CPC 出价...
✨ 官方网关同步成功！获得 856 条 Google Ads 官方精准指标。
🧠 正在执行哥飞 SEO 难度算法评估 (KD) 与商业价值机会评分...

==========================================================================================
排名   | 关键词                                | 月搜索量     | 哥飞KD         | 机会评分     | 行动建议
------------------------------------------------------------------------------------------
1    | custom airless bottle manufacturer   | 110      | 🟢 12 (极低)    | 88       | 【💼 采购寻源·询盘转化必写】
2    | airless pump bottle wholesale low moq | 90       | 🟢 10 (极低)    | 86       | 【💼 采购寻源·询盘转化必写】
3    | airless bottle supplier china        | 140      | 🟢 14 (极低)    | 85       | 【💼 采购寻源·询盘转化必写】
4    | how does an airless pump bottle work | 720      | 🟢 16 (极低)    | 79       | 【📐 选型参数·技术背书长文】
5    | airless cosmetic bottle specifications | 50       | 🟢 11 (极低)    | 76       | 【📐 选型参数·技术背书长文】
6    | airless pump bottle materials guide  | 70       | 🟢 13 (极低)    | 75       | 【📐 选型参数·技术背书长文】
...
==========================================================================================
📊 完整分析数据大表已导出至: output/gefei_seo_analysis_airless_bottle_20261110.csv
💡 自动生成的文章选题与大纲已保存至: output/content_plan_airless_bottle_20261110.md
```

---

## 📝 自动生成的 B2B 采购文章大纲示例 (截取)

查看自动生成的 `output/content_plan_*.md`：

```markdown
# 🏭 基于「airless bottle」的 B2B 行业 SEO 采购指南与文章大纲方案

## 📌 方案一：B2B 核心采购寻源指南 (Buyer's Sourcing Guide)
- **目标主词**：custom airless bottle manufacturer (意图: B2B Sourcing / RFQ)
- **建议文章 H1 标题**：How to Source & Buy Airless Bottle: The Complete B2B Buyer's Guide for Manufacturers & Distributors
- **商业变现定位**：直接承接海外采购经理的询盘 (RFQ)，沉淀高客单转化
- **建议字数**：2,200 ~ 3,500 词
- **章节骨架 (建议 H2 / H3 目录)**：
  - **H2: Understanding Airless Bottle: Types, Applications & Industry Standards**
    - H3: Key Considerations for Cosmetic & Pharmaceutical Packaging
  - **H2: How to Evaluate Reliable Airless Bottle Manufacturers & Suppliers**
    - H3: Factory Audit & Quality Control (ISO, FDA, GMP Compliance)
    - H3: MOQ, Pricing Structures & Lead Time Breakdown
  - **H2: Custom OEM/ODM Capabilities: Materials, Tooling & Design**
    - H3: Best Practices for Private Label & Custom Molding
  - **H2: Common Pitfalls to Avoid in Overseas Sourcing** (避坑指南与质检要点)
  - **H2: Frequently Asked Procurement Questions (FAQ)**
    - H3: What is the average lead time for custom tooling?
    - H3: How does an airless pump bottle prevent oxidation?
```

---

## 📁 架构与目录

```text
google-keyword-planner/
├── run.py                          # 开源 CLI 主入口 (开箱秒跑)
├── requirements.txt                # 极简纯净依赖 (零臃肿驱动)
├── pyproject.toml                  # 标准 Python 模块配置
├── keyword_planner/                # 核心算法引擎
│   ├── b2b_config.py               # B2B 工业采购与供应链修饰词库
│   ├── scraper.py                  # 词边界防跑偏 Google Suggest 引擎
│   ├── evaluator.py                # 哥飞选词决策与 B2B 采购意图评分
│   ├── kgr.py                      # KGR (Keyword Golden Ratio) 金比率核算器
│   ├── content_generator.py        # B2B 采购指南与工艺选型大纲生成器
│   ├── official_ads.py             # 官方 API 客户端与 Cloudflare 全球网关
│   └── setup_wizard.py             # 自建官方凭证向导 (可选)
├── references/
│   ├── b2b_agency_seo_playbook.md  # 乙方 SEO 操盘 B 端行业实战手册
│   ├── gefei_seo_methodology.md    # 哥飞选词与机会评估方法论深度拆解
│   ├── google_cloud_setup_guide.md # 自建 Google 凭证图文教程
│   └── api_errors_and_limits.md    # 常见报错与排错手册
└── SKILL.md                        # 兼容 Codex / Claude / Cursor 的 Agent Skill
```

---

## 📄 开源许可证

本项目采用 [MIT 许可证](LICENSE)。你可以自由商用、集成到 Agency 内部 SOP 工作流或进行二次分发。
