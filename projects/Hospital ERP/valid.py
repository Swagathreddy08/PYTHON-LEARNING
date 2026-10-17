import json
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
    k=0
    with open ("projects/Hospital ERP/pat.json","r") as file2:
        data=json.load(file2)
    for i in data:
        if i["uid"]==uid and i["psw"]==psw:
            return True
    else:
        return False

def vcpat(id):
    with open ("projects/Hospital ERP/pat.json","r") as file2:
        data=json.load(file2)
    for i in data:
        if id == i["uid"]:
            return  True
    else:
        return False

            