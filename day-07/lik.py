posts={'001':{'post_id':'001',
       'post_name':'trial',
       'user_id':'001',
       'user_name':'creator_001',
       'like':10000,
       'share':100,
       'discription':"the discription",
        }}
users={'001':{
       'folowers':10000,
       'user_id':'001',
       'user_name':'creator_001',
       
}}
db={'001':{
    'user_name':'creator_001',
    'password':'tiger'
}}
b=False

#post check
def check2(id2):
     global b
     if id2 not in posts:
          b=True
          return id2
     else:
          b=False
          print(" Id is already present in the dictionary ")
          id2=input("enter the correct id ")
          return check2(id2)

# user check
def check3(id2):
        if id2 in users:
            return True
        else:
            print("the id is not available")

            return False
#db check
def check(uname,psw):
    for i in db:
        if uname == db[i]['user_name']:

             if psw == db[i]['password']:
                  return True
             else:
                  psw=input("enter correct password : ")
                  return check(uname,psw)
    else:
        uname=input("enter correct user name")
        psw=input("enter correct password : ")
        return check(uname,psw)

def ret(uname):
     for i in users:
          if users[i]['user_id']==uname:
               return i
def post(uname):
     id2=input("enter the post_id")
     id2=check2(id2)
     if b:
        posts[id2]={
        'post_id': id2,
        'post_name':input("enter the post name"),
        'user_id':ret(uname),
        'user_name':uname,
        'like': 0,
        'share': 0,
        'discription':input("enter the discription"),
        }

def search():
    id2 = input("enter id of user")
    id=check3(id2)
    if id == True:
        print(users[id2])
        
    else:
        print("User not found") 

def delete():
        id2 = input("enter id of user")
        id=check3(id2)
        j=0
        a=[]
        if id == True:
            del users[id2]
            for i in posts:
                if posts[i]['user_id']==id2:
                    a.append(i)
            while j < len(a):
                 del posts[a[j]]
                 j+=1           
            a.clear()
            if id2 in db:
                del db[id2]
        else:
            print("user is a ghost")  

def follow():
    id2 = input("enter id of user whome you want to follow")
    id3 = input("enter your id")
    id=check3(id2)
    i=check3(id3)
    if i and id == True:
         if id2!=id3:        
            users[id2]['folowers']+=1
        
        
b=input("Do you already have a media account (yes/no)").lower().rstrip().strip()
if b == 'yes':
    uname=input("enter your user name")
    psw=input("enter the password")
    if check(uname,psw):
        while True:
            c=input('''1) post
        2) delete
        3) search
        4) follow
        5) exit''')
            match c:
                            case '1':
                                post(uname)
                            case '2':
                                delete()
                            case '3':
                                search()
                            case '4':
                                follow()
                            case '5':
                                break
                            case _:
                                print("wrong input")
elif b == 'no':
    b1=("do you want to create a account (yes/no)").lower().strip().rstrip()
    if b1 == 'yes':
        usid=input("enter the user id")
        uname=input("enter your user name")
        psw=input("enter the password")
        db[usid]={}
        db[usid]['user_name']=uname
        db[usid]['password']=psw
        users[usid]={
       'folowers':0,
       'user_id':usid,
       'user_name':uname}
        
