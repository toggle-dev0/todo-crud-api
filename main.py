from fastapi import FastAPI, HTTPException, status
app = FastAPI()

tasks = [
    {"id": 1, "title": "Learn FastAPI", "done": False},
    {"id": 2, "title": "Mow the lawn", "done": False},
    {"id": 3, "title": "Attend Piano lesson", "done": False},
]

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