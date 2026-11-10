#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
哥飞 SEO 选词决策与机会评估引擎 (Gefei SEO Decision Engine)

核心方法论：
1. 【搜索意图分类 (Search Intent)】：
   - Informational (信息型/教程): 适合写自然引流文章、FAQ、教程。
   - Commercial (商业调查/评测): 适合做产品横评、Best 榜单、对比页，转化率极高。
   - Transactional (交易/服务): 转化意愿最强，适合直接落地页或销售转化。
   - Tool/Utility (工具/落地页): 搜索量大、粘性高，适合做免费轻量小工具或程序化页面。

2. 【哥飞版启发式 KD 难度评估 (0-100)】：
   - 考虑词长与长尾结构、意图特异性、修饰词阻力与官方竞价指数。
   - 0-20分：极低难度（新站闭眼写，几乎无专门针对该词优化的竞品）
   - 21-40分：低难度（写一篇结构完整、解答深刻的单篇内容极易冲上前排）
   - 41-60分：中等难度（需要一定网站权重与外链积累）
   - 61-100分：高难度（行业大站/维基百科/聚合页盘踞，新手避坑）

3. 【“值不值得做”综合机会评分 (Opportunity Score 0-100)】：
   - 权衡“流量规模 × 商业变现价值 ÷ 竞争阻力”，给出明确的行动建议。
"""

import re
from typing import Dict, Any, List, Optional, Tuple

INTENT_PATTERNS = {
    "Transactional": [
        r"\bbuy\b", r"\bpurchase\b", r"\bcheap\b", r"\bdiscount\b", r"\bcoupon\b",
        r"\bpricing\b", r"\bprice\b", r"\bcost\b", r"\border\b", r"\bhire\b",
        r"\bquote\b", r"\bdeal\b", r"\bsale\b", r"\bwholesale\b", r"\bagency\b",
        r"\bservice\b", r"\bfor sale\b"
    ],
    "Commercial": [
        r"\bbest\b", r"\btop\b", r"\breview\b", r"\breviews\b", r"\bvs\b",
        r"\bversus\b", r"\bcomparison\b", r"\balternative\b", r"\balternatives\b",
        r"\bworth it\b", r"\branked\b", r"\branking\b", r"\brated\b"
    ],
    "Tool": [
        r"\bgenerator\b", r"\bcalculator\b", r"\bmaker\b", r"\bconverter\b",
        r"\bchecker\b", r"\banalyzer\b", r"\btemplate\b", r"\bsoftware\b",
        r"\btool\b", r"\btools\b", r"\bapp\b", r"\bonline free\b", r"\bextension\b"
    ],
    "Informational": [
        r"\bhow to\b", r"\bhow do\b", r"\bwhat is\b", r"\bwhat are\b", r"\bwhy\b",
        r"\bcan you\b", r"\bguide\b", r"\btutorial\b", r"\btips\b", r"\bexamples\b",
        r"\bideas\b", r"\bchecklist\b", r"\bmeaning\b", r"\bstrategy\b", r"\blearn\b"
    ]
}


def detect_intent(keyword: str) -> str:
    """判定关键词的主要搜索意图"""
    kw_lower = keyword.lower()
    for intent, patterns in INTENT_PATTERNS.items():
        for pat in patterns:
            if re.search(pat, kw_lower):
                return intent
    return "Informational"  # 默认倾向于信息型搜索


def calculate_gefei_kd(
    keyword: str,
    intent: str,
    google_ads_comp_index: Optional[int] = None,
    allintitle_count: Optional[int] = None
) -> int:
    """
    计算哥飞版启发式 KD (0-100)
    结合词长效应、意图特异性、竞价竞争指数与 Allintitle 密度
    """
    words = keyword.strip().split()
    word_count = len(words)

    # 1. 基础词长分：词越长，长尾程度越高，全网针对性优化越少
    if word_count == 1:
        base_kd = 88
    elif word_count == 2:
        base_kd = 68
    elif word_count == 3:
        base_kd = 46
    elif word_count == 4:
        base_kd = 28
    elif word_count == 5:
        base_kd = 18
    else:
        base_kd = 12

    # 2. 意图修正：特异性强的疑问词、对比词容易突破
    intent_modifier = 0
    if intent == "Informational" and re.search(r"^(how to|what is|why|can)", keyword.lower()):
        intent_modifier -= 8
    elif intent == "Commercial" and "vs" in keyword.lower():
        intent_modifier -= 6
    elif intent == "Transactional":
        intent_modifier += 5  # 商业交易词做竞价与SEO的对手相对更多

    # 3. Google Ads 官方竞争指数融合 (0-100)
    ads_modifier = 0
    if google_ads_comp_index is not None and google_ads_comp_index > 0:
        # 竞价竞争指数往往与 SEO 竞争正相关，但长尾词中竞价与自然排名有差
        ads_modifier = int((google_ads_comp_index - 50) * 0.25)

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
    """
    计算“值不值得做”综合机会评分 (Opportunity Score 0-100) 与决策判定
    """
    # 难度阻力分 (100 - KD)
    ease_score = max(0, 100 - kd)

    # 商业价值权重
    intent_weight = {
        "Transactional": 1.25,
        "Commercial": 1.20,
        "Tool": 1.15,
        "Informational": 1.00
    }.get(intent, 1.0)

    # CPC 加权 (高出价意味着高收益潜力)
    cpc_bonus = min(20.0, cpc * 2.5) if cpc > 0 else 5.0

    # 搜索量适中加分 (50~2000 的词新站性价比最高)
    vol_bonus = 10.0
    if search_volume > 0:
        if 50 <= search_volume <= 1500:
            vol_bonus = 20.0
        elif 1500 < search_volume <= 8000:
            vol_bonus = 15.0
        elif search_volume > 8000:
            vol_bonus = 8.0  # 大词难啃，加分反而克制

    # KGR 奖励
    kgr_bonus = 0
    if kgr is not None:
        if kgr < 0.25:
            kgr_bonus = 15
        elif kgr <= 1.0:
            kgr_bonus = 5

    raw_score = (ease_score * 0.55) + (cpc_bonus) + (vol_bonus) + (kgr_bonus)
    final_score = int(min(99, max(10, raw_score * intent_weight * 0.75)))

    # 行动建议与判定
    if intent == "Tool" and kd <= 45:
        verdict = "【🛠️ 工具落地页·程序化】"
    elif kgr is not None and kgr < 0.25:
        verdict = "【⚡ 黄金KGR·极速排名前排】"
    elif final_score >= 80:
        verdict = "【🔥 强烈推荐·核心文章必写】"
    elif final_score >= 65:
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
    """对单条关键词执行全面哥飞指标评估"""
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

    # KD 视觉分级
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
