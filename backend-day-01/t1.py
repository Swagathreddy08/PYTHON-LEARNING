from fastapi import FastAPI,Path as p
from pydantic import BaseModel
import json
from pathlib import Path
app=FastAPI()
DOCTOR_DB = Path(__file__).with_name("doc.json")

class doctor(BaseModel):
    uid: str
    psw: str
    name: str
    dept: str
    branch: str
    phno: str
    address: str
    
  
@app.get("/GET_Doc_Details/{student_id}")
def doc_det(student_id : str):
    with open (DOCTOR_DB,"r") as file:
        doctors = json.load(file)
    if student_id in doctors:
        return {
        "uid": doctors[student_id]["uid"],
        "name": doctors[student_id]["name"],
        "branch": doctors[student_id]["branch"],
        "phno": doctors[student_id]["phno"],
        "dept": doctors[student_id]["dept"]
                }
    else:
        return {"detail":"data not found for the given id "}

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
        