import reports,students,validation
admin={"UID":"Admin","PSW":"Swag@2004","KEY":"DAD"}
print("WELCOME TO STUDENT DATABASE MANAGEMENT SYSTEM")
id=input("Enter your ID Mr.Admin")
psw=input("Enter your Pasword")
i=0
for i in range(2):
    if admin["UID"]==id and admin["PSW"]==psw:
        while True:
            print("\n===== STUDENT MANAGEMENT SYSTEM =====")
            print("1. Add Student")
            print("2. Update Student")
            print("3. Delete Student")
            print("4. Search Student")
            print("5. Generate Report")
            print("6. Display All Students")
            print("7. Exit")
            c=input("enter the choice")
            match c:
                case "1":
                    add()
                case "2":
                    update()
                case "3":
                    delete()
                case "4":
                    search()
                case "5":
                    report()
                case "6":
                    allstd()
                case "7":
                    break
                case _:
                    print("WRONG INPUT FORM THE USER")
        break
    else:
        print("invalid id or password")
        if i<2:
            id=input("Enter your ID Mr.Admin")
            psw=input("Enter your Pasword")
else:
    print("YOU ARE NOT A REAL ADMIN")