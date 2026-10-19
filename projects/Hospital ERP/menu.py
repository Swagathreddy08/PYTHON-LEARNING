import json
from pathlib import *
from create import *

DOCTOR_DB = Path(__file__).with_name("doc.json")
ADMIN_DB = Path(__file__).with_name("admin.json")
PATIENT_DB=Path(__file__).with_name("pat.json")
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
                if vcdoc(doctor_id):
                    print("user already exists")
                else:
                    patient = dcreate(doctor_id)
                    with DOCTOR_DB.open("r") as file2:
                        Doctor = json.load(file2)
                    Doctor.append({
                                        "uid": patient.id,
                                        "psw": patient.psw,
                                        "name": patient.name,
                                        "ref": patient.ref,
                                        "phno": patient.num,
                                        "address": patient.add
                                    })
                    with DOCTOR_DB.open("w") as file2:
                        json.dump(Doctor, file2, indent=2)
                    print("Patient created")
            case "2":
                with PATIENT_DB.open("r") as file2:
                    patient=json.load(file2)
                for i in patient:
                    if i["status"]=="inactive":
                        print(i)
                        reply=input("Did you call and verify the Patient ? ( Yes / No ): ").lower()
                        if reply == "yes":
                            i["status"]="active"
                            print("The patient is active ")
                        elif reply == "no":
                            print("verify first and come back ")
                        else:
                            print("Wrong Input")
                else:
                    print("All the patients are verified and active ")
                
            case "3":
                print("leave request")
            case "4":
                print("ALL details")
            case "5":
                print("Remove doctor")
            case "6":
                print("New admin")
                admin_id = input("Enter the ID to create")
                if vcdoc(admin_id):
                    print("user already exists")
                else:
                    patient = acreate(admin_id)
                    with ADMIN_DB.open("r") as file2:
                        ADMINS = json.load(file2)
                    ADMINS.append({
                                        "uid": patient.id,
                                        "psw": patient.psw,
                                        "name": patient.name,
                                        "phno": patient.num,
                                        "address": patient.add
                                    })
                    with ADMIN_DB.open("w") as file2:
                        json.dump(ADMINS, file2, indent=2)
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
                print("Leave request")
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