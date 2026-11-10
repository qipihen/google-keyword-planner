#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B2B 采购与出海文章大纲智能生成器 (B2B Content Strategy & Outline Generator)
解决乙方 SEO 操盘 B 端行业客户时“Semrush 挖不出词、内容团队不知道写什么话题”的痛点。
"""

import re
from typing import List, Dict, Any


def generate_content_plan(
    seed_keyword: str,
    evaluated_keywords: List[Dict[str, Any]],
    top_n: int = 15
) -> str:
    if not evaluated_keywords:
        return "⚠️ 无可用关键词数据，无法生成内容方案。"

    sorted_kws = sorted(evaluated_keywords, key=lambda x: x.get("opportunity_score", 0), reverse=True)

    b2b_kws = [k for k in sorted_kws if k.get("intent") == "B2B Sourcing / RFQ"]
    specs_kws = [k for k in sorted_kws if k.get("intent") == "Technical Specs"]
    comm_kws = [k for k in sorted_kws if k.get("intent") == "Commercial"]
    high_score_kws = sorted_kws[:top_n]

    question_kws = [
        k["keyword"] for k in sorted_kws
        if re.search(r"^(how|what|why|can|where|is|which)", k["keyword"].lower())
    ]

    plan_md = []
    plan_md.append(f"# 🏭 基于「{seed_keyword}」的 B2B 行业 SEO 采购指南与文章大纲方案\n")
    plan_md.append("> 专为 B 端制造外贸、OEM/ODM、工业设备及供应链出海企业量身打造。\n")

    # ---------------- 方案一：B2B 采购寻源指南 (B2B Sourcing & Buyer's Guide) ----------------
    sourcing_kw = b2b_kws[0]["keyword"] if b2b_kws else high_score_kws[0]["keyword"]
    plan_md.append("## 📌 方案一：B2B 核心采购寻源指南 (Buyer's Sourcing Guide)")
    plan_md.append(f"- **目标主词**：`{sourcing_kw}` (意图: B2B Sourcing)")
    plan_md.append(f"- **建议文章 H1 标题**：`How to Source & Buy {seed_keyword.title()}: The Complete B2B Buyer's Guide for Manufacturers & Distributors`")
    plan_md.append("- **商业变现定位**：直接承接海外采购经理、外贸采购总监的询盘 (Inquiry / RFQ)，沉淀高客单转化")
    plan_md.append("- **建议字数**：2,200 ~ 3,500 词")
    plan_md.append("- **章节骨架 (建议 H2 / H3 目录)**：")
    plan_md.append(f"  - **H2: Understanding {seed_keyword.title()}: Types, Applications & Industry Standards**")
    if specs_kws:
        for sk in specs_kws[:3]:
            plan_md.append(f"    - **H3: Key Considerations for {sk['keyword'].title()}**")
    plan_md.append(f"  - **H2: How to Evaluate Reliable {seed_keyword.title()} Manufacturers & Suppliers**")
    plan_md.append("    - H3: Factory Audit & Quality Control (ISO, FDA, CE Standards)")
    plan_md.append("    - H3: MOQ, Pricing Structures & Lead Time Breakdown")
    plan_md.append(f"  - **H2: Custom OEM/ODM Capabilities: Materials, Tooling & Design**")
    if b2b_kws:
        for bk in b2b_kws[1:4]:
            plan_md.append(f"    - **H3: Best Practices for {bk['keyword'].title()}**")
    plan_md.append("  - **H2: Common Pitfalls to Avoid in Overseas Sourcing** (避坑指南与质检要点)")
    plan_md.append("  - **H2: Frequently Asked Procurement Questions (FAQ)** (布局长尾疑问词，获取 Google 首页精选摘要)")
    for qk in question_kws[:4]:
        plan_md.append(f"    - **H3: {qk.capitalize()}?**")
    plan_md.append("\n" + "-" * 70 + "\n")

    # ---------------- 方案二：工程选型与工艺参数对比 (Technical Specs & Material Guide) ----------------
    tech_kw = specs_kws[0]["keyword"] if specs_kws else (comm_kws[0]["keyword"] if comm_kws else high_score_kws[1]["keyword"])
    plan_md.append("## 📌 方案二：工程选型与材质工艺技术长文 (Technical Specification Guide)")
    plan_md.append(f"- **目标主词**：`{tech_kw}`")
    plan_md.append(f"- **建议文章 H1 标题**：`{seed_keyword.title()} Specifications & Selection Guide: Materials, Engineering Process & Comparison`")
    plan_md.append("- **受众定位**：海外产品研发工程师、工艺师、采购技术决策人")
    plan_md.append("- **建议字数**：1,800 ~ 2,600 词")
    plan_md.append("- **章节骨架**：")
    plan_md.append(f"  - **H2: Comprehensive Technical Specifications & Dimensions Table** (置顶核心参数表)")
    plan_md.append(f"  - **H2: Material Selection: Pros and Cons of Different Compounds/Alloys** (材质优劣势横评)")
    plan_md.append(f"  - **H2: Manufacturing Process: From Raw Material to Precision Finished Product** (生产工艺拆解)")
    plan_md.append(f"  - **H2: Testing & Compliance (Stress, Durability & Environmental Standards)** (检测标准与认证)")
    plan_md.append("\n" + "-" * 70 + "\n")

    # ---------------- 方案三：低竞争开荒长尾词与询盘诱饵 (Quick-Win Long-Tail Posts) ----------------
    plan_md.append("## 📌 方案三：新站极速冲刺词单 (Quick-Win Long-Tail Articles)")
    plan_md.append("> 专挑 B2B-KD 最低 (0-20分) 或 KGR < 0.25 的精准采购长尾词，没有头部大站专门做针对性优化，新站发布后能极快获得排名与精准询盘。")
    easy_kws = [k for k in sorted_kws if k.get("kd", 50) <= 25][:6]
    if not easy_kws:
        easy_kws = sorted_kws[:6]
    plan_md.append("- **建议重点开荒的长尾采购词**：")
    for ek in easy_kws:
        plan_md.append(f"  - `{ek['keyword']}` (KD: {ek.get('kd_badge', 'N/A')}, 意图: {ek.get('intent', 'N/A')}, 评分: {ek.get('opportunity_score')})")

    return "\n".join(plan_md)
