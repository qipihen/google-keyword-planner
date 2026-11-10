# 🏭 Google Keyword Planner & B2B SEO Intelligence Toolkit

> **专为乙方 SEO 机构、出海代运营团队与 B 端外贸/工业独立站量身定制的关键词武器库**  
> 彻底解决「Semrush / Ahrefs 在 B 端搜不出词、话题枯竭、泛流量转化低」的痛点。  
> **零第三方依赖 · 内置 Google 官方 API 网关 · 智能意图集群 (Intent Clusters) · Pillar-Cluster 拓扑地图 · KGR 黄金法则**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/)

---

## ⚡ 痛点直击：为什么做 B 端/外贸客户的 SEO，用 Semrush 越来越找不到词？

如果你在乙方 SEO 机构、出海代运营公司操盘过 **制造外贸、机械设备、OEM/ODM 定制、工业耗材、化工电子** 等 B 端客户，你一定遇到过这些困境：

1. **“Semrush / Ahrefs 搜不出词，词库两三个月就枯竭了”**  
   - 商业三方工具主要依赖消费级 **点击流 (Clickstream)** 采样，对 B2C 消费品有效；但在细分工业 B 端领域，全球每月只有几百个专业采购经理、工厂工程师搜索。三方工具因为抽样不足，往往粗暴判定为 `Volume: 0` 或搜不出词，导致编辑团队没话题可写。
2. **“写的文章有虚荣流量，但客户一个询盘 (RFQ) 都没有”**  
   - 为了 Semrush 上的搜索量数字，编辑去写了《什么是塑料》、《化妆品瓶的历史》等泛科普大词，招来一堆写作业的学生，客户网站跳出率高达 85%，续费面临巨大危机。
3. **“单篇写词无法沉淀权重，孤岛文章排名摇摆”**  
   - 缺乏完整的意图集群（Intent Clusters）与支柱架构（Pillar-Cluster），文章之间互不关联，Google 无法识别网站在具体品类上的整体权威度。

---

## 💎 破局之道：Google Keyword Planner (第一手真源) 的绝对优势

本项目通过**直连 Google 官方第一手广告竞价数据 (Google Ads API v26) + 严格词边界防跑偏的 Google 实时联想下拉建议 (Google Suggest)**，实现对三方工具的降维打击：

- 🎯 **连 10 次月搜索量的工业长尾采购词也能挖出**：  
  只要曾有海外采购商在 Google 搜索框敲过、或有工业品牌在后台竞价，Google Ads 官方第一方数据就有精准记录！
- 💼 **B 端专精：采购转化价值远大于虚荣流量**：  
  消费品词月搜 10 万，客单价 15 美元；而工业词 `custom airless cosmetic bottle manufacturer low moq` 即使月搜只有 40 次，**一个海外大客户询盘往往就是数十万美金的采购大单**！
- 🛡️ **所有人开箱即用，免配任何 Key**：  
  内置已部署在全球 Cloudflare 边缘的专属 API 网关，任何员工、文案作者克隆仓库即可秒级查询，无需申请 Google 凭证，不泄露任何私密秘钥。

---

## 🏛️ 核心突破：关键词意图集群 (Intent Clusters) 与 Pillar 拓扑架构

在现代 Google 算法（RankBrain、MUM、Topical Authority）与海外采购心智模型下，**单打独斗的单篇文章必死，唯有集群拓扑才能霸榜！**

本项目自动将挖掘出的海量长尾词，聚类为 **5 大海外采购意图集群**，并自动生成双向内链闭环拓扑图：

```text
               ┌────────────────────────────────────────────────────────┐
               │       【核心支柱主页 (Core Pillar Hub)】                │
               │  Role: 统领全行业、高权重核心大词、承接海外大客户第一入口 │
               │  Slug: /airless-bottle-guide/                          │
               └──────────────────────────┬─────────────────────────────┘
                                          │ 双向内链 (Contextual Links)
          ┌───────────────────────────────┼───────────────────────────────┐
          ▼                               ▼                               ▼
  ┌───────────────┐               ┌───────────────┐               ┌───────────────┐
  │ 卫星集群页 1  │               │ 卫星集群页 2  │               │ 卫星集群页 3  │
  │ Sourcing/RFQ  │               │ Specs/Param   │               │ Comparisons   │
  │ 采购寻源与MOQ │               │ 规格材质选型  │               │ 竞品横评对比  │
  └───────┬───────┘               └───────┬───────┘               └───────┬───────┘
          │                               │                               │
          └───────────────────────────────┴───────────────────────────────┘
               ▲                                                          ▲
  ┌────────────┴──┐                                               ┌───────┴───────┐
  │ 卫星集群页 4  │                                               │ 卫星集群页 5  │
  │ How-to/Process│ ◀──────────── 相互交叉支撑链接 ────────────▶  │Troubleshoot/QA│
  │ 生产工艺原理  │                                               │保养与避坑指南 │
  └───────────────┘                                               └───────────────┘
```

### 为什么必须做「核心支柱 (Pillar) - 卫星集群 (Cluster)」拓扑？
1. **意图完整性**：海外采购决策人经历「原理了解 (TOFU) -> 选型参数对比 (MOFU) -> 寻源询盘 (BOFU)」，集群页面完整承接采购心智全链路。
2. **权重倍增流动**：卫星集群页面由于长尾词难度低（B2B-KD 5~25），新站发布后能极快冲上 Google 首页并积攒自然权重；通过内链反哺核心支柱页，促使高难度核心大词水涨船高！
3. **消除孤岛页面**：全站形成紧密的网状链接，Google 蜘蛛一次性抓取全部关联页面，收录率与更新频次提升 300%。

---

## 🧠 5 大功能矩阵

### 1. B2B 供应链拓词引擎 (`scraper.py` + `b2b_config.py`)
自动叠加供应商寻源（`manufacturer/supplier/factory/oem/odm`）、采购商机（`moq/quote/rfq/price`）、技术认证（`iso certified/fda/ce/specs`）等数百个采购修饰词，词边界精准过滤防跑偏。

### 2. B2B-KD 难度评估模型 (`evaluator.py`)
针对 B 端特征设计的 0-100 难度分：
- 🟢 `0 - 20` (极低难度)：**开荒必写词**，大厂只有粗目录页，全网无专门深度技术长文。
- 🟡 `21 - 40` (低难度)：一篇结构严谨的技术指南极易在 2~4 周冲上首页。
- 🟠 `41 - 60` (中等难度) / 🔴 `61 - 100` (高难度)。

### 3. KGR (Keyword Golden Ratio) 金比率判定 (`kgr.py`)
$$\text{KGR} = \frac{\text{Google Allintitle 搜索结果数}}{\text{月搜索量 Monthly Search Volume}}$$
- 🟢 **KGR < 0.25 (黄金捡钱词)**：全网把该词完整写入 `<title>` 的网页屈指可数，收录后**极速排进前 50 甚至首页前排**！

### 4. 自动生成 Pillar-Cluster 拓扑地图 (`clustering.py`)
一键输出包含 ASCII 拓扑关系图、核心主页规划、卫星子页划分、URL Slug 建议与双向内链锚文本规则的 `topic_cluster_architecture_*.md`。

### 5. 自动生成 B 端采购指南与工程选型大纲 (`content_generator.py`)
自动生成可直接交付编辑团队或海外写手的 Markdown 大纲方案：
- **方案一：B2B 核心采购寻源指南 (Buyer's Sourcing Guide)**
- **方案二：工程选型与材质工艺参数文章 (Technical Specs Guide)**
- **方案三：低竞争开荒长尾词单 (Quick-Win Long-Tail Posts)**

---

## ⚡ 极速上手 (10 秒开箱即用)

```bash
# 1. 克隆仓库
git clone https://github.com/qipihen/google-keyword-planner.git
cd google-keyword-planner
pip install -r requirements.txt

# 2. 一键执行 B 端挖掘与意图集群分析 (免配任何 Key，秒级出词)
python run.py "airless bottle"

# 3. 包含 KGR 计算
python run.py "rotary tablet press" --kgr
```

---

## 📊 终端实测输出样例

```text
======================================================================================
🎯 正在针对 B 端种子词「airless bottle」进行多维度 SEO 智能挖掘与关键词集群分析...
语言: en | 地区: us | 模式: 开箱即用 (官方 API 网关就绪)
======================================================================================
🔍 正在抓取 Google 实时搜索下拉联想词 (融合 A-Z 字母汤与 B2B 采购词库)...
✅ 成功捕获 412 个纯净长尾词！
📡 正在调用内置 Google Ads 官方网关获取真实月搜索量、竞争指数与 CPC 出价...
✨ 官方网关同步成功！获得 856 条 Google Ads 官方精准指标。
🧠 正在执行 B2B 意图识别、难度评估 (B2B-KD) 与商业价值机会评分...

==============================================================================================
排名   | 关键词                                | 月搜索量     | B2B-KD       | 机会评分     | 行动建议
----------------------------------------------------------------------------------------------
1    | custom airless bottle manufacturer   | 110      | 🟢 12 (极低)    | 88       | 【💼 采购寻源·询盘转化必写】
2    | airless pump bottle wholesale low moq | 90       | 🟢 10 (极低)    | 86       | 【💼 采购寻源·询盘转化必写】
3    | airless bottle supplier china        | 140      | 🟢 14 (极低)    | 85       | 【💼 采购寻源·询盘转化必写】
4    | how does an airless pump bottle work | 720      | 🟢 16 (极低)    | 79       | 【📐 选型参数·技术背书长文】
5    | airless cosmetic bottle specifications | 50       | 🟢 11 (极低)    | 76       | 【📐 选型参数·技术背书长文】
6    | airless pump bottle materials guide  | 70       | 🟢 13 (极低)    | 75       | 【📐 选型参数·技术背书长文】
==============================================================================================

🗺️ 正在执行关键词意图集群 (Clustering) 与 Pillar-Cluster 内容拓扑规划...
🏛️ 支柱与集群内容拓扑地图已保存至: output/topic_cluster_architecture_airless_bottle_20261110.md
📊 完整分析数据大表已导出至: output/b2b_keyword_analysis_airless_bottle_20261110.csv
💡 文章大纲方案已保存至: output/content_plan_airless_bottle_20261110.md
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
│   ├── evaluator.py                # B2B 意图分类与难度评估模型 (B2B-KD)
│   ├── clustering.py               # 【核心】关键词集群与 Pillar 拓扑引擎
│   ├── kgr.py                      # KGR (Keyword Golden Ratio) 金比率核算器
│   ├── content_generator.py        # B2B 采购指南与工艺选型大纲生成器
│   ├── official_ads.py             # 官方 API 客户端与 Cloudflare 全球网关
│   └── setup_wizard.py             # 自建官方凭证向导 (可选)
├── references/
│   ├── b2b_pillar_cluster_architecture.md # 意图集群与 Pillar-Cluster 拓扑指南
│   ├── b2b_agency_seo_playbook.md         # 乙方 SEO 操盘 B 端行业实战手册
│   ├── google_cloud_setup_guide.md        # 自建 Google 凭证图文教程
│   └── api_errors_and_limits.md           # 常见报错与排错手册
└── SKILL.md                        # 兼容 Codex / Claude / Cursor 的 Agent Skill
```

---

## 📄 开源许可证

本项目采用 [MIT 许可证](LICENSE)。你可以自由商用、集成到 Agency 内部 SOP 工作流或进行二次分发。
