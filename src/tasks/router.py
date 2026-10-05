# Router request ko correct function tak pahunchata hai, aur decorator
# function ko specific URL + HTTP method ke saath register karta hai.
from fastapi import APIRouter,Depends,status
# controller import : Controller file ke functions ko router me use karne ke liye import kiya.
from src.tasks import controller
from src.tasks.dtos import TaskSchema,TaskResponseSchema
from src.utils.db import get_db
from typing import List
from src.user.models import UserModel
from src.utils.helpers import is_authenticated


task_routes=APIRouter(prefix="/tasks")
# ######################## FastAPI: Router flow #####################33
# "/tasks" → prefix match karta hai
# POST "/" → matching route dhundhta hai
# ↓
# create_task() function call hota hai
#################################################################################
# Router ka kaam mainly request ko sahi controller function tak pahunchana hai

# Router function
# Ye function incoming request ko handle karega.
# Naam create_task humne meaningful rakha hai.
# Naam fixed nahi hai; koi bhi valid naam ho sakta hai

@task_routes.post("/create",response_model=TaskResponseSchema,status_code=status.HTTP_201_CREATED)
# Request body ko TaskSchema ke according validate karta hai.
# Validation ke baad validated body controller ko pass hoti hai.
def create_task(body:TaskSchema, db = Depends(get_db),user:UserModel = Depends(is_authenticated)):
    print(user.id)
    
# Controller ko call
# Router khud actual task-creation logic nahi karta.
# Ye request ko controller ke create_task() function ko forward karta hai.
# Controller jo result dega, router wahi response me return karega.
    return controller.create_task(body,db,user)

@task_routes.get("/all_tasks",status_code=status.HTTP_200_OK)
def get_all_tasks(db=Depends(get_db),user:UserModel = Depends(is_authenticated)):
    return controller.get_tasks(db,user)

@task_routes.get("/one_task/{task_id}",response_model=TaskResponseSchema,status_code=status.HTTP_200_OK)
def get_one_task(task_id:int,db=Depends(get_db),user:UserModel = Depends(is_authenticated)):
    return controller.get_one_task(db,task_id)


@task_routes.put("/update_task/{task_id}",response_model=TaskResponseSchema,status_code=status.HTTP_201_CREATED)
def update_task(body:TaskSchema,task_id:int,db=Depends(get_db),user:UserModel = Depends(is_authenticated)):
    return controller.update_task(body,task_id,db,user)

@task_routes.delete("/delete_task/{task_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id:int,db=Depends(get_db),user:UserModel = Depends(is_authenticated)):
    return controller.delete_task(task_id,db,user)


