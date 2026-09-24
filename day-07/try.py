d={
        }

def check(id2):
    if id2 in d:
        print("id alredy exist")
        return True
    else:
        return False
    
def add():
    print("do you want a student detalis" )
    q=int(input("How many students ?"))
    if len(d) == 0:
        for i in range(q):
            id2 = int(input("enter id of student"))
            id=check(id2)
            if id==False:
                d[id2]={
                    'user_id': id2,
                            'name': input("name"),
                            'email':input("email"),
                            'subjects':list((input("skills").lower().split(" "))),
                            'marks': int(input("enter the marks")),
                            'attandence':int(input("enter the attandence percentage")),
                            'skills': set(input("enter the skills ").lower().split(" ")),
                            'status':input("enter the acc status(active/inactive)").lower()                        
                            }
            else:
                id2 = int(input("enter id of student"))
                id=check(id2)

    else:
        for q in range (len(d),len(d)+q):
            id2=int(input("enter the id of students"))
            id=check(id2)
            if id==False:
                d[id2]={
                            'user_id': id2,
                                'name': input("name"),
                                'email':input("email"),
                                'subjects':list((input("skills").lower().split(" "))),
                                'marks': int(input("enter the marks")),
                                'attandence':int(input("enter the attandence percentage")),
                                'skills': set(input("enter the skills ").lower().split(" ")),
                                'status':input("enter the acc status(active/inactive)").lower()
                                                        
                                    }
            else:
                
                id2 = int(input("enter id of student"))
                id=check(id2)


def view():
    print(d)
def find():
    id2 = int(input("enter id of student"))
    id=check(id2)
    if id == True:
        print(d[id2])
    else:
        print("User not found")
def delete():
    id2 = int(input("enter id of student"))
    id=check(id2)
    if id == True:
        del d[id2]
    else:
        print("user is a ghost")

def unique():
    s=set()
    for i in d:
        s.union(d[i]['skills'])

    print("the unique skills are :")
    print(s)

print('''


========================================
    student engine
========================================

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Student Statistics
7. unique skills
8. Exit''')
while True:
    choice=input("enter your chice ")
    match choice:
        case "1":
            add()
        case "2":
            view()
        case "3":
            find()
        case "7":
            unique()
        case _:  
            print("wrong input")

        