from fastapi import APIRouter, Depends
from src.controller.async_controller import (
    get_all_students,
    create_new_student,
    get_db
)
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix="/async",
    tags=["Async Students"]
)

@router.get("/students")
async def get_students_endpoint(db: AsyncSession = Depends(get_db)):
    return await get_all_students(db)

@router.post("/students")
async def create_student_endpoint(
    nama: str, 
    npm: str, 
    db: AsyncSession = Depends(get_db)
):
    return await create_new_student(nama, npm, db)