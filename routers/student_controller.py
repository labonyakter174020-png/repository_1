from fastapi import APIRouter, status
from service.student_service import StudentService
from utils.schema import Student, StudentCreate

router = APIRouter(prefix="/students", tags=["Student"])



@router.get("/all", status_code=status.HTTP_200_OK)
def get_all_students():
     service = StudentService()
     return service.get_students()

@router.post("/add", status_code= status.HTTP_201_CREATED)
def add_student(student_payload: StudentCreate):
     service = StudentService()
     service.add_student(student_payload)

# @router.delete("/{id}", status_code= status.HTTP_202_ACCEPTED)
# def delete(id:int):
#     service = StudentService()
#     service.delete_student(id)

# @router.patch("/{id}", status_code= status.HTTP_202_ACCEPTED)
# def update(id: int, payload : StudentUpdate):
#     service = StudentService()
#     service.update(id, payload)