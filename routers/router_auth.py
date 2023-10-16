from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from classes.schema_dto import User


from firebase_admin import auth
from database.firebase import firebase




router = APIRouter(
    tags=["Auth"], 
    prefix='/auth',
)


@router.post('/signup', status_code=201)
async def create_an_account(user_data:User):
    """ Register a new paying user"""
    try:
        user = auth.create_user(
            email = user_data.email,
            password = user_data.password
        )
        return {
            "message" : f"User account created successfuly for user {user.uid}"
        }
    except auth.EmailAlreadyExistsError:
        raise HTTPException(
            status_code=409,
            detail= f"Account already created for the email {user_data.email}"
        )

# Define the Firebase authentication dependency
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(provided_token: str = Depends(oauth2_scheme)):
    print("provided_token "+ provided_token)
    # You can use token to verify the user's authentication using Firebase or other methods.
    # Here, you can use Pyrebase to verify the token.
    user = auth.verify_id_token(provided_token)
    return user

# Login endpoint
@router.post('/login')
async def create_swagger_token(user_credentials: OAuth2PasswordRequestForm = Depends()):
    try:
        print(user_credentials)
        user = firebase.auth().sign_in_with_email_and_password(
            email = user_credentials.username,
            password = user_credentials.password
        )
        token = user['idToken']
        print(token)
        return {
            "access_token": token,
            "token_type": "bearer"
        }
    except:
        raise HTTPException(
            status_code=401,detail="Invalid Credentials"
        )

# Protecte route to get personal data
@router.get("/me")
def secure_endpoint(user_id: int = Depends(get_current_user)):
    return user_id

