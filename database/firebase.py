import firebase_admin
from firebase_admin import credentials
import pyrebase
from configs.firebaseConfig import firebaseConfig

if not firebase_admin._apps:
    cred = credentials.Certificate("configs/serviceAccountKey.json")
    firebase_admin.initialize_app(cred)


firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database() # Utiliser le module realtime Database
