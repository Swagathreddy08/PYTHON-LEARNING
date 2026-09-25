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
                    'id': id2,
                        'name': input("name"),
                        'email':input("email"),
                        'subjects':list((input("skills").lower().split(" "))),
                        'marks': {
                                    'maths':int(input("enter maths marks ")),
                                    'physics':int(input("enter physics marks")),
                                    'biology':int(input("enter biology marks")),
                                    'english':int(input("enter english marks")),
                                    'social':int(input("enter social marks")),
                                    'telugu':int(input("enter telugu marks")),
                                    'hindi':int(input("enter hingi marks"))
                                    },

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
                            'id': id2,
                                'name': input("name"),
                                'email':input("email"),
                                'subjects':list((input("skills").lower().split(" "))),
                                'marks': {
                                    'maths':int(input("enter maths marks ")),
                                    'physics':int(input("enter physics marks")),
                                    'biology':int(input("enter biology marks")),
                                    'english':int(input("enter english marks")),
                                    'social':int(input("enter social marks")),
                                    'telugu':int(input("enter telugu marks")),
                                    'hindi':int(input("enter hingi marks"))
                                },
                                'attandence':int(input("enter the attandence percentage")),
                                'skills': set(input("enter the skills ").lower().split(" ")),
                                'status':input("enter the acc status(active/inactive)").lower(),
                                'performance':"pass"
                                                        
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
        s=s.union(d[i]['skills'])

    print("the unique skills are :")
    print(s)

def stats():
    avg=0
    sum=0
    avg1=0
    for i in d:
        print(d[i]['name'],
              d[i]['id'],
              ['marks'])
        for j in d[i]['marks']:
            sum=d[i]['marks'][j]+sum
            if d[i]['marks'][j]<35:
                d[i]['performance']='FAIL'
        avg=sum/len(d[i]['marks'])
        avg1=avg1+sum         
        print(f'''
=======================================
Student Statistics
=======================================
      marks:\n {d[i]['marks'].items()} \n
      avg student marks : {avg} \n
      status : {d[i]['status'].values()}\n
      Result : {d[i]['performance']}    
    ''')
    avg1=avg1/len(d)
    print(f'total sutents avg : {avg1}')

def updates():
    id=int(input("ENTER THE ID OF THE STUDENT TO BE EXECUTED : "))
    id2=check(id)
    if id2== True:
        key=input("Enter category to change : ")
        if key in d[id]:
            data=input("enter the data here")
            d[id].update({key:data})
    else:
        print("you entered wrong id")

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
        case "4":
            updates()
        case "5":
            delete() 
        case '6':
            stats()
        case "7":
            unique()
        case '8':
            break
        case _:  
            print("wrong input")

        