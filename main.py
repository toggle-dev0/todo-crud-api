from fastapi import FastAPI, HTTPException, status, Response
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

# Returns status code 400 - Bad Request for empty body and invalid path parameters
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": exc.errors(), "body": exc.body},
    )

# In-memory tasks list 
tasks = [
    {"id": 1, "title": "Learn FastAPI", "done": False},
    {"id": 2, "title": "Mow the lawn", "done": False},
    {"id": 3, "title": "Attend Piano lesson", "done": False},
]

# Pydantic models
class TaskCreate(BaseModel):
    title: str = Field(min_length=1)

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1)
    done: Optional[bool] = Field(default=None)

@app.get("/")
def main():
    return { "name": "Task API", "version": "1.0", "endpoints": ["/tasks"] }

@app.get("/health")
def server_health():
    return { "status": "ok" }

@app.get("/tasks")
def get_tasks(): 
    return tasks

@app.get("/tasks/{id}")
def get_task(id: int):
    for task in tasks:
        if task["id"] == id:
            return task
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Task not found")

@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "done": False
    }
    tasks.append(task)
    return task

@app.put("/tasks/{id}")
def update_task(id: int, payload: TaskUpdate):
    # check if request body is empty
    if not payload:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Empty body")
    
    # sets updated_task to the valid request body
    updated_task = payload.model_dump(exclude_unset=True)
    for task in tasks:
        if task["id"] == id:
            task.update(updated_task)
            return task
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Task not found")

@app.delete("/tasks/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id: int):
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Task not found")