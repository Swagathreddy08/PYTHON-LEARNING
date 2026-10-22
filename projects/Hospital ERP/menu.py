import json
from pathlib import Path
from datetime import *

from create import acreate, dcreate

DOCTOR_DB = Path(__file__).with_name("doc.json")
ADMIN_DB = Path(__file__).with_name("admin.json")
PATIENT_DB = Path(__file__).with_name("pat.json")


def madmin():
    while True:
        ch=input('''
1)New Doctor
2)New Patients
3)Leave Aproval
4)All the details of hospital
5)Remove Doctor
6)New Admin
7)LOG OUT 
''')
        match ch:
            case "1":
                doctor_id = input("Enter the ID to create")
                with DOCTOR_DB.open("r") as file:
                    doctors = json.load(file)
                if any(record.get("uid") == doctor_id for record in doctors):
                    print("user already exists")
                else:
                    doctor = dcreate(doctor_id)
                    doctors.append({
                        "uid": doctor.id,
                        "psw": doctor.psw,
                        "name": doctor.name,
                        "branch": doctor.branch,
                        "phno": doctor.num,
                        "address": doctor.add
                    })
                    with DOCTOR_DB.open("w") as file:
                        json.dump(doctors, file, indent=2)
                    print("Doctor created")
            case "2":
                with PATIENT_DB.open("r") as file:
                    patients = json.load(file)
                pending_patients = False
                for patient in patients:
                    if patient.get("Status", patient.get("status", "")).lower() == "inactive":
                        pending_patients = True
                        print(patient)
                        reply=input("Did you call and verify the Patient ? ( Yes / No ): ").lower()
                        if reply == "yes":
                            patient["Status"] = "active"
                            if "status" in patient:
                                patient["status"] = "active"
                            print("The patient is active ")
                        elif reply == "no":
                            print("verify first and come back ")
                        else:
                            print("Wrong Input")
                if pending_patients:
                    with PATIENT_DB.open("w") as file:
                        json.dump(patients, file, indent=2)
                else:
                    print("All the patients are verified and active ")
                
            case "3":
                with DOCTOR_DB.open("r") as file:
                    doctors = json.load(file)
                for record in doctors:
                    if record.get("Leave Status") == "Waiting":
                        print(record.get("uid"))
                        print(record.get("Leave"))
                        print(record.get("Reason"))
                        responce=input("Do you want to accept the leave request (YES/NO)").lower()
                        if responce =="yes":
                            record["Leave Status"]="Accepted"
                            record.pop("Reason")
                            with DOCTOR_DB.open("w") as file:
                                json.dump(doctors, file, indent=2)
                        elif responce== "no":
                            print("THE leave will be rejected")
                            record["Leave Status"]= "Rejected"
                            record.pop("Leave")
                            record.pop("Reason")
                            with DOCTOR_DB.open("w") as file:
                                json.dump(doctors, file, indent=2)
                        else:
                            print("wrong input")
            case "4":
                print("Hospital Report")
                print("DOCTOR REPORTS")
                with DOCTOR_DB.open("r")as file:
                    doctors = json.load(file)
                for doctor in doctors:
                    print(f'''
                    NAME: {doctor.get("name")}
                    Branch : {doctor.get("branch")}
                    Phno : {doctor.get("phno")}
                    ''')
                    print("\n")
                with PATIENT_DB.open("r") as file:
                    patient = json.load(file)
                for pat in patient:
                    print(f'''
                    NAME: {pat.get("name")}
                    Branch : {pat.get("branch")}
                    Phno : {pat.get("phno")}
                    ''')
                    print("\n")
                    
                    
            case "5":
                id2=input("enter the id to delete : ")
                with DOCTOR_DB.open("r") as file:
                    doctors = json.load(file)
                for doctor in doctors:
                    if doctor["uid"] == id2:
                        doctors.remove(doctor)
                        with DOCTOR_DB.open("w") as file:
                            json.dump(doctors, file, indent=2)
                        print("Doctor successfully removed")
                        break
                else:
                    print("DOCTOR ID DOESNOT EXISTS IN THE DATABASE")
            case "6":
                print("New admin")
                admin_id = input("Enter the ID to create")
                with ADMIN_DB.open("r") as file:
                    admins = json.load(file)
                with DOCTOR_DB.open("r") as file:
                    doctors = json.load(file)
                if any(record.get("uid") == admin_id for record in admins + doctors):
                    print("user already exists")
                else:
                    admin = acreate(admin_id)
                    admins.append({
                        "uid": admin.id,
                        "psw": admin.psw,
                        "name": admin.name,
                        "phno": admin.num,
                        "address": admin.add
                    })
                    with ADMIN_DB.open("w") as file:
                        json.dump(admins, file, indent=2)
                    print("Admin created")
            case "7":
                break
            case _:
                print("Wrong Input")

def mdoc():
    while True:
        ch=input('''
1)View appointments
2)leave
3)LOG OUT''')
        match ch:
            case "1":
                print("view appointments")
            case "2":
                print("Hello Doctor this is a leave request application")
                try:
                    id=input('Doctor id : ')
                    date=input("Enter leave date (YYYY-MM-DD): ")
                    x = datetime.strptime(date, "%Y-%m-%d")
                    print()
                    with DOCTOR_DB.open("r") as file:
                        doctors = json.load(file)
                    for record in doctors:
                        if record.get("uid") == id :    
                            record["Leave"]=(f"{x.strftime("%Y-%m-%d")} : {x.strftime("%A")}")
                            record["Leave Status"]="Waiting"
                            record["Reason"]=input("Enter the leave reason")
                            with DOCTOR_DB.open("w") as file:
                                json.dump(doctors, file, indent=2)
                        else:
                            print("doctor doesnot exists")
                except ValueError as val:
                    print("WONG INPUT TRY AGAIN")
            case "3":
                break
            case _ :
                print("wrong input")

def mpat():
    while True:
        ch=input('''
        1)Book Appointment
        2)Medical History
        3)Appointment 
        4)Logout
        ''')
        match ch:
                    case "1":
                        print("Hello dear patient welcome to appoint booking")
                        with DOCTOR_DB.open("r") as file:
                            doctors = json.load(file)
                        x=input('''Departments Avalilable
                        1)cardiology
                        2)ent
                        3)general physician
                        4)neurology
                        ''')
                        match x:
                            case "1":
                                for rec in doctors:
                                    if rec.get("dept")=="Cardiology" :
                                        print(f"{rec.get("uid")} : {rec.get("name")} : {rec.get("dept")} : {rec.get("breanch")}")
                                    id2=input("Enter the doctor id")

                    case "2":
                        print("Medical History")
                    case "3":
                        print("Appointment")
                    case "4":
                        break
                    case _ :
                        print("wrong input")