# Actual business logic controller me rahega.
from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
from fastapi import HTTPException

# Router se validated body receive hoti hai.
# TaskSchema yahan type hint hai — batata hai body ka data kis type ka hai.optional but for understanding


def create_task(body:TaskSchema,db:Session):
    data = body.model_dump()
    new_task=TaskModel(title=data["title"],
                       description=data["description"],
                       is_completed=data["is_completed"])
    
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task
    
def get_tasks(db:Session):
    tasks=db.query(TaskModel).all()
    # return {
    #     "return":"all tasks","data":tasks
    # }
    return tasks
    
def get_one_task(db:Session,task_id:int):
    one_task=db.query(TaskModel).get(task_id)
    if not one_task:
        return HTTPException(404,detail="Task id is incorrect")
    
    return one_task
    
def update_task(body:TaskSchema,task_id:int,db:Session):
    one_task=db.query(TaskModel).get(task_id)
    if not one_task:
        return HTTPException(404,detail="Task id is incorrect")
    
    # one_task.title = body.title
    # one_task.description = body.description
    # one_task.is_completed = body.is_completed
    
# hum uper wali lines ko use nhi karenge kyuki hme asi chiz chahiye jo ek sath itna code na likhne k bajaye hamara sare
# table content ko update karde 

    body=body.model_dump()
    for field,value in body.items():
        setattr(one_task,field,value)

    
    db.add(one_task)
    db.commit()
    db.refresh(one_task)
    
    return one_task
    
    
def delete_task(task_id:int,db:Session):
    one_task=db.query(TaskModel).get(task_id)
    if not one_task:
        return HTTPException(404,detail="Task id is incorrect")
    
    db.delete(one_task)
    db.commit()
    
    return None