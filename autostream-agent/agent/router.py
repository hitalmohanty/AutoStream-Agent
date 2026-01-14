from agent.state import AutoStreamAgent

def route(state: AutoStreamAgent):
    if state["intent"] == "PRICING":
        return "pricing"

    if state["intent"] == "HIGH_INTENT":
        return "qualify"

    return "end"