from fastapi import APIRouter
router = APIRouter(prefix="/patients", tags=["Patients"])
@router.get("/")
async def list_patients():
 return {"patients": []}
@router.get("/{patient_id}")
async def get_patient(patient_id: str):
 return {"patient_id": patient}