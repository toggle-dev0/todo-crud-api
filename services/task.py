from repositories import task as task_repo
from sqlmodel import Session
from models.task import Task

def get_all_tasks(session: Session):
    return task_repo.get_all(session)

def get_task(id: int, session: Session):
    task = task_repo.get_unique(id, session)
    return task

def add_task(title: str, session: Session):
    task = Task(title=title, done=False)
    task_repo.create(task, session)
    return task

def remove_task(id: int, session: Session):
    return task_repo.delete(id, session)

def update_task(id: int, data: dict, session: Session):
    return task_repo.update(id, data, session)
