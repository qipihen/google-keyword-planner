# 🏢 乙方 SEO 操盘 B 端行业实战手册：为什么 Semrush 找不到了？

> 专门为 SEO 操盘手、出海代运营机构、独立站营销顾问打造的 B 端外贸与工业出海选词攻坚手册。

---

## 一、乙方 SEO 面临的核心困境：Semrush / Ahrefs 为什么在 B 端失灵？

做 B 端客户（例如工业机械、定制包装、化工原料、OEM/ODM 代工、汽车零配件、B2B SaaS）的 SEO 操盘手，几乎都会遇到这个死穴：

### 1. “Semrush 显示 0 搜索量，或者词库枯竭”
- **底层原因**：Semrush、Ahrefs 等三方工具主要依赖 **第三方插件数据收集 (Clickstream 浏览器点击流)** 与历史爬取反推。
- 在 B2C 消费品领域（如 `shoes`, `iphone case`），每天有几万普通网民搜索，Clickstream 样本充足。
- 但在 B 端细分行业（如 `rotary tablet press machine`, `custom airless cosmetic bottle`, `pcba assembly low moq`），全球一个月只有几百或几十个专业采购经理、工厂厂长在搜！第三方工具的采样样本太少，往往直接判定为 `Volume: 0` 或 `No keywords found`，导致乙方团队两三个月后就“词穷”了，文章没法继续排期。

### 2. 客户抱怨“写的文章有流量但没询盘 (Inquiry / RFQ)”
- 内容编辑为了追求 Semrush 上的“搜索量数字”，去写了大量与采购无关的泛科普大词（例如 `what is plastic`, `history of cosmetic bottle`）。
- 带来一堆学生做功课的泛流量，跳出率极高，客户后台一个高质量询盘都没有，合作面临丢单风险。

---

## 二、Google Keyword Planner + Google Suggest 的降维打击优势

为什么 Google Ads 官方数据（GKP）在 B 端行业是无可替代的真正“真源”？

1. **第一手真实竞价拍卖数据 (First-Party Ad Auction Data)**：
   - 即使一个专业工业长尾词一个月只有 30 次搜索，只要曾有海外采购商在 Google 搜索框里敲过这串字符、或有工业品牌在后台出价，Google Keyword Planner 就有**精确记录**！
2. **Google Suggest (实时联想下拉框) 的最新真实搜索意图**：
   - 展现的是**当前真实世界中海外采购商正在输入的完整长尾 query**。
   - 配合 **Alphabet Soup（字母汤拓词）** 与 **B2B 采购修饰词**，能够立刻把 1 个核心词裂变出 300~800 个精准采购话题！
3. **B 端 SEO 的核心公式：转化价值 > 虚荣流量**：
   - 一个消费品词月搜 10 万，客单价 20 美元。
   - 一个工业机械词 `custom pharmaceutical blister packaging machine manufacturer`，月搜只有 50 次，但一个询盘拿下就是 **20 万美金的外贸订单**！

---

## 三、结合哥飞选词体系的 B 端实操 SOP

### 第一步：种子词深挖 (Seed Discovery)
不要直接搜 `packaging`，输入精准品类词：
```bash
python run.py "airless bottle"
```
工具自动叠加：
- 供应链词：`manufacturer`, `supplier`, `factory`, `wholesale`, `oem`, `odm`, `private label`
- 采购决策词：`moq`, `cost`, `quote`, `rfq`, `lead time`, `catalog`
- 选型参数词：`materials`, `specs`, `process`, `iso certified`, `standards`

### 第二步：哥飞 KD 难度筛选 (Pick Low-Hanging Fruits)
- 在生成的 CSV 报表中，优先筛选 **哥飞 KD <= 25** 的词。
- 这类词通常是 4~6 个单词的精准长尾采购词。大厂、平台型聚合站（如 Alibaba、ThomasNet）只会用大目录页做大词，根本不会专门写一篇 3,000 字的长文深入解答这个具体的工艺与选型。
- 新站只要发布一篇结构严谨的技术选型指南，极短时间内就能在 Google 占据前 3 名！

### 第三步：KGR 黄金法则突击 (KGR < 0.25)
- 计算全网 `allintitle` 网页数量。若全网把该长尾词完整放到 `<title>` 里的网页少于 10 个，且该词有几十点精准采购搜索量，这就是无竞争的“捡钱词”。

### 第四步：把文章大纲直接交付客户或内容编辑
工具自动在 `output/content_plan_*.md` 生成了：
- **方案一：B2B 采购寻源指南 (Buyer's Guide)**
- **方案二：技术选型与工艺参数长文 (Technical Specification)**
- **方案三：快速见效长尾文章 (Quick-Win Q&A)**

乙方团队无需再花几小时构思标题与大纲，直接把大纲发给文案或海外写手填肉，生产力直接提升 5 倍以上！
