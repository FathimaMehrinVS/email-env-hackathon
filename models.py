from pydantic import BaseModel, field_validator
from typing import Optional

class EmailObservation(BaseModel):
    email: Optional[str]
    subject: Optional[str]
    sender: Optional[str]

class EmailAction(BaseModel):
    action: str

    @field_validator("action")
    @classmethod
    def validate_action(cls, v: str) -> str:
        allowed = ["mark_important", "delete", "ignore"]
        if v not in allowed:
            raise ValueError(f"Action must be one of {allowed}")
        return v
