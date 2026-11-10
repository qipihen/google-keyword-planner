#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Google Keyword Planner & SEO Intelligence CLI (开源开箱即用主入口)

功能：
1. 零门槛免 Token 智能拓词 (Google Suggest Autocomplete 算法)
2. 内置 Google Ads 官方数据网关 (免配 Key，自动获取真实月搜索量、竞争指数、建议出价 CPC)
3. 哥飞 SEO 选词方法论：启发式 KD 难度评估 (0-100) + 意图识别 (Informational/Commercial/Tool/Transactional)
4. 商业机会评分与“值不值得做”行动决策判定
5. KGR (Keyword Golden Ratio) 金比率自动核算
6. 文章选题与高排名内容大纲 (H1/H2/H3/FAQ) 自动生成
"""

import os
import sys
import argparse
from datetime import datetime

from keyword_planner.scraper import SuggestScraper
from keyword_planner.evaluator import evaluate_keyword_item
from keyword_planner.kgr import calculate_kgr
from keyword_planner.content_generator import generate_content_plan
from keyword_planner.setup_wizard import run_setup
from keyword_planner.official_ads import fetch_keyword_ideas_official


def main():
    parser = argparse.ArgumentParser(
        description="Google Keyword Planner & SEO Intelligence Toolkit (开源开箱即用版)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例：
  python run.py "ai photo generator"          # 极速拓词 + 官方搜索量/CPC + 哥飞KD + 选题大纲 (免配 Key)
  python run.py "crochet pattern" --kgr       # 包含 KGR 金比率计算
  python run.py "独立站" --hl zh-CN --gl cn    # 中文与特定地区市场
  python run.py --suggest-only "seo"          # 仅使用 Google Suggest 纯本地模式
  python run.py --setup                       # 启动自建官方 Google Ads 凭据向导 (可选)
        """
    )
    parser.add_argument("keyword", nargs="?", default=None, help="目标主关键词或种子词 (例如 'seo tools', 'ai photo')")
    parser.add_argument("--hl", default="en", help="语言代码 (默认: en, 可选: zh-CN, ja, de, etc.)")
    parser.add_argument("--gl", default="us", help="地区代码 (默认: us, 可选: cn, uk, jp, etc.)")
    parser.add_argument("--workers", type=int, default=3, help="并发线程数 (默认: 3)")
    parser.add_argument("--kgr", action="store_true", help="是否计算 KGR (Keyword Golden Ratio)")
    parser.add_argument("--suggest-only", action="store_true", help="仅使用 Google Suggest 纯本地拓词，不请求官方搜索量数据")
    parser.add_argument("--setup", action="store_true", help="运行 Google Ads 官方凭据配置向导 (自建模式)")
    parser.add_argument("--output_dir", default="output", help="结果保存目录 (默认: output)")

    args = parser.parse_args()

    if args.setup:
        run_setup()
        return

    keyword = args.keyword
    if not keyword:
        try:
            keyword = input("👉 请输入要挖掘和分析的种子关键词: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n已取消")
            return

    if not keyword:
        print("❌ 错误：关键词不能为空")
        return

    os.makedirs(args.output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = "".join(c if c.isalnum() else "_" for c in keyword)[:30]

    print("=" * 82)
    print(f"🎯 正在针对种子词「{keyword}」进行多维度 SEO 智能挖掘与机会分析...")
    print(f"语言: {args.hl} | 地区: {args.gl} | 模式: 开箱即用 (官方 API 网关就绪)")
    print("=" * 82)

    # 1. 拓词阶段 (Google Suggest)
    scraper = SuggestScraper(
        seed_keyword=keyword,
        hl=args.hl,
        gl=args.gl,
        num_workers=args.workers,
    )
    print("🔍 正在抓取 Google 实时搜索下拉联想词...")
    harvested_meta = scraper.harvest()
    raw_keywords = [item["keyword"] for item in harvested_meta]
    if keyword.lower() not in [k.lower() for k in raw_keywords]:
        raw_keywords.insert(0, keyword.lower())

    print(f"✅ 成功捕获 {len(raw_keywords)} 个纯净长尾词！")

    # 2. 官方 Google Ads 搜索量与出价数据同步
    official_data = {}
    if not args.suggest_only:
        print("📡 正在调用内置 Google Ads 官方网关获取真实月搜索量、竞争指数与 CPC 出价...")
        res = fetch_keyword_ideas_official([keyword], language_id="1000" if args.hl == "en" else "1017")
        if "results" in res and res["results"]:
            print(f"✨ 官方网关同步成功！获得 {len(res['results'])} 条 Google Ads 官方精准指标。")
            for item in res["results"]:
                txt = item.get("text", "").lower()
                m = item.get("keywordIdeaMetrics", {})
                vol = int(m.get("avgMonthlySearches", 0))
                c_idx = int(m.get("competitionIndex", 0))
                comp = m.get("competition", "")
                high_bid = int(m.get("highTopOfPageBidMicros", 0)) / 1_000_000
                official_data[txt] = {
                    "volume": vol,
                    "comp_idx": c_idx,
                    "competition": comp,
                    "cpc": high_bid
                }
                # 如果是新的高价值词，也纳入候选
                if txt not in [k.lower() for k in raw_keywords]:
                    raw_keywords.append(txt)

    # 3. 哥飞指标与 KGR 评估
    evaluated_results = []
    print("🧠 正在执行哥飞 SEO 难度算法评估 (KD) 与商业价值机会评分...")
    for kw in raw_keywords:
        kw_info = official_data.get(kw.lower(), {})
        vol = kw_info.get("volume", 0)
        cpc = kw_info.get("cpc", 0.0)
        c_idx = kw_info.get("comp_idx")

        kgr_val = None
        if args.kgr:
            kgr_val, _, _ = calculate_kgr(kw, vol if vol > 0 else 500)

        ev = evaluate_keyword_item(
            keyword=kw,
            search_volume=vol,
            google_ads_comp_index=c_idx,
            cpc=cpc,
            kgr=kgr_val
        )
        evaluated_results.append(ev)

    # 4. 排序：按机会评分降序
    evaluated_results.sort(key=lambda x: x.get("opportunity_score", 0), reverse=True)

    # 5. 终端美观打印 Top 20
    print("\n" + "=" * 90)
    print(f"{'排名':<4} | {'关键词':<32} | {'月搜索量':<8} | {'哥飞KD':<12} | {'机会评分':<8} | {'行动建议'}")
    print("-" * 90)
    for idx, item in enumerate(evaluated_results[:20], 1):
        vol_str = f"{item['search_volume']:,d}" if item['search_volume'] > 0 else "-"
        print(f"{idx:<4} | {item['keyword']:<32} | {vol_str:<8} | {item['kd_badge']:<12} | {item['opportunity_score']:<8} | {item['verdict']}")
    print("=" * 90)

    # 6. 保存评估 CSV
    csv_file = os.path.join(args.output_dir, f"gefei_seo_analysis_{safe_name}_{timestamp}.csv")
    with open(csv_file, "w", encoding="utf-8") as f:
        f.write("keyword,intent,gefei_kd,opportunity_score,search_volume,cpc,kgr,verdict\n")
        for r in evaluated_results:
            clean_kw = r["keyword"].replace('"', '""')
            kgr_str = f"{r['kgr']:.3f}" if r['kgr'] is not None else ""
            f.write(f'"{clean_kw}","{r["intent"]}",{r["kd"]},{r["opportunity_score"]},{r["search_volume"]},{r["cpc"]},{kgr_str},"{r["verdict"]}"\n')
    print(f"📊 完整分析数据大表已导出至: {csv_file}")

    # 7. 生成文章选题与大纲方案
    print("\n📝 正在基于高分长尾词为您自动聚类并生成「文章选题与大纲方案」...")
    content_plan = generate_content_plan(keyword, evaluated_results)
    plan_file = os.path.join(args.output_dir, f"content_plan_{safe_name}_{timestamp}.md")
    with open(plan_file, "w", encoding="utf-8") as f:
        f.write(content_plan)
    print(f"💡 文章选题与大纲已保存至: {plan_file}")

    print("\n" + "=" * 82)
    print("🎉 恭喜！全流程选词、KD难度评估与文章策划已完成！可以直接使用导出的方案写文章或建站。")
    print("=" * 82)


if __name__ == "__main__":
    main()
