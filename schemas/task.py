from sqlmodel import SQLModel, Field
from typing import Optional

# Pydantic models
class TaskCreate(SQLModel):
    title: str = Field(min_length=1)

class TaskUpdate(SQLModel):
    title: Optional[str] = Field(default=None, min_length=1)
    done: Optional[bool] = Field(default=None)