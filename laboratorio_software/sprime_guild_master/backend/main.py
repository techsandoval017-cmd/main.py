from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="S-Prime Guild Master | S-Prime Corp", version="1.0")

class OrdenDirector(BaseModel):
    comando: str
    parametros: dict

@app.get("/")
def estado_sistema():
    return {"status": "online", "sistema": "S-Prime Guild Master", "dominio": "Project Management / Scrum"}

@app.post("/ejecutar")
def ejecutar_orden(req: OrdenDirector):
    # TODO: Lógica de ejecución de sombras (Goku / Arquitecto)
    return {"status": "success", "mensaje": f"Orden '{req.comando}' asimilada por S-Prime Guild Master."}
