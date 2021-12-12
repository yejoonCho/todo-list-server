from datetime import datetime
from fastapi import FastAPI
from fastapi.params import Depends
import schemas
import models
import database

models.Base.metadata.create_all(database.engine)

def get_db():
    db = database.Session()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()


@app.get('/')
def index():
    return 'Hello world'

@app.get('/tasks')
def get_tasks(db: database.Session = Depends(get_db)):
    tasks = db.query(models.Task).all()
    return tasks

@app.get('/task/{id}')
def get_task(id:int, db: database.Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == id).first()
    return task

@app.post('/addtask')
def add_task(request: schemas.Task, db: database.Session = Depends(get_db)):
    task = models.Task(
        content = request.content,
        created_at = datetime.now()
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return request

@app.put('/task/{id}')
def update_task(id:int, request:schemas.Task, db:database.Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == id)
    if not task.first():
        pass
    task.update(request.dict())
    db.commit()
    return {'Task is successfully updated'}

@app.delete('/task/{id}')
def delete(id:int, db:database.Session = Depends(get_db)):
    db.query(models.Task).filter(models.Task.id == id).delete(synchronize_session=False)
    db.commit()
    return {'Task is deleted'}