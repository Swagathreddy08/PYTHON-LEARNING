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
