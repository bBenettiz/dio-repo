from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API teste para deploy no azure"}

@app.get("/saudacao/{nome}")
def read_item(nome: str):
    return {"message": f"Olá, {nome}! A API está funcional."}
