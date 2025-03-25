from fastapi import APIRouter, Depends
from src.controller.sync_controller import (
    get_all_students,
    create_new_student,
    get_db
)
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/sync",
    tags=["Sync Students"]
)

@router.get("/students")
def get_students_endpoint(db: Session = Depends(get_db)):
    return get_all_students(db)

@router.post("/students")
def create_student_endpoint(
    nama: str, 
    npm: str, 
    db: Session = Depends(get_db)
):
    return create_new_student(nama, npm, db)