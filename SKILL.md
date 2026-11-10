---
name: google-keyword-planner
description: "Harvest long-tail keyword ideas, evaluate Gefei KD difficulty and search intent, calculate KGR ratios, and generate SEO article outlines using Google Suggest and official Google Ads API without third-party dependencies."
metadata:
  short-description: Google keyword ideas, KD, KGR, and article outlines
---

# Google Keyword Planner & SEO Intelligence

Harvest long-tail keyword ideas, calculate Gefei-style Keyword Difficulty (KD), determine commercial search intent, compute KGR (Keyword Golden Ratio), and automatically generate click-worthy article outlines and FAQ topics.

## Core Capabilities

1. **Zero-Setup Keyword Expansion (`scraper.py`)**:
   - Zero token / zero API keys required.
   - Harvests hundreds of long-tail search terms directly from Google Suggest.
   - Strict word-boundary matching (`\b{keyword}\b`) prevents topic drift (e.g., `seo` never matches `seoul`).
   - Professional SEO Alphabet Soup (A-Z suffixes/prefixes), question prefixes (how to, what is, why), and commercial modifiers (best, vs, checklist).

2. **Gefei SEO Decision Engine (`evaluator.py`)**:
   - **Search Intent**: Categorizes terms into Informational, Commercial, Tool/Utility, or Transactional.
   - **Heuristic KD (0-100)**: Evaluates term length, intent specificity, competition density, and SERP title resistance.
     - `0-20`: 🟢 Very Easy (ideal for new sites / immediate quick wins)
     - `21-40`: 🟡 Easy (topical authority single posts rank easily)
     - `41-60`: 🟠 Moderate (requires backlinks & topical cluster)
     - `61-100`: 🔴 Hard (dominated by mega sites)
   - **Opportunity Score (0-100)**: Actionable verdict on whether the keyword is worth targeting (`【🔥 强烈推荐·核心文章】`, `【⚡ 优质长尾·易拿下流量】`, `【🛠️ 工具落地页】`, `【🛑 暂缓】`).

3. **KGR (Keyword Golden Ratio) Calculator (`kgr.py`)**:
   - $\text{KGR} = \frac{\text{Allintitle Count}}{\text{Monthly Volume}}$
   - Highlights terms with $\text{KGR} < 0.25$ that can hit page 1 immediately upon indexation.

4. **Instant Article Topic & Outline Generator (`content_generator.py`)**:
   - Solves creator writer's block.
   - Automatically clusters keywords into 3 complete article blueprints:
     - Pillar Post (H1 title, H2/H3 section architecture, FAQ schema targets)
     - Commercial Roundup / Comparison (feature matrices & buying advice)
     - Quick-Win Q&A Posts (targeted at Google Featured Snippets)

## Quick Start Commands

```bash
# Basic run: 100% free, out of the box (zero configuration needed)
python run.py "ai photo generator"

# Run with KGR calculation
python run.py "crochet pattern" --kgr

# Target specific language and region
python run.py "独立站" --hl zh-CN --gl cn

# Configure official Google Ads API credentials (interactive wizard)
python run.py --setup

# Direct official Google Ads metrics
python run.py "seo audit" --official
```

## References

- For Gefei's keyword selection methodology, read [references/gefei_seo_methodology.md](references/gefei_seo_methodology.md).
- For free Google Cloud OAuth setup, read [references/google_cloud_setup_guide.md](references/google_cloud_setup_guide.md).
- For API error troubleshooting, read [references/api_errors_and_limits.md](references/api_errors_and_limits.md).
