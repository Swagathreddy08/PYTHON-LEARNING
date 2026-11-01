from fastapi import FastAPI
from pydantic import BaseModel,Field
import json
from pathlib import Path

app=FastAPI()
DOCTOR_DB = Path(__file__).with_name("doc.json")

class doctor(BaseModel):
    uid: str=Field(min_length=4 ,max_length=8)
    psw: str=Field(min_length=8)
    name: str=Field(max_length=20)
    dept: str=Field(max_length=4)
    branch: str=Field(min_length=3)
    phno: str=Field(max_length=10)
    address: str
    num: int = Field(gt=0,lte=20)

@app.post("/admin_login/admin_menu/doc_create/{doc_id}")
def doc_create(doc_id :str , doc:doctor):
    with open (DOCTOR_DB,"r")as file:
        doctors=json.load(file)
    if doc_id not in doctors:
        if doc_id != doc.uid:
            return {"ERROR": "URL ID and doctor UID do not match"}

    # Convert Pydantic model to dictionary
        doctors[doc_id] = doc.model_dump()

    # Save updated doctor data
        with DOCTOR_DB.open("w") as file:
            json.dump(doctors, file, indent=4)

        return {
        "message": "Doctor created successfully",
        "doctor": doctors[doc_id]
    }
            
    else:
        return {"ERROR" : "THE id already exisits"}