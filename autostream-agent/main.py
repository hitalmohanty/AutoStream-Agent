from langchain_core.messages import AIMessage, HumanMessage
from graph import build_graph

agent = build_graph()

state = {
    "messages": [
        AIMessage(
            content=(
                "👋🏼 Hi! I'm your AutoStream assistant.\n\n" 
                "How can I help you with:\n"
                "- Pricing and Plans\n"
                "- Signing up for Pro plan\n"
                "- Getting started with AutoStream\n\n"
                "Feel free to ask!"
            )
        )
    ],
    "intent": None,
    "name": None,
    "email": None,
    "platform": None,
    "lead_captured": False
}

# ============== DEMO INTERACTION LOOP ==============

print("\n🎬 AutoStream Agent (type 'exit' to quit)\n")
print("Agent:", state["messages"][-1].content)

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    # Store user-provided lead info
    if state["intent"] == "HIGH_INTENT":
        if not state["name"]:
            state["name"] = user_input
        elif not state["email"]:
            state["email"] = user_input
        elif not state["platform"]:
            state["platform"] = user_input

    state["messages"].append(HumanMessage(content=user_input))

    state = agent.invoke(state)

    print("Agent:", state["messages"][-1].content)