import json
from pathlib import *
from valid import *
from create import *
from menu import *

PATIENT_DB = Path(__file__).with_name("pat.json")
print("WELCOME TO HOSPITAL MANAGEMENT SYSTEM")
print("Choose a option to select ")
while True:
    ch=input('''
    1)Admin
    2)Doctor
    3)Patient
    ''')
    match ch:
        case "1":
            b=vadmin()
            if b==True:
                madmin()
            else:
                print("Admin Doesnot Exists ")
                pass
        case "2":
            b=vdoc()
            if b==True:
                mdoc()
            else:
                print("Doctor Doesnot Exists")
                pass
        case "3":
            b =vpat()
            if b==True:
                mpat()
            elif b=="PARTIAL":
                print("Patient is not still active by the user let management call you")
            elif b==False:
                print("Patient Doesnot Exists")
                patient_id = input("Enter the ID to create")
                if vcpat(patient_id):
                    print("user already exists")
                else:
                    patient = pcreate(patient_id)
                    with PATIENT_DB.open("r") as file2:
                        patients = json.load(file2)
                    patients.append({
                        "uid": patient.id,
                        "psw": patient.psw,
                        "name": patient.name,
                        "ref": patient.ref,
                        "phno": patient.num,
                        "address": patient.add,
                        "Status": "Inactive"
                    })
                    with PATIENT_DB.open("w") as file2:
                        json.dump(patients, file2, indent=2)
                    print("Patient created")
        case _:
            print("Enter a proper choice ")
