from src.repository.sync_repository import SyncStudentRepository

class SyncStudentService:
    def __init__(self, db):
        self.repository = SyncStudentRepository(db)
        
    def get_all_students(self):
        return self.repository.get_all()
    
    def create_student(self, student_data):
        return self.repository.create(student_data)