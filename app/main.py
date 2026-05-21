from fastapi import FastAPI, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Todo
from database import Base
from minio import Minio
import os

Base.metadata.create_all(bind=engine)

app = FastAPI()

# MinIO Client
minio_client = Minio(
    "minio:9000",
    access_key=os.getenv("MINIO_ROOT_USER"),
    secret_key=os.getenv("MINIO_ROOT_PASSWORD"),
    secure=False
)
BUCKET_NAME = "uploads"

if not minio_client.bucket_exists(BUCKET_NAME):
    minio_client.make_bucket(BUCKET_NAME)

# Database Dependency

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Nusantara Tech Todo API Running"}
@app.post("/todos")
async def create_todo(
    title: str = Form(...),
    description: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    temp_file = f"/tmp/{file.filename}"

    with open(temp_file, "wb") as f:
        f.write(await file.read())

    minio_client.fput_object(
        BUCKET_NAME,
        file.filename,
        temp_file
    )
    todo = Todo(
        title=title,
        description=description,

        attachment=file.filename
    )

    db.add(todo)
    db.commit()
    db.refresh(todo)
    return {
        "message": "Todo berhasil dibuat",
        "todo": {
            "id": todo.id,
            "title": todo.title,
            "description": todo.description,
            "attachment": todo.attachment
        }
    }
@app.get("/todos")
def get_todos(db: Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return todos