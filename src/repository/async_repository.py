from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.model.student_model import Student

class AsyncStudentRepository:
    def __init__(self, db: AsyncSession):
        self.db = db
        
    async def get_all(self):
        result = await self.db.execute(select(Student))
        return result.scalars().all()
    
    async def create(self, student_data):
        new_student = Student(**student_data)
        self.db.add(new_student)
        await self.db.commit()
        await self.db.refresh(new_student)
        return new_student
    