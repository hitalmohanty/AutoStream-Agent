from langgraph.graph import StateGraph
from agent.responses import pricing_answer
from agent.intent import detect_intent
from agent.qualification import qualify_lead
from agent.router import route
from agent.tools import mock_lead_capture
from langchain_core.messages import AIMessage

from agent.state import AutoStreamAgent

# ============= LEAD CAPTURE =============
def capture_lead(state: AutoStreamAgent):
    if state["name"] and state["email"] and state["platform"]:
        mock_lead_capture(
            state["name"],
            state["email"],
            state["platform"]
        )
        state["lead_captured"] = True
        state["messages"].append(
            AIMessage(content="You're all set! Our team will contact you soon.")
        )
    return state

# ============= BUILD GRAPH =============
def build_graph():
    graph = StateGraph(AutoStreamAgent)

    graph.add_node("intent", detect_intent)
    graph.add_node("pricing", pricing_answer)
    graph.add_node("qualify", qualify_lead)
    graph.add_node("capture", capture_lead)
    graph.add_node("end", lambda state: state)
    graph.set_entry_point("intent")

    graph.add_conditional_edges(
        "intent",
        route,
        {
            "pricing": "pricing",
            "qualify": "qualify",
            "end": "end"
        }
    )

    graph.add_edge("qualify", "capture")
    graph.add_edge("capture", "end")

    graph.set_finish_point("end")

    return graph.compile()