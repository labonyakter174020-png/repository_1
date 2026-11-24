from db import session_local
from model.subject import Subjects            

class CourseRepository:
    def __init__(self):
        self.connection =session_local()
    def sdd_subject_score(selt, subjects:Subjects):
        selt.connection.add(subjects)
        selt.connection.commit()