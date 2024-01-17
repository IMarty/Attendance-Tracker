from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_session_success(auth_user):
    res = client.post("/sessions",headers={
        "Authorization": f"Bearer {auth_user['access_token']}",
        }, json={
            "name": "test.session"
        })
    assert res.status_code == 201

# test_create_session_conflict => fixture
# test_create_session_unauthorized
# test_create_session_bad_request
    

#Afternoon project
    #1. List test scenarios
    #2. Create test scenarios