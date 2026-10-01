from fastapi import FastAPI
from src.utils.db import Base,engine
from src.tasks.router import task_routes


Base.metadata.create_all(engine)

app = FastAPI(title="This is my task application")
# Router ko FastAPI application ke saath connect/register karne ke liye
app.include_router(task_routes)