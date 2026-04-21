from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Olá, Mundo! API funcionando com sucesso 🚀"}


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_sobre():
    response = client.get("/sobre")
    assert response.status_code == 200
    data = response.json()
    assert "autor" in data
    assert "tecnologias" in data
