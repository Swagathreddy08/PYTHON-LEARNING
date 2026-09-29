lib=[{"bname":"history","bid":"001","status":"Active" }]
id=['001','002']
def option():
    choice=0
    while True:
                 print(''' 1) Add New books to library 
                2)Search/view availability
                3)borrow ''')
             
                 choice=input("enter your choice")
                 match choice:
                     case '1':
                           add()
                     case '2':
                           serach()
                     case '3':
                           borrow()
def login(cid):
    if cid in id:
        return True
def create():
    cid=input("enter your id")
    if cid not in id:
        id.append(cid)
        return cid
    else:
         print("give correct id ")
         return create()
def check(bid):
    i=0
    if len(lib)==0:
         return True
    while i < len(lib):
        if bid==lib[i]["bid"]:
            return False
        i+=1
    else:
         return True 

def scheck(bname):
     q=j=0
     b=False
     for i in lib:
          if bname == i["bname"]:
            if i["status"]=="Active":
                 j+=1
                 b=True
            q+=1
     return j,b,q

def bcheck(bname):
    b= False
    for i in lib:
        if bname == i["bname"]and i["status"]=="Active":
            b=True
            return b,i
        else:
             pass
    return b,0
          
def add():
    bid=input("enter the book id")
    
    if check(bid):
            bname=input("enter book name : ")
            book={
                 "bname":bname,
                 "bid":bid,
                 "status":'Active',

            }
            lib.append(book)
    else:
             pass
    

def serach():
    bname=input("enter the book name")
    available,check,quantity =scheck(bname)
    if check==True:
          print(f" the book {bname} is found and the library has {quantity} books but {available} are available ")
    else:
         print("the book is not available ")

def borrow():
    bname=input("enter the book name")
    check,details=bcheck(bname)
    if check==True:
         borrow_date=input("enter borrowed date for the book")
         return_date=input("enter return date for the book")
         print("Note for every 1 day dealay 5 rs fine and cost for the lend duration is 50 rs")
         for i in lib:
              if details["bid"]==i["bid"]:
                   i.update({"status":"borrowed","borroed_date":borrow_date,"return_date":return_date})
    else:
         print("book is not available")
         


print("welcome to swwag library")
cid=input("enter your id")
if login(cid):
        #option to choose from
        option()
             
else:
        #repete the login again
        print("you dont have a membership to the library")
        c=input("Do you want to take membership (Yes/No): ").lower()
        if c == 'yes':
            t=create()
            if login(t):
                 option()
            

        