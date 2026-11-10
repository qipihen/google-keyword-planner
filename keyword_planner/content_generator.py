#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文章选题与 SEO 内容大纲智能生成器 (Content Strategy & Outline Generator)

解决创作者核心痛点：
“想写文章却不知道写什么词？”
“挖出一堆长尾词后，不知道该怎么组合成一篇文章的标题与大纲？”

本模块自动聚类高价值长尾词，生成可直接落地的 H1 文章标题、H2 章节目录架构和 LSI 词布局方案。
"""

import re
from typing import List, Dict, Any


def generate_content_plan(
    seed_keyword: str,
    evaluated_keywords: List[Dict[str, Any]],
    top_n: int = 15
) -> str:
    """基于评估结果，自动提炼出 3 套不同类型的深度文章选题与大纲"""
    if not evaluated_keywords:
        return "⚠️ 无可用关键词数据，无法生成内容方案。"

    # 按机会评分降序
    sorted_kws = sorted(evaluated_keywords, key=lambda x: x.get("opportunity_score", 0), reverse=True)

    info_kws = [k for k in sorted_kws if k.get("intent") == "Informational"]
    comm_kws = [k for k in sorted_kws if k.get("intent") == "Commercial"]
    tool_kws = [k for k in sorted_kws if k.get("intent") == "Tool"]
    high_score_kws = sorted_kws[:top_n]

    # 提取问答词
    question_kws = [k["keyword"] for k in sorted_kws if re.search(r"^(how|what|why|can|where|is)", k["keyword"].lower())]

    plan_md = []
    plan_md.append(f"# ✍️ 基于「{seed_keyword}」的 SEO 文章选题与大纲规划方案\n")
    plan_md.append("> 本方案基于 Google 真实长尾搜索词与哥飞机会评分自动聚类，专为新站突围与高排名前排设计。\n")

    # ---------------- 方案 A：权威支柱长文 (Pillar Post) ----------------
    pillar_kw = high_score_kws[0]["keyword"] if high_score_kws else seed_keyword
    plan_md.append("## 📌 方案一：核心支柱长文 (Pillar Guide)")
    plan_md.append(f"- **目标主词**：`{pillar_kw}` (哥飞KD: {high_score_kws[0].get('kd_badge', 'N/A')})")
    plan_md.append(f"- **建议文章 H1 标题**：`The Ultimate Guide to {seed_keyword.title()}: Strategies, Best Practices, and Tools for Beginners`")
    plan_md.append("- **建议字数**：2,000 ~ 3,500 词")
    plan_md.append("- **章节骨架 (建议 H2 / H3 目录)**：")
    plan_md.append(f"  - **H2: What is {seed_keyword.title()} and Why Does It Matter?** (基础概念铺垫)")
    if question_kws:
        for q in question_kws[:3]:
            plan_md.append(f"    - **H3: {q.capitalize()}?**")
    plan_md.append(f"  - **H2: Step-by-Step Implementation Guide** (核心实操步骤)")
    if len(high_score_kws) > 3:
        for item in high_score_kws[1:4]:
            plan_md.append(f"    - **H3: How to Leverage {item['keyword'].title()}**")
    plan_md.append(f"  - **H2: Essential Tools & Checklists** (工具推荐与排坑)")
    if tool_kws:
        plan_md.append(f"    - **H3: Recommended {tool_kws[0]['keyword'].title()}**")
    plan_md.append(f"  - **H2: Common Mistakes to Avoid** (新手避坑指南)")
    plan_md.append(f"  - **H2: Frequently Asked Questions (FAQ)** (布局精选长尾词获取快速卡片排名)")
    for q in question_kws[3:6]:
        plan_md.append(f"    - **H3: {q.capitalize()}?**")
    plan_md.append("\n" + "-" * 60 + "\n")

    # ---------------- 方案 B：高转化评测与选购对比 (Commercial / VS Post) ----------------
    if comm_kws or len(sorted_kws) > 5:
        target_comm = comm_kws[0]["keyword"] if comm_kws else sorted_kws[1]["keyword"]
        plan_md.append("## 📌 方案二：高转化评测对比文章 (Commercial Roundup)")
        plan_md.append(f"- **目标主词**：`{target_comm}`")
        plan_md.append(f"- **建议文章 H1 标题**：`Best {seed_keyword.title()} in 2026: In-Depth Review, Comparison & Buying Guide`")
        plan_md.append("- **建议字数**：1,500 ~ 2,200 词")
        plan_md.append("- **变现定位**：适合插入联盟营销链接、SaaS 分销推广或自营服务转化")
        plan_md.append("- **章节骨架**：")
        plan_md.append("  - **H2: Quick Verdict: Top Picks at a Glance** (置顶核心推荐对比表)")
        plan_md.append(f"  - **H2: How We Tested and Evaluated {seed_keyword.title()}** (建立可信度与专业度)")
        plan_md.append("  - **H2: Detailed Breakdown of Top Contenders** (每个竞品优缺点深评)")
        plan_md.append("  - **H2: Feature & Pricing Comparison Table** (参数横评矩阵)")
        plan_md.append("  - **H2: Which One Should You Choose?** (按不同人群给出选择建议)")
        plan_md.append("\n" + "-" * 60 + "\n")

    # ---------------- 方案 C：快速见效长尾问答文章 (Quick-Win Q&A) ----------------
    plan_md.append("## 📌 方案三：极速见效长尾文章 (Quick-Win Post)")
    plan_md.append("> 专挑哥飞 KD 最低 (0-20分) 或 KGR < 0.25 的长尾词，极低竞争，发布后极快获得自然排名。")
    easy_kws = [k for k in sorted_kws if k.get("kd", 50) <= 30][:6]
    if not easy_kws:
        easy_kws = sorted_kws[:5]
    plan_md.append("- **精选开荒低竞争长尾词列表**：")
    for ek in easy_kws:
        plan_md.append(f"  - `{ek['keyword']}` (KD: {ek.get('kd_badge', 'N/A')}, 判定: {ek.get('verdict', 'N/A')})")
    plan_md.append("- **写作建议**：针对这些问题直接给出 50~80 词精炼回答，极易触发 Google 首页精选摘要 (Featured Snippets)！")

    return "\n".join(plan_md)
