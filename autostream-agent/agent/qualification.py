from agent.state import AutoStreamAgent
from langchain_core.messages import AIMessage


# ============= LEAD QUALIFICATION =============
def qualify_lead(state: AutoStreamAgent):
    if not state["name"]:
        state["messages"].append(AIMessage(content="Great! May I know your name?"))
    elif not state["email"]:
        state["messages"].append(AIMessage(content="Thanks. Please share your email."))
    elif not state["platform"]:
        state["messages"].append(
            AIMessage(content="Which creator platform do you use? (YouTube, Instagram, etc.)")
        )
    return state