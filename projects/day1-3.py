print("******************************************")
print("EMPLOYEE EXPENSE MANAGEMENT SYSTEM")
print("******************************************")
print("1. Client meetings")
print("2. business travel")
print("3. food ")
print("4. taxis")
print("5. hotels")
print("6. office supplies")
print("7. conferences")
n = int(input("Enter your choice: "))
r=input("Do have receipt?:(yes/no) ")
report=input(" is it pre aproved by manager?:(yes/no) ")
if report=="yes":
    limit=int(input("Enter the pre aproved expence amount: "))
    spent=int(input("Enter the amount spent: "))
    if spent>limit:
        print("You have exceeded the pre-approved expense limit reembursement will be processed.")
    else:
        print("Your expense is within the pre-approved limit. do you want to submit the expense report for reimbursement? (yes/no)")
        submit=input()
        if submit=="yes":
            print("Expense report submitted for reimbursement. You will be notified once the reimbursement is processed.")
        else:
            print("Expense report not submitted. so rejected")
elif report=="no":
    print("Your expense report is not pre-approved by the manager. Please seek approval before submitting for reimbursement.")
    job=input("enter your job title:  ")
    if job in ["manager","developer","tester","designer","sales"]:
        print("You are eligible to submit the expense report for reimbursement. Please seek approval from your manager before submitting.")
        if spent<=200:
            print("refund is not possible as the amount is less than 200")
        else:
            print("do you want to submit the expense report for reimbursement? (yes/no)")
            submit=input()
            if submit=="yes":
                print("Expense report submitted for reimbursement. You will be notified once the reimbursement is processed.")
            else:
                print("Expense report not submitted. so rejected")

        