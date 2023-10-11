# Import du framework
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# Initialisation de l'API
app = FastAPI(
    title="Attendance Tracker"
)

# Model Pydantic = Datatype
class Student(BaseModel):
    id: int
    name: str

students = [
    Student(id=1, name="Adama"),
    Student(id=2, name="Adrien"),
    Student(id=3, name="Akbar")
]

# Verbs + Endpoints
@app.get('/students', response_model=List[Student])
async def get_student():
    return students
# 1. Exercice (10min) Create new Student: POST
# 2. Exercice (10min) Student GET by ID
# 3. Exercice (10min) PATCH Student (name)
# 4. Exercice (10min) DELETE Student

# Spécification...
# "Students" auront des "Attendances" pour des "Sessions"
# Utilisateurs, lien vers une ressource
# API vendu à des centre de formations ... "Center" -> Sessions + Students -> Attendances
