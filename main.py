#FASTAPI - UVICORN
#pip install fastapi uvicorn

from typing import Optional
from pydantic import BaseModel, EmailStr

class Persona(BaseModel):
    id: Optional[int] = None
    nombre: str
    edad: int
    email: EmailStr

from fastapi import FastAPI, HTTPException

app = FastAPI()

#Base de datos simulada con un array
persona_db = []
#Crear persona
@app.post("/persona/", response_model=Persona)
def crear_persona(persona:Persona):
    persona.id = len(persona_db) +1
    persona_db.append(persona)
    return persona

#Ver persona por id
@app.get("/personas/{persona_id}", response_model=Persona)
def obtener_persona(persona_id: int):
    for persona in persona_db:
        if persona.id == persona_id:
            return persona
        raise HTTPException(status_code=404, detail="Persona no encontrada")

#Listar personas
@app.get("/personas/", response_model=list[Persona])
def listar_persona():
    return persona_db   

#Actualizar personas
@app.put("/personas/{persona_id}", response_model=Persona)
def actualizar_persona(persona_id: int, persona: Persona):
    for index, persona in enumerate(persona_db):
        if persona.id == persona_id:
            persona_db[index] = persona
            return persona
    raise HTTPException(status_code=404, detail="Persona no encontrada")

#Eliminar personas
@app.delete("/personas/{persona_id}", response_model=Persona)
def eliminar_persona(persona_id: int):
    for index, persona in enumerate(persona_db):
        if persona.id == persona_id:
            del persona_db[index]
            return {"message": "Persona eliminada"}
    raise HTTPException(status_code=404, detail="Persona no encontrada")
