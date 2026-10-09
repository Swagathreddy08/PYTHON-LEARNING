from data import *
def view():
    for i in lists:
        print(i)

def search():
    b1=False 
    id=input("Enter the Id to be searched")
    for i in lists[1:]:
        if i[0] == id:
            print(i)
            break
    else:
        print("EMPLOYEE NOT FOUND") 

def rejected():
    for i in reject:
        print(i)

def summary():
    print("EXPENSE SUMMARY")
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