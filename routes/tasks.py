from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import create_task, get_tasks, delete_task
from database import get_db
from schemas import Task, TaskCreate
from auth.auth_bearer import JWTBearer

router = APIRouter()

@router.post("/{user_id}", response_model=Task, dependencies=[Depends(JWTBearer())])
def create_task_route(user_id: int, task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, task, user_id)

@router.get("/{user_id}", response_model=list[Task], dependencies=[Depends(JWTBearer())])
def read_tasks_route(user_id: int, db: Session = Depends(get_db)):
    return get_tasks(db, user_id)

@router.delete("/{task_id}", dependencies=[Depends(JWTBearer())])
def remove_tasks(task_id: int, db: Session = Depends(get_db)):
    return delete_task(db, task_id)
