import json
from pathlib import Path

PATIENT_DB = Path(__file__).with_name("pat.json")


def vadmin():
    uid=input("ID : ")
    psw=input("password : ")
    k=0
    with open ("projects/Hospital ERP/admin.json","r") as file2:
        data=json.load(file2)
    for i in data:
        if i["uid"]==uid and i["psw"]==psw:
            return True

def vdoc ():
    uid=input("ID : ")
    psw=input("password : ")
    k=0
    with open ("projects/Hospital ERP/doc.json","r") as file2:
        data=json.load(file2)
    for i in data:
        if i["uid"]==uid and i["psw"]==psw:
            return True


def vpat ():
    uid=input("ID : ")
    psw=input("password : ")
    with PATIENT_DB.open("r", encoding="utf-8") as file2:
        data=json.load(file2)
    for i in data:
        if i["uid"]==uid and i["psw"]==psw:
            return True
    else:
        return False

def vcpat(patient_id):
    with PATIENT_DB.open("r", encoding="utf-8") as file2:
        data=json.load(file2)
    for i in data:
        if patient_id == i["uid"]:
            return  True
    else:
        return False

            