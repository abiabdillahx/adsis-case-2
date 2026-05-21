from pydantic import BaseModel

class TodoCreate(BaseModel):
    title: str
    description: str

class TodoResponse(BaseModel):
    id: int
    title: str
    description: str
    attachment: str | None = None

    class Config:
        from_attributes = True