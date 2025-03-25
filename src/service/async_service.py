from src.repository.async_repository import AsyncStudentRepository

class AsyncStudentService:
    def __init__(self, db):
        self.repository = AsyncStudentRepository(db)
        
    async def get_all_students(self):
        return await self.repository.get_all()
    
    async def create_student(self, student_data):
        return await self.repository.create(student_data)