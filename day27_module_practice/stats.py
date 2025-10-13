from typing import Dict, List, Tuple
from collections import defaultdict
from statistics import mean
from models import StudySession

def summarize_by_topic(sessions: List[StudySession]) -> Dict[str, Dict[str, float]]:
    agg: Dict[str, List[int]] = defaultdict(list)
    for s in sessions:
        mins = s.duration_minutes()
        if mins is not None:
            agg[s.topic].append(mins)

    summary: Dict[str, Dict[str, float]] = {}
    for topic, mins_list in agg.items():
        total = sum(mins_list)
        avg = mean(mins_list) if mins_list else 0.0
        count = len(mins_list)
        summary[topic] = {
            "count": float(count),
            "total_min": float(total),
            "avg_min": float(round(avg, 2)),
        }
    return summary

def top_topics_by_total(summary: Dict[str, Dict[str, float]], n: int = 3) -> List[Tuple[str, float]]:
    items = [(k, v["total_min"]) for k, v in summary.items()]
    items.sort(key=lambda x: x[1], reverse=True)
    return items[:n]