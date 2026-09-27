from sqlmodel import Session, select
from models.task import Task

def get_all(session: Session):
    return session.exec(select(Task)).all()

def get_unique(id: int, session: Session):
    return session.get(Task, id)

def create(task: dict, session: Session):
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

def delete(id: int, session: Session):
    task = session.get(Task, id)
    if task is None:
        return False
    session.delete(task)
    session.commit()
    return True

def update(id: int, data: dict, session: Session):
    task = session.get(Task, id)
    if task is None:
        return None
    task.sqlmodel_update(data)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task