from pydantic import BaseModel

class BaseModelORM(BaseModel):
  class Config:
    orm_mode = True

class TodoBase(BaseModelORM):
  title: str
  description: str = None
  completed: bool = False

class TodoReturn(TodoBase):
  id: int