lists=[["EMPLOYE ID","NAME","EXPENCE CATEGORY","Climed Amount","Eligible AMT","STATUS"]]
reject=[["EMPLOYE ID","NAME","EXPENCE CATEGORY","Climed amount","Reason"]]
def expence(n):
    match n:
        case "1":
            limit2=10000
            exp_name="Hotel"
            return exp_name,limit2
        case "2":
            limit2=50000
            exp_name="flights"
            return exp_name,limit2
        case "3":
            limit2=5000
            exp_name="transportation"
            return exp_name,limit2
        case "4":
            limit2=2000
            exp_name="meals"
            return exp_name,limit2
        case "5":
            limit2=2000
            exp_name="office supplies"
            return exp_name,limit2
        case "6":
            limit2=1000
            exp_name="internet/mobile expences"
            return exp_name,limit2
        case "7":
            limit2=15000
            exp_name="training/conferences"
            return exp_name,limit2
        case _:
            print(" WRONG INPUT ")
            n=input("enter the choice")
            exp_name,limit2=expence(n)
            return exp_name,limit2


def submit():
    report=input(" is it pre aproved by manager?:(True/False) ").lower().title
    if report not in ['True','False']:
        print("Please follow the instructions properly")
        report=input(" is it pre aproved by manager?:(yes/no) ").lower().title()
    spent=int(input("ENTER THE SPENT AMOUNT"))
    if spent<=0:
        print("enter a correct ammount")
        spent=int(input("Enter the spent amount correctly this time"))
    limit=int(input("Enter the max limit aproved by the manager"))
    choice=input('''
                     1)Hotel
                     2)flights
                     3)transpotation
                     4)meals
                     5)office supplies
                     6)mobile expence
                     7)training conference
                     ''')
    exp_name,lim2=expence(choice)
    Day=input("Enter the day of expense: ")
    r=input("Do have receipt?:(True/False) ").lower()
    
    pr=input("Do you have a promotional code? (yes/no): ").lower()
    if pr=="yes":
        promo_code=input("Enter the promotional code: ").upper()
        if promo_code=="DISCOUNT10":
            discount_rate=0.10
        elif promo_code=="DISCOUNT20":
            discount_rate=0.20
        elif promo_code=="DISCOUNT30":
            discount_rate= 0.30
        else:
            print("Invalid promotional code")
            discount_rate=0
    else:
        print("no promotional code")
        discount_rate=0
    eid=input("Enter your eployee id : ")
    name=input("Enter the name of the emplyee : ")
    dept=int(input("enter the dept no"))
    if dept not in [10,20,30,40,50]:
        print("enter the correct dept no")
        dept=int(input("enter the dept no"))
    eligibility=min(limit,spent,lim2)
    if report=="yes":
        discount_amount = eligibility * discount_rate
        final_price = eligibility - discount_amount
        if r:
            if (spent<=limit and spent<=lim2):
                print("Your expense is within the limit for pre-approved expenses. Reimbursement will be processed.")
                status="aproved"
                l=[eid,name,exp_name,spent,final_price,status]
                lists.append(l)
            elif spent>limit and spent>lim2:
                print(f'''You have exceeded the limit for {exp_name} expenses. +
            Reimbursement will be processed for the maximum limit of {eligibility}.
            contact your manager for further assistance.''')
                status='partially aproved'
                l=[eid,name,exp_name,spent,final_price,status]
                lists.append(l)
            elif spent>limit and spent<=lim2:
                print(f'''You have exceeded the limit for pre-approved expenses.
            Reimbursement will be processed for the maximum limit of {eligibility}.
            contact your manager for further assistance.''')
                status='partially aproved'
                l=[eid,name,exp_name,spent,final_price,status]
                lists.append(l)
            else:
                print(f'''Your expense is within the limit for pre-approved expenses. 
            Reimbursement will be processed for the amount of {spent}. because its
            not with in the limit of {lim2} for {exp_name} expenses.''')
                status="partially aproved"
                l=[eid,name,exp_name,spent,final_price,status]
                lists.append(l)
        elif r == False:
            reason="no proof of payment"
            status="rejected"
            l=[eid,name,exp_name,spent,0,status]
            l2=[eid,name,exp_name,spent,reason]
            lists.append(l)
            reject.append(l2)
    else:
        print("Your expense is not pre-approved by the manager. Reimbursement will not be processed directly .")
        reason="the expence is not pre aproved"
        status="rejected"
        l=[eid,name,exp_name,spent,0,status]
        l2=[eid,name,exp_name,spent,reason]
        lists.append(l)
        reject.append(l2)

def view():
    for i in lists:
        print(i)

def search():
    b1=False 
    id=int(input("Enter the Id to be searched"))
    for i in lists[1:]:
        if i[0] == id:
            b1=True
            print(i)
    if b1 == False:
        print("EMPLOYEE NOT FOUND") 

def rejected():
    for i in reject:
        print(i)

def summary():
    print("EXPENSE SUMMARY").center(30,"=")
    print("\n")
    app=par=re=cl=al=av=0
    for i in lists[1:]:
        if i[-1] == 'aproved':
            app+=1
            re+=i[-2]
        elif i[-1] == 'partially aproved':
            par+=1
            re+=i[-2]
        elif i[-1] != 'rejected':
            re+=i[-2]
        cl+=i[-3]
    if len(lists)-1>=1:  
        av=(cl/(len(lists)-1))
    print(f'''

Total Claims: {len(lists)-1}

Approved Claims: {app}
Partially Approved {par}
Rejected Claims: {len(reject)-1}

Total Amount Claimed: ₹{cl}
Total Amount Reimbursed: ₹{re}

Average Claim: ₹{av}''')


def totalexp():
    totalexpnce=0
    for i in lists[1:]:
        if i[-1] !='rejected':
            totalexpnce=i[-2]+totalexpnce
    print(f"Total reimbursement payable: {totalexpnce}")
    
print('''
========================================
     PRODUCTION INCIDENT ANALYZER
========================================

1. Submit
2. View
3. Search
4. Summary
5. Rejected 
6. Total Expence report
7. Exit''')
while True:
    choice=input("enter your chice ")
    match choice:
        case "1":
            submit()
        case "2":
            view()
        case "3":
            search()
        case "4":
            summary()
        case "5":
            rejected()
        case "6":
            totalexp()
        case "7":
            break
        case _:  
            print("wrong input")

