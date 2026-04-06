from fastapi import FastAPI
from fastapi import Depends
from sqlalchemy.orm import Session
from src.utils.db import Base, engine, get_db
from src.tasks.router import task_routes
from src.users.router import user_routes

Base.metadata.create_all(bind=engine)


app=FastAPI(title="my task management application")
app.include_router(task_routes)
app.include_router(user_routes)
from sqlalchemy import text


@app.get("/")
def root():
    return {"message":"API is working successfully"}


@app.get("/db-check")
def db_check(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT 1"))
    return {"db_status": "ok", "result": result.scalar()}
