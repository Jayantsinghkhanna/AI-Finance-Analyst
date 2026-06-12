from langgraph.graph import (
    StateGraph,
    END
)

from state.finance_state import (
    FinanceState
)

from agents.router_agent import (
    router_agent
)

from agents.finance_supervisor_agent import (
    finance_supervisor_agent
)

from agents.report_agent import (
    report_agent
)

from skills.pdf_report_skill import (
    pdf_report_skill
)


builder = StateGraph(
    FinanceState
)

# ==========================
# NODES
# ==========================

builder.add_node(
    "router",
    router_agent
)

builder.add_node(
    "supervisor",
    finance_supervisor_agent
)

builder.add_node(
    "report",
    report_agent
)

builder.add_node(
    "pdf",
    pdf_report_skill
)

# ==========================
# ENTRY POINT
# ==========================

builder.set_entry_point(
    "router"
)

# ==========================
# FLOW
# ==========================

builder.add_edge(
    "router",
    "supervisor"
)

builder.add_edge(
    "supervisor",
    "report"
)

builder.add_edge(
    "report",
    "pdf"
)

builder.add_edge(
    "pdf",
    END
)

# ==========================
# COMPILE
# ==========================

graph = builder.compile()