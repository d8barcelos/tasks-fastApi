from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from crud.crud import delete_task
from database import SessionLocal
from crud import create_task, get_tasks
from schemas import Task, TaskCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/{user_id}", response_model=Task)
def create_task_route(user_id: int, task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, task, user_id)

@router.get("/{user_id}", response_model=list[Task])
def read_tasks_route(user_id: int, db: Session = Depends(get_db)):
    return get_tasks(db, user_id)

@router.delete("/{task_id}")
def remove_tasks(task_id: int, db: Session = Depends(get_db)):
    return delete_task(db, task_id)
