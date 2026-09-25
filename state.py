from typing import TypedDict


class ResearchState(TypedDict):
    question: str
    search_results: dict
    final_report: list