from fastapi import FastAPI, HTTPException, Depends, status, Response
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.database import SessionLocal, engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()


@app.post("/todos/", response_model=schemas.TodoReturn, status_code=status.HTTP_201_CREATED)
def create_todo(todo: schemas.TodoBase, db: Session = Depends(get_db)):
  return crud.create_todo(db=db, todo=todo)

@app.get("/todos/{todo_id}", response_model=schemas.TodoReturn, status_code=status.HTTP_200_OK)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
  db_todo = crud.read_todo(db, todo_id=todo_id)
  if db_todo is None:
    raise HTTPException(status_code=404, detail="Todo not found")
  return db_todo

@app.get("/todos/", response_model=list[schemas.TodoReturn], status_code=status.HTTP_200_OK)
def read_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
  return crud.read_todos(db, skip=skip, limit=limit)

@app.put("/todos/{todo_id}", response_model=schemas.TodoReturn, status_code=status.HTTP_200_OK)
def update_todo(todo_id: int, todo: schemas.TodoBase, db: Session = Depends(get_db)):
  update_todo = crud.update_todo(db, todo_id=todo_id, todo=todo)
  if update_todo == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
  else:
    return update_todo

@app.delete("/todos/{todo_id}", response_model=None, status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
  delete_todo = crud.delete_todo(db, todo_id=todo_id)
  if delete_todo == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
  else:
    return
  


