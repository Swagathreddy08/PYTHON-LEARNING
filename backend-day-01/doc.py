from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
@app.get("/doctors/{doctor_id}")
def get_doctor(doctor_id: int):
 return {
 "doctor_id": doctor_id,
 "message": "Here is the requested doctor"
 }

@app.get("/doctors")
def list_doctors(branch: str | None = None, limit: int = 10):
 return {
 "branch_filter": branch,
 "limit": limit
 }
class PatientCreate(BaseModel):
 name: str
 age: int
 department: str
@app.post("/patients")
def create_patient(patient: PatientCreate):
 return {
 "message": "Patient details received",
 "patient": patient.model_dump()
 }
