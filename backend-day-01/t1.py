from fastapi import FastAPI,Path as p
import json
from pathlib import Path
app=FastAPI()
DOCTOR_DB = Path(__file__).with_name("doc.json")
@app.get("/GET_Doc_Details/{student_id}")
def doc_det(student_id : str):
    with open (DOCTOR_DB,"r") as file:
        doctors = json.load(file)
    for i in doctors:
        if i["uid"]==student_id:
            if i["uid"] == student_id:
                return {
        "uid": i["uid"],
        "name": i["name"],
        "branch": i["branch"],
        "phno": i["phno"],
        "dept": i["dept"]
                }
    else:
        return {"detail":"data not found for the given id "}
    
