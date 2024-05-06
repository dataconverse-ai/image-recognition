from fastapi.testclient import TestClient
from src.image_recognition.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/api/v1/images/test/")
    assert response.status_code == 200
    assert response.json() == {"message": "Test API endpoint is working"}
