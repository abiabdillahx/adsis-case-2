from fastapi import FastAPI, Depends, UploadFile, File, Form
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Student
from database import Base
from minio import Minio
import os

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Nusantara Tech - Academic System")

app.mount("/static", StaticFiles(directory="static"), name="static")

# MinIO Client
MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT", "minio:9000")
BUCKET_NAME = os.getenv("MINIO_BUCKET", "uploads")

minio_client = Minio(
    MINIO_ENDPOINT,
    access_key=os.getenv("MINIO_ROOT_USER"),
    secret_key=os.getenv("MINIO_ROOT_PASSWORD"),
    secure=False
)

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
    return FileResponse("static/index.html")

@app.post("/students")
async def register_student(
    name: str = Form(...),
    nim: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # Simpan file sementara untuk diupload ke MinIO
    temp_file = f"/tmp/{file.filename}"
    os.makedirs("/tmp", exist_ok=True) # Pastikan folder /tmp ada

    with open(temp_file, "wb") as f:
        f.write(await file.read())

    # Upload ke MinIO
    minio_client.fput_object(
        BUCKET_NAME,
        file.filename,
        temp_file
    )
    
    # Hapus file sementara setelah upload
    if os.path.exists(temp_file):
        os.remove(temp_file)

    # Simpan ke Database
    student = Student(
        name=name,
        nim=nim,
        profile_image=file.filename
    )

    db.add(student)
    db.commit()
    db.refresh(student)
    
    return {
        "message": "Data mahasiswa berhasil disimpan",
        "student": {
            "id": student.id,
            "name": student.name,
            "nim": student.nim,
            "profile_image": student.profile_image
        }
    }

@app.get("/students")
def list_students(db: Session = Depends(get_db)):
    students = db.query(Student).all()
    return students

@app.get("/students/image/{filename}")
async def get_student_image(filename: str):
    try:
        response = minio_client.get_object(BUCKET_NAME, filename)
        return StreamingResponse(response, media_type="image/jpeg")
    except Exception as e:
        return {"error": str(e)}
