d={
        }


def check(id2):
        if id2 in d:
            id2=int(input("Enter correct id which is not in data base: "))
            return check(id2)
        else:
            return True
def check2(id2):
        if id2 in d:
            return True
        else:
            print("the id is not available")
            return False
        
def add():
        print("do you want a student detalis" )
        q=int(input("How many students ?"))
        for i in range(q):
                id2 = int(input("enter id of student"))
                
                if check(id2):
                    d[id2]={
                        'id': id2,
                            'name': input("name"),
                            'email':input("email"),
                            'marks': {
                                        'maths':int(input("enter maths marks ")),
                                        'physics':int(input("enter physics marks")),
                                        'biology':int(input("enter biology marks")),
                                        'english':int(input("enter english marks")),
                                        'social':int(input("enter social marks")),
                                        'telugu':int(input("enter telugu marks")),
                                        'hindi':int(input("enter hingi marks"))
                                        },

                            'attandance': att if (att := int(input("Enter attandance percentage: "))) in range(0, 101) else main()  ,
                            'skills': set(input("enter the skills ").lower().split(" ")),
                            'status':'active',
                            'performance':'pass'
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
            
            for j in d[i]['marks']:
                s=d[i]['marks'][j]+s
                if d[i]['marks'][j]<35:
                    d[i]['performance']='FAIL'
                
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
                                    d[id][key].pop(data)
                                else:
                                     print("skill not present")
                    case 'name':
                        d[id][key]=input("enter the change of name")
                    case 'email':
                        d[id][key]=input("enter the change of email")
                    case 'attandence':
                        att=int(input("enter the attandence percentage"))
                        if att in range (0,101):
                            d[id][key]=att
                        else:
                             print("give correct attandence")
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

def main(): 
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

                