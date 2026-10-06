days={"001":["monday", "wednesday", "friday"]}
admin={"id":"ADMIN",
       "psw":"Swag@2004"}
a=d=p=1
doctordb=[ {"Doctor ID":"D001","psw":"doc001","Name":"Dr. John Doe","Department":"Cardiology",
"Specialization":"Heart Disease","Consultation fee":50,"days":days["001"],"slots":
{days["001"][0]:["9:30","10:30","11:30","12:30",],days["001"][1]:["9:30","10:30","11:30","12:30"],
 days["001"][2]:["9:30","10:30","11:30","12:30"]},"status":"leave aproval","Appointment":[],
 "leave":{"day":"monday","reason":"Feaver"}
 }]
patientdb=[{"Patient ID":"001","psw":"pat001","Name":"John Doe","Age":30,"Gender":"Male","Phone":"123-456-7890",
"Blood group":"O+","status":"active","Appointment":[]}]

def admincheck():

    global a
    if a<=5:
        uid=input("enter the user id : ") 
        psw=input("enter the password : ")
        if uid==admin["id"] and psw == admin["psw"]:
            a+=1
            return True
        else:
            print("enter the correct id and password")
            a+=1
            return admincheck()
    else:
        print("limit exausted")
        return False
def doccheck():
    global d
    if d<5:
        print("this is doctor check")
        did=input("enter the id")
        dpsw=input("enter the password")
        for i in doctordb:
            if i["Doctor ID"]==did and i["psw"]==dpsw:
                d+=1
                return True,did
        else:
            print("userid or password is wrong")
            d+=1
            return doccheck()
    else:
        print("limit exausted")
        return False,None
def pcheck():
    global p
    
    print("this is patient check")
    if p<5:
            pid=input("enter the id")
            psw=input("enter the password")
            for i in patientdb:
                if i["Patient ID"]==pid and i["psw"]==psw:
                    p+=1
                    return True , pid
            else:
                print("userid or password is wrong")
                p+=1
                return pcheck()
    else:
            print("limit exausted")
            return False,None
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
def cdept():
    s= set()
    for i in doctordb:
        s.add(i["Department"])
    print(s)
    dept=input("Depatment Name : ")
    if dept in s:
            return dept
    else:
        print("Wrong choice")
        return cdept()
def cdid(dept):
    for i in doctordb:
        if i["Department"]==dept:
            print(f"{i["Doctor ID"]} : {i["Name"]}")
    did=input("Enter Doctor ID")
    for i in doctordb:
        if i["Department"]==dept and i["Doctor ID"]==did:
            return did
    else:
        return cdid(dept)
def cday(dept,did):
    for i in doctordb:
        if i["Department"]==dept and i["Doctor ID"]==did:
            if i["status"]=="active":
                for j in i["days"]:
                    print(j)
            elif i["status"]in["leave","leave aproval"]:
                for j in i["days"]:
                    if j != i["leave"]["day"]:
                        print(j)
    day=input("enter the day of appointment : ")
    for i in doctordb:
        if i["Department"]==dept and i["Doctor ID"]==did:
            if  i["status"]=="active":
                if day in i["days"]:
                    return day
                else:
                    print("Not a working day")
                    return cday(dept,did)

            elif i["status"]in["leave","leave aproval"]:
                if day != i["leave"]["day"]:
                    if day in i["days"]:
                        return day
                    else:
                        print("Not a working day")
                        return cday(dept,did)
                    
            else:
                return cday(dept,did)          
def ctime(dept,did,day):
    for i in doctordb:
         if i["Department"]==dept and i["Doctor ID"]==did:
            if i["status"]=="active":
                print(i["slots"][day])
            elif i["status"] in ["leave","leave aproval"]:
                if day != i["leave"]["day"]:
                    print(i["slots"][day])
    time=input("Enter the time : ")
    for i in doctordb:
        if i["Department"]==dept and i["Doctor ID"]==did:
            if  i["status"]=="active":
                if time in i["slots"][day]:
                    return time
                else:
                    return ctime(dept,did,day)
            elif i["status"] in ["leave","leave aproval"]:
                if day != i["leave"]["day"]:
                    if time in i["slots"][day]:
                        return time
                    else:
                        return ctime(dept,did,day)
            else:
                return ctime(dept,did,day)    
def book(pid):
    print("welcome to swag hospitals")
    dept=cdept()
    did=cdid(dept)
    day=cday(dept,did)
    time=ctime(dept,did,day)
    for i in doctordb:
        if i["Doctor ID"] == did:
            i["slots"][day].remove(time)
            i["Appointment"].append({pid:f"Appointment with {pid} on {day} at {time}"})
    for i in patientdb:
        if i["Patient ID"]==pid:
            text={did:f"Appointment with {did} on {day} at {time}"}
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
def leave(id):
    for i in doctordb:
        if i["Doctor ID"] == id:
            leaves=input("Enter the day of the leave : ")
            reason=input("Reason : ")
            lv={"day":leaves,"reason":reason}
            i["leave"]=lv
            i["status"]="leave aproval"
def pbookcheck(id):
    for i in doctordb:
        if i["Doctor ID"]==id:
            print(i["Appointment"])
def doclogin():
    b,id = doccheck()
    if b==True:
        print("welcome admin")
        while True:
            print("1)Patient Check \n2)Leave")
            c=input("enter your choice")
            match c:
                case '1':
                    pbookcheck(id)
                case '2':
                    leave(id)
                case '3':
                    break
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
    if checknewdoc(id):
        day=input("Work Days : ").lower().split()
        if day in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
            days[id]=day
        else:
            add_doc()
        doc={"Doctor ID":id,
           "psw":input("password : "),
"Name":input("Name : "),
"Department":input("Department : "),
"Specialization":input("Specialization : "),
"Consultation fee":int(input("Fee : ")),
"days":days[id],
"slots":slots(day),
"status":"active",
"Appointment":[]}
        doctordb.append(doc)

    else:
        print("ID already exits")
        add_doc()
def leaveap():
    print("ADMIN LEAVE APROVAL FOR DOCTORS")
    for i in doctordb:
        if i["status"]=="leave aproval":
            print(f"ID : {i["Doctor ID"]}\n Name : {i["Name"]}\n leave day : {i["leave"]["day"]} \n Reason : {i['leave']["reason"]}")
            b=input(f"Do you want to aprove the leave for the {i['Name']}(Yes/No)").lower()
            if b=="yes":
                i["status"]="leave"
                for j in patientdb:
                    j["Appointment"]["Doctor ID"]="cancled"
            elif b=="no":
                i["status"]="active"
            else:
                print("enter a valid input")
                leaveap()
def adminlogin():
    if admincheck():
        print("welcome admin")
        while True:
            print("1)View all doctors\n2)View all patients\n3)Pending verification\n4)Add Doctor\n5)Leave aproval\n6)Exit")
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
                    leaveap()
                case '6':
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