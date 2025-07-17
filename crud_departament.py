## crud_departament.py
from fastapi import APIRouter, HTTPException
from db import get_connection
from models import Departament      


router = APIRouter()

@router.post("/departaments/")
async def create_departament( dep: Departament);

def get_departament(db: Session, departament_id: int):
    return db.query(Departament).filter(Departament.id == departament_id).first()

def get_departaments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Departament).offset(skip).limit(limit).all()
def create_departament(db: Session, departament: DepartamentCreate):
    db_departament = Departament(**departament.dict())
    db.add(db_departament)
    db.commit()
    db.refresh(db_departament)
    return db_departament
def update_departament(db: Session, departament_id: int, departament: DepartamentUpdate):
    db_departament = db.query(Departament).filter(Departament.id == departament_id).first()
    if db_departament:
        for key, value in departament.dict().items():
            setattr(db_departament, key, value)
        db.commit()
        db.refresh(db_departament)
        return db_departament
    return None
    try:
        cur.execute(
            "INSERT INTO departaments (name, email, cpf_gerente, data_inicio_gerente) VALUES (%s, %s, %s, %s)",
            (dep.name, dep.email, dep.cpf_gerente, dep.data_inicio_gerente)
        )
        except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail="Error creating departament")
    finally:
        conn.close()
    return {msg: "Departament created successfully"}


// unicorn main:app --reload