from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
from fastapi import HTTPException
from src.utils.db import get_db

def create_task(body:TaskSchema,db:Session):
    data=body.model_dump()
    new_task = TaskModel(title=data["title"],
                       description=data["description"],
                       is_completed=data["is_completed"]
                        )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_tasks(db:Session):
    tasks=db.query(TaskModel).all()
    return tasks


def get_one_task(db:Session,task_id:int):
    one_task = db.get(TaskModel, task_id)
    if not one_task:
       raise HTTPException(status_code=404,detail="task not found")
    return one_task
    

def update_task(body:TaskSchema,task_id:int,db:Session):
    one_task = db.get(TaskModel, task_id)
    if not one_task:
        raise HTTPException(status_code=404,detail="task not found")
    body=body.model_dump()

    for key, value in body.items():
        setattr(one_task, key, value)

    db.add(one_task)
    db.commit()
    db.refresh(one_task)
    return one_task

def delete_task(task_id:int,db:Session):
    one_task=db.get(TaskModel,task_id)
    if not one_task:
        raise HTTPException(status_code=404,detail="task not found")
    db.delete(one_task)
    db.commit()
    return None
