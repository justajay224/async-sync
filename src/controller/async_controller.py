from database.connection import AsyncSessionLocal
from src.service.async_service import AsyncStudentService
from sqlalchemy.ext.asyncio import AsyncSession
import time

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

async def get_all_students(db: AsyncSession):
    start = time.time()
    try:
        service = AsyncStudentService(db)
        return await service.get_all_students()
    finally:
        print(f"Async GET Execution time: {time.time() - start:.4f}s")

async def create_new_student(nama: str, npm: str, db: AsyncSession):
    start = time.time()
    try:
        service = AsyncStudentService(db)
        return await service.create_student({"nama": nama, "npm": npm})
    finally:
        print(f"Async POST Execution time: {time.time() - start:.4f}s")