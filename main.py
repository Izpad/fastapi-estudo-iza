from fastapi import FastAPI

app = FastAPI(
    title="Minha Primeira API",
    description="API de estudo com FastAPI",
    version="1.0.0",
)


@app.get("/")
def read_root():
    return {"message": "Olá, Mundo! API funcionando com sucesso 🚀"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
