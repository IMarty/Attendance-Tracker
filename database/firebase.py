import firebase_admin
from firebase_admin import credentials
import pyrebase 
from configs.firebase_config_example import firebaseConfig

if not firebase_admin._apps:
    cred = credentials.Certificate("configs/myapi-adcde-firebase-adminsdk-x2xzc-fbd6249976.json")
    firebase_admin.initialize_app(cred)

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
authSession = firebase.auth()