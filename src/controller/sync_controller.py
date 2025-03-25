from sqlalchemy.orm import Session
from database.connection import SyncSessionLocal
from src.service.sync_service import SyncStudentService
import time

def get_db():
    db = SyncSessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_all_students(db: Session):
    start = time.time()
    try:
        service = SyncStudentService(db)
        return service.get_all_students()
    finally:
        print(f"Sync GET Execution time: {time.time() - start:.4f}s")

def create_new_student(nama: str, npm: str, db: Session):
    start = time.time()
    try:
        service = SyncStudentService(db)
        return service.create_student({"nama": nama, "npm": npm})
    finally:
        print(f"Sync POST Execution time: {time.time() - start:.4f}s")