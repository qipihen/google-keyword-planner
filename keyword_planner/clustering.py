#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B2B 关键词智能集群与支柱拓扑引擎 (B2B Keyword Clustering & Pillar-Cluster Engine)

核心原理：
在现代 Google 算法（Hummingbird, RankBrain, MUM）与 B 端采购决策模型下，
单篇零散关键词文章几乎无法建立权威度（Topical Authority）。
海外采购经理与工程师在搜索时，遵循完整的心智决策链路：
  认知与规格选型 (TOFU) -> 材质工艺对比 (MOFU) -> 供应商寻源/核价/询盘 (BOFU)

本模块将挖掘出的海量长尾词自动进行双层聚类：
1. 第一层：搜索意图集群 (Search Intent Clusters)
2. 第二层：核心支柱 (Pillar) 与 卫星集群 (Cluster Sub-pages) 拓扑映射，并规划双向内链闭环。
"""

import re
from collections import defaultdict
from typing import List, Dict, Any, Tuple


class TopicClusterEngine:
    def __init__(self, seed_keyword: str, evaluated_keywords: List[Dict[str, Any]]):
        self.seed = seed_keyword.strip()
        self.keywords = evaluated_keywords

    def cluster_by_intent(self) -> Dict[str, List[Dict[str, Any]]]:
        """按 B2B 核心意图将词库分组"""
        clusters = defaultdict(list)
        for item in self.keywords:
            intent = item.get("intent", "Informational")
            clusters[intent].append(item)
        return dict(clusters)

    def extract_subtopic_clusters(self) -> Dict[str, Dict[str, Any]]:
        """
        基于语义和实体特征，构建 5 大战略级 B2B 话题集群 (Sub-topic Clusters)
        """
        cluster_rules = {
            "Sourcing & Procurement": {
                "title": f"B2B 供应商寻源与采购商机集群 (Sourcing & RFQ)",
                "role": "BOFU (漏斗底端·直接转化询盘)",
                "url_slug": f"/{self.seed.lower().replace(' ', '-')}-manufacturers-suppliers/",
                "patterns": [r"manufacturer", r"supplier", r"factory", r"wholesale", r"oem", r"odm", r"custom", r"bulk", r"moq", r"vendor", r"rfq", r"cost", r"price", r"quote"],
                "keywords": []
            },
            "Technical Specs & Engineering": {
                "title": f"技术参数、材质与工程选型集群 (Specs & Engineering)",
                "role": "MOFU (漏斗中端·工程师技术背书)",
                "url_slug": f"/{self.seed.lower().replace(' ', '-')}-specifications-materials/",
                "patterns": [r"spec", r"dimension", r"material", r"process", r"drawing", r"diagram", r"standard", r"iso", r"fda", r"ce", r"size", r"capacity", r"cad"],
                "keywords": []
            },
            "Product Comparison & Evaluation": {
                "title": f"竞品横评与品类对比集群 (Comparison & Versus)",
                "role": "MOFU/BOFU (采购选型评估)",
                "url_slug": f"/{self.seed.lower().replace(' ', '-')}-vs-alternatives/",
                "patterns": [r"vs", r"versus", r"difference", r"comparison", r"best", r"top", r"types of", r"review", r"alternative"],
                "keywords": []
            },
            "How-to & Process Guide": {
                "title": f"工艺流程与操作指南集群 (How-to & Workflows)",
                "role": "TOFU (漏斗顶端·行业认知与自然流量入口)",
                "url_slug": f"/how-{self.seed.lower().replace(' ', '-')}-works-guide/",
                "patterns": [r"how to", r"how do", r"how it works", r"why", r"guide", r"tutorial", r"step by step", r"principle"],
                "keywords": []
            },
            "Troubleshooting & Maintenance": {
                "title": f"故障排查、保养与避坑指南 (Troubleshooting & FAQs)",
                "role": "TOFU/MOFU (长尾问答·专攻精选摘要 Featured Snippets)",
                "url_slug": f"/{self.seed.lower().replace(' ', '-')}-troubleshooting-maintenance/",
                "patterns": [r"clean", r"maintain", r"problem", r"troubleshoot", r"fix", r"defect", r"error", r"safe", r"leak", r"stuck"],
                "keywords": []
            }
        }

        matched_kws = set()

        for item in self.keywords:
            kw = item["keyword"].lower()
            matched = False
            for c_key, c_info in cluster_rules.items():
                for pat in c_info["patterns"]:
                    if re.search(r"\b" + pat, kw):
                        c_info["keywords"].append(item)
                        matched_kws.add(kw)
                        matched = True
                        break
                if matched:
                    break

        # 兜底放入未匹配词
        other_kws = [item for item in self.keywords if item["keyword"].lower() not in matched_kws]
        if other_kws:
            cluster_rules["Long-tail Opportunities"] = {
                "title": f"其他高潜力长尾词扩展池 (Extended Long-tails)",
                "role": "卫星长尾扩展",
                "url_slug": f"/{self.seed.lower().replace(' ', '-')}-faq-resources/",
                "patterns": [],
                "keywords": other_kws
            }

        return cluster_rules

    def generate_pillar_cluster_blueprint(self) -> str:
        """生成详细的「核心支柱 (Pillar) - 卫星集群 (Cluster)」内容拓扑与内链映射文档"""
        subtopics = self.extract_subtopic_clusters()

        # 挑选机会分最高的作为 Pillar 核心主词
        sorted_all = sorted(self.keywords, key=lambda x: x.get("opportunity_score", 0), reverse=True)
        pillar_main_kw = sorted_all[0]["keyword"] if sorted_all else self.seed

        lines = []
        lines.append(f"# 🏛️「{self.seed.title()}」B2B 关键词集群与 Pillar-Cluster 内容架构拓扑图\n")
        lines.append("> 架构说明：单篇散写无法对抗大站，必须建立「1 篇核心支柱页 (Pillar) + N 篇卫星集群页 (Clusters)」的双向内链闭环，构建绝对的主题权威度 (Topical Authority)。\n")

        # 1. 拓扑拓扑关系图 (ASCII)
        lines.append("## 🗺️ 支柱与集群内容拓扑架构 (Topic Cluster Topology)")
        lines.append("```text")
        lines.append(f"               ┌────────────────────────────────────────────────────────┐")
        lines.append(f"               │       【核心支柱主页 (Core Pillar Hub)】                │")
        lines.append(f"               │  Title: The Complete B2B Guide to {self.seed.title():<21}│")
        lines.append(f"               │  Target: {pillar_main_kw:<44} │")
        lines.append(f"               │  Role: 统领行业全局、高权重大词、承接采购询盘总入口    │")
        lines.append(f"               └──────────────────────────┬─────────────────────────────┘")
        lines.append(f"                                          │ 双向内链 (Contextual Links)")
        lines.append(f"          ┌───────────────────────────────┼───────────────────────────────┐")
        lines.append(f"          ▼                               ▼                               ▼")
        lines.append(f"  ┌───────────────┐               ┌───────────────┐               ┌───────────────┐")
        lines.append(f"  │ 卫星集群页 1  │               │ 卫星集群页 2  │               │ 卫星集群页 3  │")
        lines.append(f"  │ Sourcing/RFQ  │               │ Specs/Param   │               │ Comparisons   │")
        lines.append(f"  │ 采购寻源与MOQ │               │ 规格材质选型  │               │ 竞品评测横评  │")
        lines.append(f"  └───────┬───────┘               └───────┬───────┘               └───────┬───────┘")
        lines.append(f"          │                               │                               │")
        lines.append(f"          └───────────────────────────────┴───────────────────────────────┘")
        lines.append(f"               ▲                                                          ▲")
        lines.append(f"  ┌────────────┴──┐                                               ┌───────┴───────┐")
        lines.append(f"  │ 卫星集群页 4  │                                               │ 卫星集群页 5  │")
        lines.append(f"  │ How-to/Process│ ◀──────────── 相互交叉支撑链接 ────────────▶  │Troubleshoot/QA│")
        lines.append(f"  │ 原理与制造工艺│                                               │保养与避坑指南 │")
        lines.append(f"  └───────────────┘                                               └───────────────┘")
        lines.append("```\n")

        # 2. 核心支柱页规划
        lines.append("## 🌟 核心支柱页面设计 (The Pillar Page)")
        lines.append(f"- **页面定位**：全站权威枢纽 (Topical Authority Hub)。聚合该品类全生命周期的核心问题，直接承接海外大客户与采购经理的顶级入口。")
        lines.append(f"- **目标主词**：`{pillar_main_kw}` (评分: {sorted_all[0].get('opportunity_score', 'N/A')}, KD: {sorted_all[0].get('kd_badge', 'N/A')})")
        lines.append(f"- **建议 URL Slug**：`/{self.seed.lower().replace(' ', '-')}/` 或 `/{self.seed.lower().replace(' ', '-')}-guide/`")
        lines.append(f"- **建议 H1 标题**：`The Definitive Guide to {self.seed.title()}: Engineering, Custom Sourcing & Buyer's Guide`")
        lines.append(f"- **内链建设规则**：支柱页在每一个章节（选型、材质、工艺、常见问题）中，通过锚文本**精准链接到下方对应的各卫星集群页**。")
        lines.append("\n" + "-" * 75 + "\n")

        # 3. 卫星集群页面规划
        lines.append("## 🛰️ 卫星集群页面规划 (Cluster Sub-Pages & Keywords)")
        cluster_idx = 1
        for c_key, c_info in subtopics.items():
            kws = c_info["keywords"]
            if not kws:
                continue

            sorted_kws = sorted(kws, key=lambda x: x.get("opportunity_score", 0), reverse=True)
            primary_kw = sorted_kws[0]["keyword"]

            lines.append(f"### 📍 集群 {cluster_idx}：{c_info['title']}")
            lines.append(f"- **漏斗定位**：`{c_info['role']}`")
            lines.append(f"- **建议 URL**：`{c_info['url_slug']}`")
            lines.append(f"- **核心主词 (Target Keyword)**：`{primary_kw}` (KD: {sorted_kws[0].get('kd_badge', 'N/A')}, 机会分: {sorted_kws[0].get('opportunity_score', 'N/A')})")
            lines.append(f"- **内链回流策略**：文章第一段首屏及正文中，**必须包含指向核心支柱页 (Pillar) 的锚文本链接**，同时与相邻集群页形成网状互相引用。")
            lines.append(f"- **该集群覆盖的精准长尾词库 (共 {len(kws)} 个)**：")

            for kw_item in sorted_kws[:12]:
                vol = f"月搜: {kw_item['search_volume']}" if kw_item.get('search_volume') else "长尾精选"
                lines.append(f"  - `{kw_item['keyword']}` | {vol} | KD: {kw_item.get('kd_badge', 'N/A')} | 建议: {kw_item.get('verdict', 'N/A')}")

            if len(sorted_kws) > 12:
                lines.append(f"  - *... 及其他 {len(sorted_kws) - 12} 个同集群拓展词*")

            lines.append("\n")
            cluster_idx += 1

        lines.append("-" * 75 + "\n")
        lines.append("## 🔗 为什么必须做双向内链闭环 (Internal Linking Rules)？")
        lines.append("1. **权重流动闭环**：卫星集群页面由于长尾词难度低（KD 5~20），能快速从 Google 获取初始搜索排名并赚取权重（Link Equity）；通过内链向上输送给核心支柱页，让大词水涨船高。")
        lines.append("2. **拒绝孤岛页面 (Orphan Pages)**：任何集群文章都不能孤立存在，确保 Google 蜘蛛能顺着内链爬遍整个品类拓扑。")
        lines.append("3. **转化率漏斗 (Funnel Optimization)**：读者哪怕从一个保养排查词（How-to）进站，也能通过内链一步跳转到 B2B Sourcing 询盘着陆页，大幅提高留资询盘率。")

        return "\n".join(lines)
