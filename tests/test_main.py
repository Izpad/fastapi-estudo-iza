from fastapi.testclient import TestClient

from main import app, tarefas

client = TestClient(app)


def setup_function():
    tarefas.clear()


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


def test_criar_tarefa():
    response = client.post("/tarefas", json={"titulo": "Estudar FastAPI"})
    assert response.status_code == 201
    data = response.json()
    assert data["titulo"] == "Estudar FastAPI"
    assert data["concluida"] is False
    assert "id" in data
