from agent.state import AutoStreamAgent
from langchain_core.messages import AIMessage

# ============= PRICING ANSWER =============
def pricing_answer(state: AutoStreamAgent):
    answer = """
AutoStream Plans:

Basic Plan:
- $29/month
- 10 videos per month
- 720p resolution

Pro Plan:
- $79/month
- Unlimited videos
- 4K resolution
- AI captions

Policies:
- No refunds after 7 days
- 24/7 support only on Pro plan
"""
    state["messages"].append(AIMessage(content=answer))
    return state