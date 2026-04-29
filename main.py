from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Minha Primeira API",
    description="API de estudo com FastAPI",
    version="1.0.0",
)


class Tarefa(BaseModel):
    titulo: str
    concluida: bool = False


tarefas: dict[int, Tarefa] = {}
proximo_id = 1


@app.get("/")
def read_root():
    return {"message": "Olá, Mundo! API funcionando com sucesso 🚀"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/sobre")
def sobre():
    return {
        "autor": "Izabella",
        "projeto": "API de estudo com FastAPI",
        "tecnologias": ["Python", "FastAPI", "Docker", "GitHub Actions"],
    }


@app.post("/tarefas", status_code=201)
def criar_tarefa(tarefa: Tarefa):
    global proximo_id
    id_tarefa = proximo_id
    tarefas[id_tarefa] = tarefa
    proximo_id += 1
    return {"id": id_tarefa, **tarefa.model_dump()}


@app.get("/tarefas")
def listar_tarefas():
    return [{"id": id_, **t.model_dump()} for id_, t in tarefas.items()]


@app.get("/tarefas/{id_tarefa}")
def obter_tarefa(id_tarefa: int):
    if id_tarefa not in tarefas:
        raise HTTPException(status_code=404, detail="Tarefa nao encontrada")
    return {"id": id_tarefa, **tarefas[id_tarefa].model_dump()}
