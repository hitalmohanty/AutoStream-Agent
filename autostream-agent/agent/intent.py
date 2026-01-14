from agent.state import AutoStreamAgent

# ============= INTENT DETECTION =============
def detect_intent(state: AutoStreamAgent):
    # 🔒 If we are already in lead qualification, DO NOT change intent

    if "messages" not in state:
        state["messages"] = []

    if state["intent"] == "HIGH_INTENT" and not state["lead_captured"]:
        return state

    if not state["messages"]:
        state["intent"] = "GREETING"
        return state

    text = state["messages"][-1].content.lower()

    pricing_words = ["price", "pricing", "cost", "plans"]
    high_intent_words = ["buy", "purchase", "signup", "sign up", "try", "trial", "pro plan", "basic plan", "i want", "i need", "i will take"]

    if any(word in text for word in pricing_words):
        state["intent"] = "PRICING"
    elif any(word in text for word in high_intent_words):
        state["intent"] = "HIGH_INTENT"
    else:
        # 👇 IMPORTANT: fallback does NOT reset intent
        state["intent"] = state["intent"] or "GREETING"

    return state