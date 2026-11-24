from pydantic import BaseModel, Field
# from typing import Optional
# from pydantic import ConfigDict

class StudentCreate(BaseModel):
    # id: int
    name: str
    age: int = Field(le=30, ge=18)
    email: str
    roll: int
    session: str
    english_score:int
    math_score:int
    history_score:int
    def to_student_dict(self):
        return self.model_dump(exclude={"english_score","math_score","history_scores"})


class StudentResponse(studentCreate):
    id:int
    class config:
        from_attribute=True

# class StudentUpdate(BaseModel):
#     name: Optional[str]= Field(default="")
#     email: Optional[str]= Field(default="")
#     age: Optional[int]=Field(default=18) 