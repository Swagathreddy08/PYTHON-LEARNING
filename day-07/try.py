d={101:{'id': 101,
                            'name': 'ravi',
                            'email':'ravi@gmail.com',
                            'marks': {
                                        'maths':10,
                                        'physics':30,
                                        'biology':90,
                                        'english':36,
                                        'social':90,
                                        'telugu':94,
                                        'hindi':73
                                        },

                            'attandance': 85,
                            'skills': set('sql'),
                            'status':'active',   
},
'102':{'id': 102,
                            'name': 'ravi',
                            'email':'ravi@gmail.com',
                            'marks': {
                                        'maths':10,
                                        'physics':30,
                                        'biology':90,
                                        'english':36,
                                        'social':90,
                                        'telugu':94,
                                        'hindi':73
                                        },

                            'attandance': 85,
                            'skills': set('sql'),
                            'status':'active',   
}
        }
b=False
def check(id2):
     global b
     if id2 not in d:
          1

          b=True
          return id2
     else:
          
          b=False
          print(" Id is already present in the dictionary ")
          id2=int(input("enter the correct id "))
          return check(id2)


        
def check2(id2):
        if id2 in d:
            return True
        else:
            print("the id is not available")

            return False
def att():
    atd=input("enter the attandence percntage")
    if atd.isnumeric() :
        atd=int(atd)
        if atd in range(0,101):
            return atd
        else:
            print("enter the correct percentage")
            return att()
    else:
         print("enter only numbers")
         return att()
def mark():
    mar=input("Enter the marks in numbers")
    if mar.isnumeric():
        mar=int(mar)
        if mar >= 0: 
            if mar in range(0,101):
                return mar
            else:
                print("enter the correct marks")
                return mark()
        else:
             print("enter a positive integer")
             return mark()
    else:
        print("enter only numbers")
        return mark()
def add():
        print("do you want a student detalis" )
        q=int(input("How many students ?"))
        id2=int(input("enter the input"))
        for i in range(q):              
                id2=check(id2)
                if b:
                    d[id2]={
                        'id': id2,
                            'name': input("name"),
                            'email':input("email"),
                            'marks': {
                                        'maths':mark(),
                                        'physics':mark(),
                                        'biology':mark(),
                                        'english':mark(),
                                        'social':mark(),
                                        'telugu':mark(),
                                        'hindi':mark()
                                        },

                            'attandance': att(),
                            'skills': set(input("enter the skills ").lower().split(" ")),
                            'status':'active',
                            }

        

def view():
        print("choose one option")
        op=input('''1. Active Students 
        2.Inactive Students
        3.all students''')
        match op:
            case '1':
                print("ACTIVE STUDENTS : \n")
                for i in d:
                    if d[i]['status']=='active':
                        print(d[i])
            case '2':    
                print("Inactive students")
                for i in d:
                            if d[i]['status']=='inactive':
                                print(d[i])
            case '3':
                  print("all the students")
                  print(d)
            case _:
                  print("wrong input")
def find():
        id2 = int(input("enter id of student"))
        id=check2(id2)
        if id == True:
            print(d[id2])
        else:
            print("User not found")
def delete():
        id2 = int(input("enter id of student"))
        id=check2(id2)
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
        s=0
        avg1=0
        for i in d:
            print(d[i]['name'],
                d[i]['id'],
                d[i]['marks'])
            d[i]['performance']='pass'
            for j in d[i]['marks']:
                s=d[i]['marks'][j]+s
                if d[i]['marks'][j]<35:
                    d[i]['performance']='fail'
                
            avg=s/len(d[i]['marks'])
            
            avg1=avg1+s
            s=0        
            print(f'''
    =======================================
    Student Statistics
    =======================================
        marks:\n {d[i]['marks'].items()} \n
        avg student marks : {avg} \n
        status : {d[i]['status']}\n
        Result : {d[i]['performance']}    
        ''')
        if len(d) != 0:
            avg1=avg1/len(d)
        print(f'total sutents avg : {avg1}')

def updates():
        id=int(input("ENTER THE ID OF THE STUDENT TO BE EXECUTED : "))
        id2=check2(id)
        if id2== True:
            key=input("Enter category to change : ").lower().strip().rstrip()
            if key in d[id]:
                match key:
                    case 'marks':
                        key2=input("enter the subject you want to change")
                        if key2 in d[id]['marks']:
                            data=int(input("enterthe marks"))
                            if data in range(0,101):
                                d[id][key][key2]=data
                            else:
                                print("correct marks you morron ")
                        
                    case 'skills':
                        sc=input('''
                            1. Adding a skill
                            2. deleting a skill''')
                        match sc:
                            case '1':
                                d[id][key]=d[id][key].union( set(input("enter the skills ").lower().split(" ")) )
                            case '2':
                                data= input('enter the skill u want to be removed')
                                if data in d[id][key]:
                                    d[id][key].remove(data)
                                else:
                                     print("skill not present")
                    case 'name':
                        d[id][key]=input("enter the change of name")
                    case 'email':
                        d[id][key]=input("enter the change of email")
                    case 'attandence':
                        d[id][key]=att()
                    case 'status':
                        print('''1.inactive
                        2.active''')
                        test=input()
                        match test:
                            case '1':
                                d[id][key]='inactive'
                            case '2':
                                d[id][key]='active'    
                            case _:
                                print("wrong input")

            else:
                    print("the given key does not exist")

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

            