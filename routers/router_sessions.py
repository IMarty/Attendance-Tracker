from fastapi import APIRouter, Depends, HTTPException
from typing import List
import uuid
from classes.schema_dto import Session, SessionNoID
from database.firebase import db
from routers.router_auth import get_current_user

router= APIRouter(
    prefix='/sessions',
    tags=["Sessions"]
)

sessions = [
    Session(id="session1", name="Fullstack Webdevelopper Janvier"),
    Session(id="session2", name="Fullstack Webdevelopper Mai"),
    Session(id="session3", name="Fullstack Webdevelopper Septembre")
]

@router.post('/', response_model=Session, status_code=201)
async def create_sessions(givenName:SessionNoID, userData: int = Depends(get_current_user)):
    generatedId=uuid.uuid4()
    newSession= Session(id=str(generatedId), name=givenName.name)
    # Alternative Writing for more complet objects: newSession= Session(id=str(generatedId), **givenName.model_dump())
    db.child("users").child(userData['uid']).child("sessions").child(generatedId).set(newSession.model_dump(),userData['idToken'])
    return newSession

@router.get('/' , response_model=List[Session])
async def get_sessions(userData: int = Depends(get_current_user)):
    fireBaseobject = db.child("users").child(userData['uid']).child('sessions').get(userData['idToken']).val()
    resultArray = [value for value in fireBaseobject.values()]
    return resultArray

# (10 minutes) 1. Exercice : en utilisant .child(sessions).child(sessions_id).get().val() renvoyez l'oject ou 404 is non trouvé
@router.get('/{session_id}', response_model=Session)
async def get_session_by_ID(session_id:str, userData: int = Depends(get_current_user)): 
    fireBaseobject = db.child("users").child(userData['uid']).child('sessions').child(session_id).get(userData['idToken']).val()
    if fireBaseobject is not None:
        return fireBaseobject
    raise HTTPException(status_code= 404, detail="Session not found")

# (10 minutes) 2. Exercice : Faire une modification du nom de la session
# Exemple db.child("users").child("Morty").update({"name": "Mortiest Morty"})
@router.patch('/{session_id}', status_code=204)
async def modify_student_name(session_id:str, modifiedSession: SessionNoID, userData: int = Depends(get_current_user)):
    fireBaseobject = db.child("users").child(userData['uid']).child('sessions').child(session_id).get(userData['idToken']).val()
    if fireBaseobject is not None:
        updatedSession = Session(id=session_id, **modifiedSession.model_dump())
        return db.child("users").child(userData['uid']).child('sessions').child(session_id).update(updatedSession.model_dump(), userData['idToken'])
    raise HTTPException(status_code= 404, detail="Session not found")

# (10 minutes) 3. Exercice : Faire une suppresion
# Exemple : db.child("user").child(some_key).remove()
# Undocumented 404 ? 
@router.delete('/{session_id}', status_code=204, responses={404: {"description": "Session not found"}})
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
