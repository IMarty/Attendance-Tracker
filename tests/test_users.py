from fastapi.testclient import TestClient
from main import app
from firebase_admin import auth
import pytest

client = TestClient(app)

def test_create_user_success():
    res = client.post("/auth/signup", json={
        "email": "test.user1@gmail.com" , "password": "password"
    })
    assert res.status_code == 201 

# define test_create_user_conflict()
# res.status_code == 409    

def test_create_user_conflict(create_user):
    res = client.post("/auth/signup", json={
        "email": "test.user2@gmail.com", 'password': "password"
    })
    assert res.status_code == 409

