from firebase_admin import auth
from fastapi.testclient import TestClient
from main import app
import pytest
# conftest.py or your test file
import os

os.environ['TESTING'] = 'True'

client = TestClient(app)
# copy other fixture into here
# @pytest.fixture(scope="session", autouse=True)
# def cleanup(request):
#     """Cleanup a testing directory once we are finished."""
#     def remove_test_users():
#         users = auth.list_users().iterate_all()
#         for user in users:
#             if user.email.startswith("test.user"):
#                 auth.delete_user(user.uid)
#     request.addfinalizer(remove_test_users)
@pytest.fixture
def created_user():
    user_credential = client.post("/auth/signup", json={
        "email": "test.user@gmail.com",
        "password": "password"
        })
    
    
@pytest.fixture
def auth_user(created_user):
    user_credential = client.post("/auth/login", data={
        "username": "test.user@gmail.com",
        "password": "password",
        })

    return user_credential.json()