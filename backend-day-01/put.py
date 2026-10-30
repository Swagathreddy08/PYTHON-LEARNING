from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class PatientUpdate(BaseModel):
 name: str
 age: int
@app.put("/patients/{patient_id}")
def update_patient( patient_id: int, patient: PatientUpdate, note: str | None = None
):
 return {
 "patient_id": patient_id,
 "updated_patient": patient.model_dump(),
 "note": note
 }
