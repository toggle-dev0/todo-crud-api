from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlmodel import Session
from database import get_session
import services.task as task_service
from schemas.task import TaskCreate, TaskUpdate

router = APIRouter(prefix="/v1/tasks", tags=["Tasks"])

@router.get("/")
def get_tasks(session: Session = Depends(get_session)): 
    return task_service.get_all_tasks(session)

@router.get("/{id}")
def get_task(id: int, session: Session = Depends(get_session)):
    task = task_service.get_task(id, session)
    if task is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, session: Session = Depends(get_session)):
    new_task = task_service.add_task(task.title, session)
    return new_task

@router.put("/{id}")
def update_task(id: int, payload: TaskUpdate, session: Session = Depends(get_session)):
    # check if request body is empty
    if not payload:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Empty body")
    
    # sets data to the valid request body
    data = payload.model_dump(exclude_unset=True)
    task = task_service.update_task(id, data, session)
    if task is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id: int, session: Session = Depends(get_session)):
    task = task_service.remove_task(id, session)
    if not task:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Task not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)