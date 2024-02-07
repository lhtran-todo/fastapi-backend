from sqlalchemy.orm import Session

from app import models, schemas

def read_todo(db: Session, todo_id: int):
  return db.query(models.Todo).filter(models.Todo.id == todo_id).first()

def read_todos(db: Session, skip: int = 0, limit: int = 100):
  return db.query(models.Todo).offset(skip).limit(limit).all()

def create_todo(db: Session, todo: schemas.TodoBase):
  db_todo = models.Todo(**todo.dict())
  db.add(db_todo)
  db.commit()
  db.refresh(db_todo)
  return db_todo

def update_todo(db: Session, todo_id: int, todo: schemas.TodoBase):
  update_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
  if update_todo == None:
    return None
  else:
    update_todo.title = todo.title
    update_todo.description = todo.description
    update_todo.completed = todo.completed
    db.commit()
    return update_todo

def delete_todo(db: Session, todo_id: int):
  delete_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
  if delete_todo == None:
    return False
  else:
    db.delete(delete_todo)
    db.commit()
    return True