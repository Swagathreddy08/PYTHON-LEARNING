
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

patients = {}


class PatientPublic(BaseModel):
    id: str
    name: str
    department: str


class Pcreate(BaseModel):
    id: int
    name: str
    department: str
    address: str


# CREATE PATIENT
@app.post("/admin/pcreate")
def p_create(p: Pcreate):

    if p.id in patients:
        raise HTTPException(
            status_code=409,
            detail="Patient ID already exists"
        )

    patients[p.id] = p.model_dump()

    return {
        "message": "Patient created successfully",
        "patient": patients[p.id]
    }


# GET PATIENT
@app.get("/patients/{patient_id}", response_model=PatientPublic)
def get_patient(patient_id: int):

    if patient_id not in patients:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )
    patient = patients[patient_id]
    return patient