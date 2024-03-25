from firebase_admin import auth
from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)

def test_create_session_success(auth_user):
    res = client.post("/sessions", headers={
        "Authorization": f"Bearer {auth_user['access_token']}"
        }, json={
            "name": "test session"
        })
    assert res.status_code == 201
    

# Exercises create a test for the following cases:
# 1. Test create session without authentification
# 2. Test create session with invalid authentification
# 3. Test create session with invalid data
# 4. Test create session with valid data but invalid authentification
# 5. Test get sessions success (We need to create the session first.) => fixture
# 6. Test get sessions without authentification
# 7. Test delete session success (We need to create the session first.) => fixture
# 9. Test update session success (We need to create the session first.) => fixture

#Afternoon project
    #1. List test scenarios
    #2. Create test scenarios
