d={
        }
def add():
    print("do you want a student detalis" )
    q=int(input("How many students ?"))
    if len(d) == 0:
        for i in range(q):
            id = int(input("enter id of student"))
            d[id]={
                'user_id': id,
                        'name': input("name"),
                        'email':input("email"),
                        'role': input("role"),
                        'skills':set((input("skills").lower().split(" ")))
                        }
    else:
        for i in range (len(d),len(d)+q):
            id = int(input("enter id of student"))
            d[id]={
                        'user_id': id,
                                'name': input("name"),
                                'email':input("email"),
                                'role': input("role"),
                                'skills':set((input("skills").lower().split(" ")))
                                }
print('''
========================================
     PRODUCTION INCIDENT ANALYZER
========================================

1. Add
2. 
3. 
4. 
5.  
6. 
7. ''')
while True:
    choice=input("enter your chice ")
    match choice:
        case "1":
            add()
        case _:  
            print("wrong input")

        