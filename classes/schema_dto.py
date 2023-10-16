from pydantic import BaseModel

# Model Pydantic = Datatype
class Student(BaseModel):
    id: str
    name: str

class Session(BaseModel):
    id: str
    name: str

class Attendance(BaseModel):
    id:str
    student_id:str
    session_id:str
    present: bool


# No IDs for POST requests   
class AttendanceNoID(BaseModel):
    student_id:str
    session_id:str
    present: bool
    
class SessionNoID(BaseModel):
    name: str    

class StudentNoID(BaseModel):
    name: str

class User(BaseModel):
    email: str
    password: str    