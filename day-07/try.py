d={
        }

def check(id2):
    if id2 in d:
        print("id alredy exist")
        id=int(input("enter the id of students"))
        i=check(id)
    else:
        return i
    
def add():
    print("do you want a student detalis" )
    q=int(input("How many students ?"))
    if len(d) == 0:
        for i in range(q):
            id2 = int(input("enter id of student"))
            id=check(id2)
            d[id]={
                'user_id': id,
                        'name': input("name"),
                        'email':input("email"),
                        'role': input("role"),
                        'skills':set((input("skills").lower().split(" ")))
                        }
    else:
        for q in range (len(d),len(d)+q):
            id2 = int(input("enter id of student"))
            id2=int(input("enter the id of students"))
            id=check(id)
            d[id]={
                        'user_id': id,
                                'name': input("name"),
                                'email':input("email"),
                                'role': input("role"),
                                'skills':set((input("skills").lower().split(" ")))
                                }
def view():
    print(d)
def find():
    id2 = int(input("enter id of student"))
    id=check(id2)
    print(d[id2])
def delete():
    id2 = int(input("enter id of student"))
    id=check(id2)
    del d[id]

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
7. Exit''')
while True:
    choice=input("enter your chice ")
    match choice:
        case "1":
            add()
        case "2":
            view()
        case "3":
            find()
        case _:  
            print("wrong input")

        