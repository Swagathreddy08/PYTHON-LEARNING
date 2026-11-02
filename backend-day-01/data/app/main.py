from fastapi import FastAPI
from app.routers import patients
app = FastAPI(title="Hospital ERP API")
app.include_router(patients.router)
@app.get("/")
async def home():
 return {"message": "Hospital ERP API is running"}