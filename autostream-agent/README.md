# Introduction
In this assignment, I built a GenAI-powered conversational agent for AutoStream that follows an agentic workflow to identify user intent, retrieve verified product information via RAG and conditionally capture leads using controlled tool execution. The agent is implemented using LangGraph to ensure deterministic state transitions and reliable business logic execution.

# Flow chart of Mechanism of my agent:
┌────────────┐
│   User     │
└─────┬──────┘
      │ Message
      ▼
┌──────────────────┐
│ Intent Detection │
│ (Greeting /      │
│  Pricing / Lead) │
└─────┬────────────┘
      │ Intent
      ▼
┌──────────────────┐
│  Agent State     │
│  (Memory)        │
│  - intent        │
│  - lead_status   │
│  - collected     │
│    fields        │
└─────┬────────────┘
      │
      ▼
┌─────────────────────────┐
│ Decision Logic (Agent)  │
│                         │
│ If pricing question →   │
│    use RAG              │
│ If high intent →        │
│    ask for missing info │
│ If all info collected → │
│    call tool            │
└─────┬───────────────────┘
      │
      ▼
┌──────────────┬───────────────┐
│ RAG Answer   │ Tool Execution │
│ (Knowledge)  │ (Lead Capture) │
└──────────────┴───────────────┘
      │
      ▼
┌────────────┐
│  Response  │
│  to User   │
└────────────┘

## How to Run the Project Locally

# Prerequisites

- Python 3.9+
- A virtual environment (recommended)
- Google Gemini API Key

# Installation Steps

- 1. Clone the repository:
     git clone <repository-url>
     cd autostream_agent

- 2. Create and activate a virtual environment:
     python -m venv venv
     venv\Scripts\activate    # Windows
     source venv/bin/activate # macOS/Linux

- 3. Install dependencies:
     pip install -r requirements.txt

- 4. Set the API key as an environment variable:
     set GOOGLE_API_KEY=your_api_key_here     # Windows
     export GOOGLE_API_KEY=your_api_key_here  # macOS/Linux

- 5. Run the agent:
     python main.py

The agent will start in interactive CLI mode.

## Architecture Explanation

# Why LangGraph was chosen?

LangGraph was selected because this project requires a deterministic, multi-step agentic workflow, not a free-form chatbot. The agent must reliably move through specific stages such as intent detection, pricing response, lead qualification, and lead capture. LangGraph provides explicit graph-based control over execution flow, which ensures predictability, debuggability, and correctness—qualities essential for business workflows.

Unlike AutoGen, which focuses more on autonomous multi-agent collaboration, LangGraph is better suited for single-agent, state-driven workflows with strict control over transitions and tool execution.

# How state is managed?

The agent uses an explicit shared state object (AutoStreamAgent) containing:

conversation messages

detected intent

lead details (name, email, platform)

lead capture status

Each LangGraph node receives the full state, mutates it if necessary, and returns it. No node ever returns a partial state, ensuring state consistency.
The state is created and owned by the runtime (main.py), while the graph remains stateless and reusable. This separation ensures clean architecture, easier debugging, and scalability to multiple deployment channels.

## WhatsApp Deployment Using Webhooks

To integrate AutoStream with WhatsApp, the agent would be deployed behind a webhook-based backend service using the WhatsApp Business API.

When a user sends a message on WhatsApp, WhatsApp triggers a webhook POST request to the backend. The backend extracts the sender’s phone number and message text, then retrieves or initializes the agent state associated with that phone number (acting as a session identifier). The message is appended to the state and passed to the LangGraph agent using agent.invoke(state).

After execution, the agent’s response is extracted from the updated state and sent back to the user via the WhatsApp Business API. The updated state is then persisted in a database or cache (e.g., Redis) to maintain conversation continuity across messages.

This design keeps WhatsApp handling separate from agent logic, allows horizontal scaling, and enables reliable multi-turn conversations with structured lead capture.