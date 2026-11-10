"""
Google Keyword Planner & B2B SEO Intelligence Toolkit
专业的 B2B 工业出海与供应链长尾词挖掘、意图集群划分与 Pillar-Cluster 内容拓扑构建利器。
"""

__version__ = "1.2.0"
__author__ = "Open Source Community"

from .scraper import SuggestScraper
from .evaluator import evaluate_keyword_item, calculate_gefei_kd, calculate_opportunity_score
from .kgr import calculate_kgr
from .content_generator import generate_content_plan
from .clustering import TopicClusterEngine
