cardb=[{"car id":"001","carname":"i20","status":"borrowed","model":"sedan","verification":"pending","borrowed by":"001","days":3,"costofday":1200},
{"car id":"002","carname":"creta","status":"borrowed","model":"sedan","verification":"pending","borrowed by" :"002","days":1,"costofday":1600},
{"car id":"004","carname":"civic","status":"active","model":"sedan","verification":"Done","costofday":1400},
{"car id":"003","carname":"i10","status":"active","model":"sedan","verification":"Done","costofday":1200}]
cdb=[{"cid":"001","cname":"swagath","phone no":"8179524481","email":"swag@gmail.com","driving licence no":"APZ1771H","status":"active" },
     {"cid":"002","cname":"swagath","phone no":"8179524481","email":"swag@gmail.com","driving licence no":"APZ1771H","status":"active"}]
db=[{"cid":"001","cpsw":"test"},{"cid":"002","cpsw":"test"}]
admin={"id":"ADMIN",
       "psw":"Swag@2004"}
def admincheck():
    uid=input("enter the user id : ") 
    psw=input("enter the password : ")
    if uid==admin["id"] and psw == admin["psw"]:
        return True
    else:
        print("enter the correct id and password")
        return admincheck()
def createcheck():  
    uid=input("enter the user id : ") 
    for i in db:
        if uid != i["cid"]:
            
            return True,uid
    else:
        print("user id already exists")
        return createcheck()

def create(cid):
    customer={
        'cid':cid,
        'cpsw':input("enter the password")
    }
    db.append(customer)
    print("user successfully created")
def customercheck():
    uid=input("enter the user id : ") 
    psw=input("enter the password : ")
    for i in db:
        if uid == i["cid"] and psw == i["cpsw"]:
            return True
    else:
        print("enter the correct id and password")
        return customercheck()
def view():
    print(" Hello Admin \n")
    print("1)ALL users \n2)car borrowed users")
    c=input("enter your choice")
    match c:
        case '1':
            for i in cdb:
                print("\n" ,i)
            print("ADVERTIZE YOUR BUSINESS PROPERLY")
        case '2':
            for i in cdb:
                if i["status"]=="borrowed":
                    print("\n",i)
            else:
                print("NO one borrowed cars")

def viewcars():
    print("HEllO BOSS ")
    print("1)All cars \n2)car borrowed ")
    c=input("enter your choice")
    match c:
        case '1':
            for i in cardb:
                print("\n" ,i)
            print("ALL the users finished")
        case '2':
            for i in cardb:
                if i["status"]=="borrowed":
                    print("\n",i)
            else:
                print("NO one borrowed cars")

def validate():
    print("HELLO BOSS \n getting all borrowed cars pending validation list")
    for i in cardb:
        if i["verification"]=="pending":
            print(i,"\n")
            c=input("Did you verified the car for any damage (Yes/No) : ").lower()
            if c=="yes":
                dam=input("did the car is found of any errors (Yes/No) : ").lower() 
                if dam=="yes":
                    for j in cdb:
                        if i["borrowed by"]==j["cid"]:
                            cost=int(input("enter the damage cost "))
                            total=cost+(i["days"]*i["costofday"])
                            j["balance"]=total
                            total=cost=0
                    i.update({"verification":"Done","borrowed by": "","days":"","status":"active"})
                else:
                    for j in cdb:
                        if i["borrowed by"]==j["cid"]:
                            total=(i["days"]*i["costofday"])
                            j["balance"]=total
                            total=0
                    i.update({"verification":"Done","borrowed by": "","days":"","status":"active"})
            else:
                print("verifiy the cars first")

def checkcar(id):
    for i in cardb:
        if i["car id"]==id :
            return False
    else:
        return True
def add():
    print("HELLO BOSS GIVE ME THE NEW CAR DETAILS")
    carid=input("enter the car id")
    if checkcar(carid):
        car={"car id":carid,
         "carname":input("enter the car name"),
         "status":"active",
         "model":input("enter car model"),
         "verification":"Done",
         "costofday":int(input("enter per day ride ammount"))}
        cardb.append(car)
    else:
        print("car id already exist in database")
        add()

def remove():
    print("HELLO BOSS GIVE ME THE NEW CAR DETAILS to be removed from garage")
    carid=input("enter the car id")
    i=0
    if checkcar(carid)== False:
        while i < len(cardb):
            if cardb[i]["car id"]==carid and cardb[i]["status"]=="active":
                cardb.pop(i)
            i+=1
        
        
            

def menuofadmin():
    while True:
        print("\n Admin controls \n")
        print("1)View Customer\n2)view cars\n3)Validate cars\n4)Add car\n5)Remove car\n6)logout")
        c=input("enter your choice")
        match c:
            case '1':
                view()
            case '2':
                viewcars()
            case '3':
                validate()
            case '4':
                add()
            case '5':
                remove()
            case '6':
                break
            case _:
                print("enter the correct input")

def menuofcustomer():
    print("i am customer")  




print("welcome to Swag rentals")
while True:
    print("welcome to login page choose a option from below to log in : ")
    c=input('''1) ADMIN LOGIN
    2)USER LOGIN''')
    match c:
        case '1':
            b=admincheck()
            if b== True:
                menuofadmin()
        case '2':
            st=input("do you have a acc in the rental service (yes/no) ").lower()
            if st == 'yes':
                if customercheck():
                    menuofcustomer()
            elif st== 'no':
                b,uid=createcheck()
                if b == True:
                    create(uid)
                    if customercheck():
                        menuofcustomer()
        case _:
            print("enter correct input")    

