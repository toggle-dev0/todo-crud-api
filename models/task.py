from sqlmodel import SQLModel, Field

class Task(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    done: bool = Field(default=False)

"""tasks = [
    {"id": 1, "title": "Learn FastAPI", "done": False},
    {"id": 2, "title": "Mow the lawn", "done": False},
    {"id": 3, "title": "Attend Piano lesson", "done": False},
]"""