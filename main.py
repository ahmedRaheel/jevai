from typing import Literal
from pydantic import BaseModel, Field
import jev
from dotenv import load_dotenv
load_dotenv()  

class Triage(BaseModel):
    department: Literal["billing", "technical", "sales"]
    is_urgent: bool
    frustration: int = Field(ge=0, le=2)
@jev.fn
def triage(ticket: str) -> Triage:
    """A customer support ticket:

    {{ ticket }}
    """
    return triage.state()

print(triage("I was internet is slow and it does not worked even after thousand complains."))
# Triage(department='billing', is_urgent=True, frustration=2)

