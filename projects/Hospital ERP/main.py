from valid import *
from create import *
from menu import *
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
            b=vpat()
            if b==True:
                mpat()
            elif b==False:
                print("Patient Doesnot Exists")
                id=input("Enter the ID to create")
                if vcpat(id):
                    patient=pcreate(id)
                    with open ("projects/Hospital ERP/pat.json","w") as file2:
                        json.load(patient)
                else:
                    print("user already exists")
        case _:
            print("Enter a proper choice ")

