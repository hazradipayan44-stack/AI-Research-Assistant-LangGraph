from langgraph.graph import StateGraph, START, END

from state import ResearchState
from tools import search_web


# ==========================================
# NODE 1: WEB RESEARCH
# ==========================================

def research_node(state: ResearchState):

    question = state["question"]

    print("Searching the web...")

    search_results = search_web(question)

    return {
        "search_results": search_results
    }


# ==========================================
# NODE 2: PREPARE RESEARCH REPORT
# ==========================================

def report_node(state: ResearchState):

    search_results = state["search_results"]

    results = search_results.get("results", [])

    final_report = []

    for result in results:

        final_report.append(
            {
                "title": result.get(
                    "title",
                    "Untitled"
                ),
                "content": result.get(
                    "content",
                    "No information available."
                ),
                "url": result.get(
                    "url",
                    ""
                )
            }
        )

    return {
        "final_report": final_report
    }


# ==========================================
# CREATE LANGGRAPH
# ==========================================

graph_builder = StateGraph(ResearchState)


# Add nodes
graph_builder.add_node(
    "research",
    research_node
)

graph_builder.add_node(
    "report",
    report_node
)


# ==========================================
# ADD EDGES
# ==========================================

graph_builder.add_edge(
    START,
    "research"
)

graph_builder.add_edge(
    "research",
    "report"
)

graph_builder.add_edge(
    "report",
    END
)


# ==========================================
# COMPILE GRAPH
# ==========================================

graph = graph_builder.compile()