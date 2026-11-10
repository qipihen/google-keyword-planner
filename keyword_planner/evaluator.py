#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
哥飞 SEO 选词决策引擎 (结合 B2B 工业采购与高客单转化加权)
"""

import re
from typing import Dict, Any, List, Optional, Tuple

INTENT_PATTERNS = {
    # B2B 供应链寻源与大宗采购意图 (极高商业转化价值)
    "B2B Sourcing / RFQ": [
        r"\bmanufacturer\b", r"\bmanufacturers\b", r"\bsupplier\b", r"\bsuppliers\b",
        r"\bfactory\b", r"\bfactories\b", r"\bvendor\b", r"\bvendors\b",
        r"\bwholesale\b", r"\bwholesaler\b", r"\bdistributor\b", r"\bdistributors\b",
        r"\bcustom\b", r"\bcustomized\b", r"\boem\b", r"\bodm\b", r"\bprivate label\b",
        r"\bbulk\b", r"\bmoq\b", r"\brfq\b", r"\bquote\b", r"\bquotation\b",
        r"\blead time\b", r"\bcontract manufacturing\b"
    ],
    # 技术标准与规格选型意图
    "Technical Specs": [
        r"\bspecs\b", r"\bspecification\b", r"\bdatasheet\b", r"\bstandards\b",
        r"\bmaterials\b", r"\bprocess\b", r"\bmanufacturing process\b",
        r"\bhow it works\b", r"\bdiagram\b", r"\bdimensions\b", r"\bcapacity\b",
        r"\biso\b", r"\bce certified\b", r"\bfda\b", r"\bgmp\b"
    ],
    # 商业调查与横评
    "Commercial": [
        r"\bbest\b", r"\btop\b", r"\breview\b", r"\breviews\b", r"\bvs\b",
        r"\bversus\b", r"\bcomparison\b", r"\balternative\b", r"\balternatives\b",
        r"\bworth it\b", r"\branked\b", r"\branking\b", r"\brated\b"
    ],
    # 工具与在线查询
    "Tool": [
        r"\bgenerator\b", r"\bcalculator\b", r"\bmaker\b", r"\bconverter\b",
        r"\bchecker\b", r"\banalyzer\b", r"\btemplate\b", r"\bsoftware\b",
        r"\btool\b", r"\btools\b", r"\bapp\b", r"\bonline free\b", r"\bextension\b"
    ],
    # 信息与基础教程
    "Informational": [
        r"\bhow to\b", r"\bhow do\b", r"\bwhat is\b", r"\bwhat are\b", r"\bwhy\b",
        r"\bcan you\b", r"\bguide\b", r"\btutorial\b", r"\btips\b", r"\bexamples\b",
        r"\bideas\b", r"\bchecklist\b", r"\bmeaning\b", r"\bstrategy\b", r"\blearn\b"
    ]
}


def detect_intent(keyword: str) -> str:
    kw_lower = keyword.lower()
    for intent, patterns in INTENT_PATTERNS.items():
        for pat in patterns:
            if re.search(pat, kw_lower):
                return intent
    return "Informational"


def calculate_gefei_kd(
    keyword: str,
    intent: str,
    google_ads_comp_index: Optional[int] = None,
    allintitle_count: Optional[int] = None
) -> int:
    words = keyword.strip().split()
    word_count = len(words)

    # 1. 基础词长分
    if word_count == 1:
        base_kd = 88
    elif word_count == 2:
        base_kd = 68
    elif word_count == 3:
        base_kd = 46
    elif word_count == 4:
        base_kd = 26
    elif word_count == 5:
        base_kd = 16
    else:
        base_kd = 10

    # 2. 意图修正 (B2B 采购词多属于极具针对性的长尾，优化阻力极易穿透)
    intent_modifier = 0
    if intent == "B2B Sourcing / RFQ":
        intent_modifier -= 6
    elif intent == "Technical Specs":
        intent_modifier -= 4
    elif intent == "Informational" and re.search(r"^(how to|what is|why|can)", keyword.lower()):
        intent_modifier -= 8
    elif intent == "Commercial" and "vs" in keyword.lower():
        intent_modifier -= 6

    # 3. Google Ads 竞价指数修正
    ads_modifier = 0
    if google_ads_comp_index is not None and google_ads_comp_index > 0:
        ads_modifier = int((google_ads_comp_index - 50) * 0.20)

    # 4. Allintitle 修正
    title_modifier = 0
    if allintitle_count is not None:
        if allintitle_count < 10:
            title_modifier = -15
        elif allintitle_count < 50:
            title_modifier = -8
        elif allintitle_count > 500:
            title_modifier = +15

    final_kd = base_kd + intent_modifier + ads_modifier + title_modifier
    return max(5, min(95, final_kd))


def calculate_opportunity_score(
    kd: int,
    intent: str,
    search_volume: int = 0,
    cpc: float = 0.0,
    kgr: Optional[float] = None
) -> Tuple[int, str]:
    ease_score = max(0, 100 - kd)

    # B2B 行业搜索量虽小，单次转化价值数万美金，意图权重极大
    intent_weight = {
        "B2B Sourcing / RFQ": 1.40,
        "Technical Specs": 1.25,
        "Commercial": 1.20,
        "Tool": 1.15,
        "Informational": 1.00
    }.get(intent, 1.0)

    cpc_bonus = min(25.0, cpc * 3.0) if cpc > 0 else 5.0

    # 搜索量平滑曲线 (B2B 黄金月搜区间为 20 ~ 1,500)
    vol_bonus = 10.0
    if search_volume > 0:
        if 20 <= search_volume <= 800:
            vol_bonus = 25.0
        elif 800 < search_volume <= 4000:
            vol_bonus = 18.0
        elif search_volume > 4000:
            vol_bonus = 10.0

    kgr_bonus = 0
    if kgr is not None:
        if kgr < 0.25:
            kgr_bonus = 20
        elif kgr <= 1.0:
            kgr_bonus = 8

    raw_score = (ease_score * 0.50) + (cpc_bonus) + (vol_bonus) + (kgr_bonus)
    final_score = int(min(99, max(10, raw_score * intent_weight * 0.72)))

    # 行动决策与判定
    if intent == "B2B Sourcing / RFQ":
        verdict = "【💼 采购寻源·询盘转化必写】"
    elif intent == "Technical Specs":
        verdict = "【📐 选型参数·技术背书长文】"
    elif intent == "Tool" and kd <= 45:
        verdict = "【🛠️ 选型工具·计算器落地页】"
    elif kgr is not None and kgr < 0.25:
        verdict = "【⚡ 黄金KGR·极速排名前排】"
    elif final_score >= 78:
        verdict = "【🔥 强烈推荐·核心支柱文章】"
    elif final_score >= 60:
        verdict = "【⚡ 优质长尾·易拿下流量】"
    elif final_score >= 45:
        verdict = "【⚖️ 评测对比·可规划排期】"
    else:
        verdict = "【🛑 竞争偏大·不建议首发】"

    return final_score, verdict


def evaluate_keyword_item(
    keyword: str,
    search_volume: int = 0,
    google_ads_comp_index: Optional[int] = None,
    cpc: float = 0.0,
    allintitle_count: Optional[int] = None,
    kgr: Optional[float] = None
) -> Dict[str, Any]:
    intent = detect_intent(keyword)
    kd = calculate_gefei_kd(
        keyword=keyword,
        intent=intent,
        google_ads_comp_index=google_ads_comp_index,
        allintitle_count=allintitle_count
    )
    score, verdict = calculate_opportunity_score(
        kd=kd,
        intent=intent,
        search_volume=search_volume,
        cpc=cpc,
        kgr=kgr
    )

    if kd <= 20:
        kd_badge = f"🟢 {kd} (极低)"
    elif kd <= 40:
        kd_badge = f"🟡 {kd} (低)"
    elif kd <= 60:
        kd_badge = f"🟠 {kd} (中等)"
    else:
        kd_badge = f"🔴 {kd} (高难度)"

    return {
        "keyword": keyword,
        "intent": intent,
        "kd": kd,
        "kd_badge": kd_badge,
        "search_volume": search_volume,
        "cpc": cpc,
        "kgr": kgr,
        "opportunity_score": score,
        "verdict": verdict,
    }
