from fastapi import APIRouter, Depends, HTTPException
from typing import List
import uuid
from classes.schema_dto import Session, SessionNoID
from database.firebase import db
from routers.router_auth import get_current_user
from routers.router_stripe import increment_stripe


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
async def get_sessions(userData: int = Depends(get_current_user)):
    """ List all the Sessions from a Training Center"""
    fireBaseobject = db.child("users").child(userData['uid']).child('session').get(userData['idToken']).val()
    resultArray = [value for value in fireBaseobject.values()]
    return resultArray

@router.post('/', response_model=Session, status_code=201)
async def create_sessions(givenName:SessionNoID, userData: int = Depends(get_current_user)):
    generatedId=uuid.uuid4()
    newSession= Session(id=str(generatedId), name=givenName.name)
    increment_stripe(userData['uid'])
    db.child("users").child(userData['uid']).child("session").child(str(generatedId)).set(newSession.model_dump(), userData['idToken'])
    return newSession

# 1. Exercice
async def modify_student_name(session_id:str, modifiedSession: SessionNoID, userData: int = Depends(get_current_user)):
    fireBaseobject = db.child("users").child(userData['uid']).child('sessions').child(session_id).get(userData['idToken']).val()
    if fireBaseobject is not None:
        updatedSession = Session(id=session_id, **modifiedSession.model_dump())
        return db.child("users").child(userData['uid']).child('sessions').child(session_id).update(updatedSession.model_dump(), userData['idToken'])
    raise HTTPException(status_code= 404, detail="Session not found")

# (10 minutes) 3. Exercice : Faire une suppresion
# 2. Exercice 

@router.patch('/{session_id}', status_code=204)
async def modify_student_name(session_id:str, modifiedSession: SessionNoID, userData: int = Depends(get_current_user)):
    fireBaseobject = db.child("users").child(userData['uid']).child('sessions').child(session_id).get(userData['idToken']).val()
    if fireBaseobject is not None:
        updatedSession = Session(id=session_id, **modifiedSession.model_dump())
        return db.child("users").child(userData['uid']).child('sessions').child(session_id).update(updatedSession.model_dump(), userData['idToken'] )
    raise HTTPException(status_code= 404, detail="Session not found")

# 3.Exercice Delete
@router.delete('/{session_id}', status_code=204)
async def delete_session(session_id:str, userData: int = Depends(get_current_user)):
    try:
        fireBaseobject = db.child("users").child(userData['uid']).child('sessions').child(session_id).get(userData['idToken']).val()
    except:
        raise HTTPException(
            status_code=403, detail="Accès interdit"
        )
    if fireBaseobject is not None:
        return db.child("users").child(userData['uid']).child('sessions').child(session_id).remove(userData['idToken'])
    raise HTTPException(status_code= 404, detail="Session not found")

# Share : https://www.notion.so/fullstack-course/Complex-Queries-30d9113966e944f99510115e8303dc93