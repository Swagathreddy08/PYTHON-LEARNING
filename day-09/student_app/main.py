import reports,students
import json
from pathlib import Path
from data import*
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
            print("7. Update the data base")
            print("8. Exit")
            c=input("enter the choice")
            match c:
                case "1":
                    students.add()
                case "2":
                    students.updateof()
                case "3":
                    students.delete()
                case "4":
                    students.search()
                case "5":
                    reports.rep()
                case "6":   
                    reports.allstd()
                case "7":
                        file_path = Path(__file__).parent / "student.json"

                        with open(file_path, "w", encoding="utf-8") as file:
                            json.dump(student, file, indent=4)

                        print("Saved data:", student)
                        print("Database updated successfully!")
                case "8":
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