def expence(n):
    if n=="1":
        limit2=10000
        exp_name="Hotel"
    elif n=="2":
        limit2=50000
        exp_name="flights"
    elif n=="3":
        limit2=5000
        exp_name="transportation"
    elif n=="4":
        limit2=2000
        exp_name="meals"
    elif n=="5":
        limit2=2000
        exp_name="office supplies"
    elif n=="6":
        limit2=1000
        exp_name="internet/mobile expences"
    elif n=="7":
        limit2=15000
        exp_name="training/conferences"
    return exp_name,limit2

report=input(" is it pre aproved by manager?:(yes/no) ")
spent=int(input("ENTER THE SPENT AMOUNT"))
limit=int(input("Enter the max limit aproved by the manager"))
choice=int(input('''
                     1)Hotel
                     2)flights
                     3)transpotation
                     4)meals
                     5)office supplies
                     6)mobile expence
                     7)training conference
                     '''))
exp_name,lim2=expence(choice)
Day=input("Enter the day of expense: ")
r=input("Do have receipt?:(yes/no) ")
pr=input("Do you have a promotional code? (yes/no): ").lower()
if pr=="yes":
    promo_code=input("Enter the promotional code: ")
    if promo_code=="DISCOUNT10":
        discount_rate=0.10
    elif promo_code=="DISCOUNT20":
        discount_rate=0.20
    elif promo_code=="DISCOUNT30":
        discount_rate=0.30
    else:
        print("Invalid promotional code")
        discount_rate=0
else:
    print("no promotional code")
    discount_rate=0
eid=int(input("Enter your eployee id : "))
name=input("Enter the name of the emplyee : ")
dept=int(input("enter the dept no"))
limit=int(input("Enter the pre aproved expence amount: "))
eligibility=min(limit,spent,lim2)
def submit():
    if report=="yes":
        discount_amount = eligibility * discount_rate
        final_price = eligibility - discount_amount
        if r=="yes":
            if (spent<=limit and spent<=lim2):
                print("Your expense is within the limit for pre-approved expenses. Reimbursement will be processed.")
            elif spent>limit and spent>lim2:
                print(f'''You have exceeded the limit for {exp_name} expenses. +
            Reimbursement will be processed for the maximum limit of {eligibility}.
            contact your manager for further assistance.''')
            elif spent>limit and spent<=lim2:
                print(f'''You have exceeded the limit for pre-approved expenses.
            Reimbursement will be processed for the maximum limit of {eligibility}.
            contact your manager for further assistance.''')
            else:
                print(f'''Your expense is within the limit for pre-approved expenses. 
            Reimbursement will be processed for the amount of {spent}. because its
            not with in the limit of {lim2} for {exp_name} expenses.''')
        elif r=="no":
            if spent<=limit and spent<=lim2:
                print(f'''Your expense is within the limit for pre-approved expenses. 
            but do not have a receipt.
            Reimbursement will not be processed for the amount of {spent}.''')
            elif spent>limit and spent>lim2: 
                print(f'''You have exceeded the limit for {exp_name} expenses. 
            Reimbursement will be processed for the maximum limit of {eligibility}.
            contact your manager for further assistance.''')
            elif spent>limit and spent<=lim2:
                print(f'''You have exceeded the limit for pre-approved expenses.
            Reimbursement will be processed for the maximum limit of {eligibility}.
            contact your manager for further assistance.''')
            else:
                print(f'''Your expense is within the limit for pre-approved expenses. 
            but do not have a receipt. 
            Reimbursement will not be processed for the amount of {spent}.''')
    else:
        print("Your expense is not pre-approved by the manager. Reimbursement will not be processed directly .")
    job=input("enter your job title:  ")
    if eid!="":
        print("You are eligible to submit the expense report for reimbursement. Please seek approval from your manager before submitting.")
        if spent<=200:
            print("refund is not possible as the amount is less than 200")
        else:
            print("do you want to submit the expense report for reimbursement? (yes/no)")
            submit=input()
            if submit=="yes":
                print("Expense report submitted for reimbursement. You will be notified once the reimbursement is processed.")
                proof=input("do you have proof of expense? (yes/no) ")
                if proof=="yes":
                    eligibility,discount_amount,final_price=refund(lim2,spent,discount_rate)
                    display(name, eid, dept, exp_name, spent, report, promo_code, discount_amount, final_price)
                else:
                    print("Expense report not submitted. so rejected")




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
        case 1:
            submit()
        case 2:
            view()
        case 3:
            search()
        case 4:
            summary()
        case 5:
            rejected()
        case 6:
            totalexp()
        case 7:
            break
        case _:  
            print("wrong input")

