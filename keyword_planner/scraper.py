#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Google Suggest 核心拓词引擎 (Zero-Token Autocomplete Engine)
免任何 API Key 或登录凭据，实时从 Google 搜索下拉建议框中批量挖掘长尾搜索词。
"""

import os
import re
import time
import random
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from typing import List, Set, Dict, Tuple, Callable, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed

USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15",
]

QUESTIONS = [
    "how to", "what is", "why", "can", "where to", "which", "who", "when", "is", "how do"
]

MODIFIERS = [
    "best", "top", "free", "cheap", "vs", "versus", "for", "with", "without",
    "near me", "online", "tools", "course", "guide", "checklist", "agency",
    "service", "examples", "tips", "strategy", "template", "software", "audit", "generator"
]

ALPHABET = [chr(c) for c in range(ord('a'), ord('z') + 1)]
DIGITS = [str(d) for d in range(0, 10)]


class SuggestScraper:
    def __init__(
        self,
        seed_keyword: str,
        hl: str = "en",
        gl: str = "us",
        num_workers: int = 3,
        exclude_words: Optional[List[str]] = None,
        on_progress: Optional[Callable[[int, str], None]] = None,
    ):
        self.seed = seed_keyword.strip().lower()
        self.hl = hl
        self.gl = gl
        self.num_workers = max(1, min(num_workers, 5))
        self.exclude_words = [w.lower() for w in (exclude_words or [])]
        self.on_progress = on_progress

        # 单词边界严格匹配（中英文通用边界处理）
        if re.match(r'^[a-zA-Z0-9\s]+$', self.seed):
            self.seed_pattern = re.compile(r'\b' + re.escape(self.seed) + r'\b', re.IGNORECASE)
        else:
            self.seed_pattern = re.compile(re.escape(self.seed), re.IGNORECASE)

        self.discovered_keywords: Set[str] = set()
        self.metadata: List[Dict[str, str]] = []

    def fetch_suggestions(self, query: str) -> List[str]:
        """向 Google Suggest 发起请求"""
        url = (
            f"https://suggestqueries.google.com/complete/search?"
            f"output=toolbar&hl={self.hl}&gl={self.gl}&q={urllib.parse.quote(query)}"
        )
        headers = {
            "User-Agent": random.choice(USER_AGENTS),
            "Accept-Language": f"{self.hl};q=0.9,en;q=0.8",
        }
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=7) as resp:
                content = resp.read().decode("utf-8", errors="ignore")
                root = ET.fromstring(content)
                suggestions = []
                for s in root.findall(".//suggestion"):
                    data = s.get("data")
                    if data:
                        suggestions.append(data.strip())
                return suggestions
        except Exception:
            return []

    def is_valid_keyword(self, candidate: str) -> bool:
        cand_lower = candidate.lower()
        if not self.seed_pattern.search(cand_lower):
            return False
        for exc in self.exclude_words:
            if exc in cand_lower:
                return False
        return True

    def build_queries(self) -> List[Tuple[str, str]]:
        """构建专业 SEO 拓词查询组合"""
        queries: List[Tuple[str, str]] = []
        queries.append((self.seed, "seed"))
        queries.append((f"{self.seed} ", "seed_space"))

        # A-Z 字母汤拓词
        for char in ALPHABET:
            queries.append((f"{self.seed} {char}", f"alphabet_suffix_{char}"))
            queries.append((f"{char} {self.seed}", f"alphabet_prefix_{char}"))
        for digit in DIGITS:
            queries.append((f"{self.seed} {digit}", f"digit_{digit}"))

        # 疑问词
        for q in QUESTIONS:
            queries.append((f"{q} {self.seed}", f"question_{q}"))

        # 商业与意图修饰词
        for mod in MODIFIERS:
            queries.append((f"{self.seed} {mod}", f"modifier_suffix_{mod}"))
            queries.append((f"{mod} {self.seed}", f"modifier_prefix_{mod}"))

        return queries

    def harvest(self) -> List[Dict[str, str]]:
        """执行多线程抓取并去重"""
        planned_queries = self.build_queries()
        count = 0

        with ThreadPoolExecutor(max_workers=self.num_workers) as executor:
            future_to_info = {}
            for query, source_type in planned_queries:
                time.sleep(random.uniform(0.08, 0.2))
                future = executor.submit(self.fetch_suggestions, query)
                future_to_info[future] = (query, source_type)

            for future in as_completed(future_to_info):
                query, source_type = future_to_info[future]
                suggestions = future.result()
                for s in suggestions:
                    s_clean = s.strip()
                    if s_clean not in self.discovered_keywords:
                        if self.is_valid_keyword(s_clean):
                            self.discovered_keywords.add(s_clean)
                            self.metadata.append({
                                "keyword": s_clean,
                                "source_query": query,
                                "source_type": source_type,
                            })
                            count += 1
                            if self.on_progress:
                                self.on_progress(count, s_clean)

        return self.metadata
