from sqlalchemy.orm import Session
from src.model.student_model import Student

class SyncStudentRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def get_all(self):
        return self.db.query(Student).all()
    
    def create(self, student_data):
        new_student = Student(**student_data)
        self.db.add(new_student)
        self.db.commit()
        self.db.refresh(new_student)
        return new_student
    