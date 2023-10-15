import uuid
from fastapi import APIRouter, HTTPException

from classes.schema_dto import Attendance, AttendanceNoID

router = APIRouter(
    tags=["Attendances"]
)
attendances = [
    Attendance(id="att1", student_id="student1", session_id="session1", present=True),
    Attendance(id="att2", student_id="student2", session_id="session2", present=False),
    Attendance(id="att3", student_id="student3", session_id="session3", present=True)
]

@router.get('/attendances')
async def create_attendance():
    return attendances

@router.post('/attendances')
async def create_attendance(givenAttendance:AttendanceNoID):
    newAttendance= Attendance(givenAttendance)
    newAttendance.id = str(uuid.uuid4())
    attendances.append(newAttendance)
    return newAttendance

@router.get('/attendances/{attendance_id}')
async def get_attendance_by_ID(sessions_id:str): # student_id correspond au URI parameter du path: '/students/{student_id}'
    for attendance in attendances:
        if attendance.id == attendance:
            return attendance
    raise HTTPException(status_code= 404, detail="attendance not found")

@router.patch('/attendances/{attendance_id}')
async def modify_attendance(attendance_id:str, modifiedAttendance:AttendanceNoID):
    for attendance in attendances : 
        if attendance.id == attendance_id and attendance.session_id == modifiedAttendance.session_id and attendance.student_id == modifiedAttendance.student_id:
            attendance.present = modifiedAttendance.present        
            return attendance
    raise HTTPException(status_code= 404, detail="attendance not found")

@router.delete('/attendances/{attendance_id}', status_code=204)
async def delete_attendance(attendance_id:str):
    for attendance in attendances:
        if attendance.id == attendance_id:
            attendances.remove(attendance)
            return
    raise HTTPException(status_code= 404, detail="attendance not found")