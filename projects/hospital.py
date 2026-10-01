days={"001":["monday", "wednesday", "friday"]}
admin={"id":"ADMIN",
       "psw":"Swag@2004"}
doctordb=[ {"Doctor ID":"D001",
           "psw":"doc001",
"Name":"Dr. John Doe",
"Department":"Cardiology",
"Specialization":"Heart Disease",
"Consultation fee":50,
"days":days["001"],
"slots":{days["001"][0]:["9:30","10:30","11:30","12:30",],
                        days["001"][1]:["9:30","10:30","11:30","12:30"],
                        days["001"][2]:["9:30","10:30","11:30","12:30"]},
"status":"active"}]

patientdb=[{"Patient ID":"001",
            "psw":"pat001",
"Name":"John Doe",
"Age":30,
"Gender":"Male",
"Phone":"123-456-7890",
"Blood group":"O+",
"status":"Active",
"Appointment":[]}]

def admincheck():
    uid=input("enter the user id : ") 
    psw=input("enter the password : ")
    if uid==admin["id"] and psw == admin["psw"]:
        return True
    else:
        print("enter the correct id and password")
        return admincheck()

def doccheck():
    print("this is doctor check")
    did=input("enter the id")
    dpsw=input("enter the password")
    for i in doctordb:
        if i["Doctor ID"]==did and i["psw"]==dpsw:
            return True
    else:
        print("userid or password is wrong")
        return doccheck()

def pcheck():

    print("this is patient check")
    b=input("DOES THE PATIENT HAVE A ACCOUNT (YES/NO)").lower()
    if b=="yes":
        pid=input("enter the id")
        psw=input("enter the password")
        for i in patientdb:
            if i["Patient ID"]==pid and i["psw"]==psw:
                return True , pid
        else:
            print("userid or password is wrong")
            return pcheck()
    else:
        return False
def pcreatecheck(id):
    for i in patientdb:
        if id == i["Patient ID"]:
            return False
    else:
        return  True

def pcreate():
    id=input("ENTER A NEW ID TO CREATE : ")
    if pcreatecheck(id):
        pd={"Patient ID":id,
            "psw":input("password :"),
"Name":input("Name: "),
"Age":int(input("Age: ")),
"Gender":input("Gender : "),
"Phone":input("phone no : "),
"Blood group":input("Blood Group : "),
"status":"pending",
"Appointment":[]
}
        patientdb.append(pd)
    else:
        print("user already exists")
        pcreate()

def book(pid):
    print("welcome to swag hospitals")
    print("available departments")
    for i in doctordb:
        print(i["Department"])
        dept=input("depatment name : ")
        if i["Department"] == dept:
            print(f"{i["Doctor ID"]} name : {i["Name"]}")
        id=input("Doctor id : ")
    
        if i["Doctor ID"]==id:
            print(i["days"])
        day=input("day selected : ")
        print(i["slots"][day])
        time=input("time : ")
        if i["Doctor ID"] == id:
            i["slots"][day].remove(time)
    for i in patientdb:
        if i["Patient ID"]==pid:
            text={id:f"Appointment with {id} on {day} at {time}"}
            i["Appointment"].append(text)

            

def plogin():
    b,id =pcheck()
    if b == True :
        print("welcome patient")
        while True:
            print("1)\n2)")
            c=input("enter your choice")
            match c:
                case '1':
                    book(id)
                case '2':
                    print("case2")
                case '3':
                    break
                case _:
                    print("enter the correct input")
    else:
        pcreate()
        

def doclogin():
    if doccheck():
        print("welcome admin")
        while True:
            print("1)\n2)")
            c=input("enter your choice")
            match c:
                case '1':
                    print("case 1")
                case '2':
                    print("case2")
                case _:
                    print("enter the correct input")

def valid():
    print("valid")
    for i in patientdb:
        if i["status"] == "pending":
            print("\n",i,"\n")
            b=input("Did you called and verifid (yes/no) : ").lower()
            if b == 'yes':
                i["status"]="active"
            elif b== 'no':
                print("first call and verify u moron")
            else:
                print("give me a proper answer")
                valid()

def checknewdoc(id):
    for i in doctordb:
        if i["Doctor ID"]==id:
            return False
    else:
        return True
def slots(day):
    d={}
    for i in day:
        d[i]=input(f"{i} available timings ").lower().split()
    return d
def add_doc():
    id = input("NEW DOCTOR ID : ")
    day=input("Work Days : ").lower().split()
    days[id]=day
    if checknewdoc(id):
        doc={"Doctor ID":id,
           "psw":input("password : "),
"Name":input("Name : "),
"Department":input("Department : "),
"Specialization":input("Specialization : "),
"Consultation fee":int(input("Fee : ")),
"days":days["001"],
"slots":slots(day),
"status":"active"}
        doctordb.append(doc)

    else:
        print("ID already exits")
        add_doc()


def adminlogin():
    if admincheck():
        print("welcome admin")
        while True:
            print("1)View all doctors\n2)View all patients\n3)Pending verification")
            c=input("enter your choice")
            match c:
                case '1':
                    for i in doctordb:
                        print("\n",i)
                case '2':
                    for i in patientdb:
                        print("\n",i)
                case '3':
                    valid()
                case '4':
                    add_doc()
                case '5':
                    break
                case _:
                    print("enter the correct input")

print("welcome to hospital management system")
while True:
    print("1)Admin\n2)Customer\n3)Doctor\n4)exit")
    c=input("enter your choice")
    match c:
        case '1':
            adminlogin()
        case '2':
            plogin()
        case '3':
            doclogin()
        case '4':
            break
        case _:
            print("enter the correct input")