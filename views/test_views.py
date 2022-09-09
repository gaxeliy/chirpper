from starlette.testclient import TestClient

from views.views import app

client = TestClient(app)


def test_create_chirp():
    response = client.post('/create', json={
        "author": {
            "login": "vasya",
            "name": "Vasya"
        },
        "text": "Hello!",
        "replies": [],
        "publish_date": "2022-09-09T16:12:43.910Z"
    })
    assert response.status_code == 200
