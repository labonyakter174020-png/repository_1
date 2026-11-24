from sqlalchemy.orm import Session
from model.student import Student
from db import get_connection,session_local

class  student_repository:
    def __init__(self):
        self.connection =session_local()

        


    def get_all_student(self):
        return self.connection.query(Student).all()
    def creat_student(self,student: Student):
        self.connection.add(student)
        self.connection.commit()

