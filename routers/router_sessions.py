from fastapi import APIRouter, HTTPException
from typing import List
import uuid
from classes.schema_dto import Session, SessionNoID


router= APIRouter(
    prefix='/sessions',
    tags=["Sessions"]
)

sessions = [
    Session(id="session1", name="Fullstack Webdevelopper Janvier"),
    Session(id="session2", name="Fullstack Webdevelopper Mai"),
    Session(id="session3", name="Fullstack Webdevelopper Septembre")
]

@router.get('/', response_model=List[Session])
async def get_sessions():
    """ List all the Sessions from a Training Center"""
    return sessions

@router.post('/', response_model=Session, status_code=201)
async def create_sessions(givenName:SessionNoID):
    generatedId=uuid.uuid4()
    newSession= Session(id=str(generatedId), name=givenName)
    sessions.append(newSession)
    return newSession


@router.get('/{sessions_id}', response_model=Session)
async def get_session_by_ID(sessions_id:str): 
    for session in sessions:
        if session.id == sessions_id:
            return session
    raise HTTPException(status_code= 404, detail="Session not found")

# 3. Exercice (10min) PATCH Student (name)
@router.patch('/{session_id}', status_code=204)
async def modify_student_name(session_id:str, modifiedSession: SessionNoID):
    for session in sessions:
        if session.id == session_id:
            session.name=modifiedSession.name
            return
    raise HTTPException(status_code= 404, detail="Session not found")

@router.delete('/{session_id}', status_code=204)
async def delete_session(session_id:str):
    for session in sessions:
        if session.id == session_id:
            sessions.remove(session)
            return
    raise HTTPException(status_code= 404, detail="Session not found")