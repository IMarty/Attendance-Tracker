from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from classes.schema_dto import User
from firebase_admin import auth
from database.firebase import authSession

router = APIRouter(
    tags=["Auth"],
    prefix='/auth',
)

# Création d'un nouvel utilisateur
@router.post('/signup', status_code=201)
async def create_an_account(user_data: User):
    try:
        user = auth.create_user(
            email=user_data.email,
            password=user_data.password
        )
        return {
            "message": f"Nouvel utilisateur créé avec id: {user.uid}"
        }
    except auth.EmailAlreadyExistsError:
        raise HTTPException(
            status_code=409,
            detail=f"Un compte existe déjà pour: {user_data.email}"
        )

# 1. Définition du chemin de génération du token (il se sert directement du formulaire de la documentation OAuth2PasswordRequestForm)
@router.post('/login', status_code=201)
async def create_swagger_token(user_credentials: OAuth2PasswordRequestForm = Depends()):
    try:
        print(user_credentials)
        user = authSession.sign_in_with_email_and_password(
            email=user_credentials.username,
            password=user_credentials.password
        )
        token = user['idToken']
        print(token)
        return {
            "access_token": token,
            "token_type": "bearer"
        }
    except:
        raise HTTPException(
            status_code=401, detail="Invalid Credentials"
        )

# 2. Ajout du lien entre le bouton d’authentification et le chemin de génération du token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# 3. Création de la méthode qui vérifie que le token correspond à un vrai utilisateur@router.post('/login')
def get_current_user(provided_token: str = Depends(oauth2_scheme)):
    decoded_token = auth.verify_id_token(provided_token)
    decoded_token['idToken']=provided_token
    return decoded_token

# 4. Utilisation de la méthode pour protéger un route (par exemple le /me)
@router.get("/me")
def secure_endpoint(userData: int = Depends(get_current_user)):
    return userData
