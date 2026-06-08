from pydantic import BaseModel

class StudentBase(BaseModel):
    name: str
    nim: str

class StudentCreate(StudentBase):
    pass

class StudentResponse(StudentBase):
    id: int
    profile_image: str | None = None

    class Config:
        from_attributes = True
