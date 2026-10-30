from fastapi import FastAPI
from projects import *
app = FastAPI()
@app.get("/")
def home():
 return {"message": "Hospital ERP API is running"}
@app.get("/doctors")
def list_doctors():
 return {"doctors": ["Dr. Rao", "Dr. Meena"]}
@app.get("/patients")
def list_patients():
 return {"patients": ["Patient A", "Patient B"]}


@app.post("/admin_login/admin_menu/doc_create")
def doc_create(doc:doctor):
    with open (DOCTOR_DB,"r")as file:
        doctors=json.load(file)
    
    if doc.uid in doctors:
        return {"ERROR": "URL ID and doctor UID do not match"}

    doctors[doc.uid] = doc.model_dump()

    # Save updated doctor data
    with DOCTOR_DB.open("w") as file:
       json.dump(doctors, file, indent=4)

    return {
        "message": "Doctor created successfully",
        "doctor": doctors[doc.uid]
    }
            
          