from repository.student_repository import  StudentRepository
from  repository.course_repository import CourseRepository

class Student_service:
    def __init__(self):
        self.repository =StudentRepository()
        def get_students(self):
            students=self.repository.get_all_student()
            student_list=[]
            for student in Students :
                student_list.append(StudentRepository.model_validate(student))

                return student_list
            def add_student(self,student_payload:StudentCreate):
                student =Students(**student_payload.to_student_dict())
                self.repository.create_student(student)
                subject =Subjects(student_roll=student_payload.roll,
                                  english_score=student_payload.english-score,
                                  math_score=student_payload.math_score,
                                  history_score=student_payload.history_score
                                  )
                self.subject_repository.add_subject_score(subject)
        
            
# from utils.schema import Student, StudentUpdate
# from repo  

# student_list = []
# student = Student(id=1,
#                   name="Kape",
#                   age=23,
#                   email="a@gmail.com",
#                   roll=23423,
#                   session="2022-2023"
#                   )
# student_list.append(student)

# class StudentService:
#     def __init__(self):
#         pass

#     def get_students(self):
#         return student_list

#     def add_student(self, student: Student):
#         student_list.append(student)

#     def delete_student(self, id : int):
#         for student in student_list:
#             if id == student.id:
#                 student_list.remove(student)

#     def update(self, id: int, update_payload: StudentUpdate):
#         for student in student_list:
#             if id == student.id:
#                 if update_payload.name:
#                     student.name = update_payload.name
#                 if update_payload.age:
#                     student.age = update_payload.age
#                 if update_payload.email:
#                     student.email = update_payload.email

#                 student_list.remove(student)
#                 student_list.append(student)
