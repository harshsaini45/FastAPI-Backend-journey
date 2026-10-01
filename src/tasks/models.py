# Column SQLAlchemy ko batata hai: Database table mein ek column banana hai
from sqlalchemy import Column,Integer,String,Boolean
from src.utils.db import Base

# Hum database table ko Python class ke through represent kar rahe hain.

# TaskModel: Python side ka model hai.
# Ye SQLAlchemy ko batata hai: Database mein user_tasks table ka structure kaisa hoga.

# user_tasks : database side ka table hai.
class TaskModel(Base):
# SQLAlchemy ko batana hai: "Is model ka database mein table naam user_tasks hoga."
    __tablename__="user_tasks"
    
    id=Column(Integer,primary_key=True)
    title=Column(String)
    description=Column(String)
    is_completed=Column(Boolean,default=False)
    
