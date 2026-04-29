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


def test_listar_tarefas():
    client.post("/tarefas", json={"titulo": "Tarefa 1"})
    client.post("/tarefas", json={"titulo": "Tarefa 2"})
    response = client.get("/tarefas")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_obter_tarefa():
    criada = client.post("/tarefas", json={"titulo": "Comprar pao"}).json()
    response = client.get(f"/tarefas/{criada['id']}")
    assert response.status_code == 200
    assert response.json()["titulo"] == "Comprar pao"


def test_obter_tarefa_inexistente():
    response = client.get("/tarefas/999")
    assert response.status_code == 404


def test_atualizar_tarefa():
    criada = client.post("/tarefas", json={"titulo": "Antiga"}).json()
    response = client.put(
        f"/tarefas/{criada['id']}",
        json={"titulo": "Nova", "concluida": True},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["titulo"] == "Nova"
    assert data["concluida"] is True


def test_atualizar_tarefa_inexistente():
    response = client.put("/tarefas/999", json={"titulo": "X"})
    assert response.status_code == 404


def test_remover_tarefa():
    criada = client.post("/tarefas", json={"titulo": "Para remover"}).json()
    response = client.delete(f"/tarefas/{criada['id']}")
    assert response.status_code == 204
    assert client.get(f"/tarefas/{criada['id']}").status_code == 404


def test_remover_tarefa_inexistente():
    response = client.delete("/tarefas/999")
    assert response.status_code == 404
