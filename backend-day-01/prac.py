from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
import json
from pathlib import Path
app=FastAPI()

class docdisplay(BaseModel):
    id:str= Field(validation_alias="uid")
    Name:str= Field(validation_alias="name")
    age:int
    number:str= Field(validation_alias="phno")
    address:str

class doc_cr(BaseModel):
    uid: str=Field(min_length=3)
    psw: str=Field(min_length=8)
    name:str=Field(max_length=20)
    age:int
    dept: str
    branch: str
    phno: str
    address: str

class docUpdate(BaseModel):
    name:str=Field(max_length=20)
    age:int
    dept: str
    branch: str
    phno: str
    address: str

DOCTOR_DB=Path(__file__).with_name("doc.json")
@app.get("/GET_Doc_Details/{doc_id}", response_model=docdisplay)
def display(doc_id : str):
    with open (DOCTOR_DB,"r") as file:
        doctors = json.load(file)
    if doc_id in doctors:
        return doctors[doc_id]
    else:
            raise HTTPException(
                status_code=404,
                detail="Patient not found"
            )
        

@app.post("/Doc_Create")
def create(doctor:doc_cr):
    with open (DOCTOR_DB,"r") as file:
        doctors = json.load(file)
    if doctor.uid not in doctors:
        doctors[doctor.uid]= doctor.model_dump()
        with open (DOCTOR_DB,"w") as file:
            json.dump(doctors,file)
        return {
                "message": "Doctor created successfully",
                "doctor": doctors[doctor.uid]
            }
    else:
        raise HTTPException(
            status_code=409,
            detail="User already exists"
        )


@app.put("/patients/{doc_id}")
def update_patient( doc_id: str, patient: docUpdate):
    with open (DOCTOR_DB,"r") as file:
        doctors = json.load(file)
    if doc_id in doctors: 
        updated_doc= patient.model_dump()
        doctors[doc_id].update(updated_doc)
        with open (DOCTOR_DB,"w") as file:
            json.dump(doctors,file)
        return {
            "message": "Doctor updated successfully",
            "doctor": doctors[doc_id]
        }

    else:
        raise HTTPException(
            status_code=404,
            detail="Doctor not found"
        )


