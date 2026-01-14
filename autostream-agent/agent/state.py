from typing import TypedDict, Optional

class AutoStreamAgent(TypedDict):
    messages: list[str]
    intent: Optional[str]
    name: Optional[str]
    email: Optional[str]
    platform: Optional[str]
    lead_captured : bool