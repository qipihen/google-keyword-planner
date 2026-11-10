---
name: google-keyword-planner
description: "Harvest B2B long-tail keywords, categorize B2B procurement search intent, evaluate B2B-KD difficulty, calculate KGR ratios, cluster keywords into topic clusters, and generate Pillar-Cluster content architecture."
metadata:
  short-description: B2B keyword clustering, Pillar-Cluster topology, and Google Ads metrics
---

# Google Keyword Planner & B2B SEO Intelligence

Harvest B2B long-tail keyword ideas, categorize search intent across the B2B procurement lifecycle, calculate B2B-KD difficulty scores, compute KGR ratios, cluster keywords into topic clusters, and automatically generate Pillar-Cluster content architecture and buyer's guide outlines.

## Core Capabilities

1. **B2B Keyword Sourcing Expansion (`scraper.py` + `b2b_config.py`)**:
   - Zero token / zero API keys required.
   - Harvests hundreds of long-tail search terms directly from Google Suggest.
   - Strict word-boundary matching (`\b{keyword}\b`) prevents topic drift.
   - Features B2B supply chain, manufacturing, OEM/ODM, MOQ, RFQ, and engineering specification modifiers.

2. **B2B Intent & Opportunity Engine (`evaluator.py`)**:
   - **Search Intent**: Categorizes terms into B2B Sourcing / RFQ, Technical Specs, Product Comparison, Tool/Utility, or Informational.
   - **B2B-KD Difficulty (0-100)**: Evaluates term length, intent specificity, competition density, and SERP title resistance.
     - `0-20`: 🟢 Very Easy (ideal for new sites / immediate quick wins)
     - `21-40`: 🟡 Easy (topical authority single posts rank easily)
     - `41-60`: 🟠 Moderate (requires backlinks & topical cluster)
     - `61-100`: 🔴 Hard (dominated by mega sites)

3. **Keyword Clustering & Pillar-Cluster Architecture (`clustering.py`)**:
   - Groups terms into 5 strategic procurement clusters: Sourcing/RFQ, Specs/Engineering, Comparisons, How-to/Process, and Maintenance.
   - Automatically generates ASCII topology diagrams, Core Pillar Page blueprint, Cluster Sub-pages mapping, and bidirectional internal linking rules.

4. **KGR (Keyword Golden Ratio) Calculator (`kgr.py`)**:
   - $\text{KGR} = \frac{\text{Allintitle Count}}{\text{Monthly Volume}}$
   - Highlights low-competition terms with $\text{KGR} < 0.25$ that can achieve early page 1 rankings.

5. **B2B Buyer's Guide & Content Outline Generator (`content_generator.py`)**:
   - Generates 3 complete article blueprints:
     - B2B Buyer's Sourcing Guide (H1 title, factory audit, MOQ pricing, FAQ schema)
     - Technical Specification Guide (dimensions, materials, engineering workflows)
     - Quick-Win Procurement Posts

## Quick Start Commands

```bash
# Basic run: 100% free, out of the box (zero configuration needed)
python run.py "airless bottle"

# Run with KGR calculation
python run.py "rotary tablet press" --kgr

# Target specific language and region
python run.py "injection molding" --hl en --gl uk
```

## References

- For B2B Intent Clustering and Pillar-Cluster architecture, read [references/b2b_pillar_cluster_architecture.md](references/b2b_pillar_cluster_architecture.md).
- For Agency B2B SEO operational SOP, read [references/b2b_agency_seo_playbook.md](references/b2b_agency_seo_playbook.md).
- For free Google Cloud OAuth setup, read [references/google_cloud_setup_guide.md](references/google_cloud_setup_guide.md).
- For API error troubleshooting, read [references/api_errors_and_limits.md](references/api_errors_and_limits.md).
