import validation
from data import student
def add():
    id=input("enter the id")
    b=validation.addv(id)
    if b == False:
        cl=int(input("Enter the classs"))
        if cl<4 and cl>=1:
            d={
                "uid":id,
                "name":input("Name : "),
                "class":cl,
                "teacher":input("Teacher Name : "),
                "marks":{"Maths":int(input("Maths Marks : ")),
                        "Science":int(input("Science Marks : ")),
                        "English":int(input("English Marks : ")),
                        "Telugu":int(input("Telugu Marks : ")),
                        "Social":int(input("Social Marks : "))
                }
            
            }
        elif cl<6 and cl>=4:
            d={
                "uid":id,
                "name":input("Name : "),
                "class":cl,
                "teacher":input("Teacher Name : "),
                "marks":{"Maths":int(input("Maths Marks : ")),
                        "Science":int(input("Science Marks : ")),
                        "English":int(input("English Marks : ")),
                        "Telugu":int(input("Telugu Marks : ")),
                        "Hindi":int(input("Hindi Marks : ")),
                        "Social":int(input("Social Marks : "))
                                    }
            }
        elif cl<=10 and cl>=6:
                    d={
                        "uid":id,
                        "name":input("Name : "),
                        "class":cl,
                        "teacher":input("Teacher Name : "),
                        "marks":{"Maths":int(input("Maths Marks : ")),
                                "Science":int(input("Science Marks : ")),
                                "English":int(input("English Marks : ")),
                                "Telugu":int(input("Telugu Marks : ")),
                                "Hindi":int(input("Hindi Marks : ")),
                                "Social":int(input("Social Marks : "))
                                            }
                    }
        student.append(d)
    else:
        print("ID ALREADY EXISTS")
        add()

def updateof():
    id=input("enter the id")
    b=validation.addv(id)
    if b:
         print("THIS IS UPDATE METHOD THE OPTIONS ARE LISTED BELOW")
         print("1)Name\n2)Class\n3)Teacher\n4)Marks")
         ch=input()
         match ch:
            case "1":
                print("Name Change \n")
                for i in student:
                    if i["uid"]==id:
                        i["name"]=input("Name : ")
            case "2":
                   print("Class Update")
                   for i in student:
                        if i["uid"]==id:
                            i["class"]=input("Class : ")
            case "3":
                   print("Teacher Update")
                   for i in student:
                        if i["uid"]==id:
                            i["teacher"]=input("Name of teacher : ")
            case "4":
                   print("Marks Update")
                   for i in student:
                        if i["uid"]==id:
                            print(i["marks"].keys())
                            sub=input("enter a subject : ")
                            if sub in i["marks"]:
                                i["marks"][sub]=input(f"enter the marks of {sub}: ")
                            else:
                                 print("Invalid Subject")                         
                            break
                

def delete():
    id=input("enter the id")
    b=validation.addv(id)
    if b:
        for i in student:
            if i["uid"]==id:
                print(i)
                student.remove(i)
    else:
        print("user doesnot exists")

def search():
    id=input("enter the id")
    b=validation.addv(id)
    if b:
        for i in student:
            if i["uid"]==id:
                print(i)
    else:
        print("User doesnot Exists")  
                            
                            

                   
