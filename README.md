# fastapi-estudo-iza

Projeto de estudo de DevOps com FastAPI, GitHub Actions (CI/CD) e Docker.

## Como rodar localmente

```bash
python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate

pip install -r requirements.txt
uvicorn main:app --reload
```

Acesse:

- API: http://127.0.0.1:8000
- Swagger: http://127.0.0.1:8000/docs

## Rodar os testes

```bash
pytest tests/ -v
```
