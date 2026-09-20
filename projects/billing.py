def expence(n):
    if n=="1":
        limit2=10000
        expense_name="Hotel"
    elif n=="2":
        limit2=50000
        expense_name="flights"
    elif n=="3":
        limit2=5000
        expense_name="transportation"
    elif n=="4":
        limit2=2000
        expense_name="meals"
    elif n=="5":
        limit2=2000
        expense_name="office supplies"
    elif n=="6":
        limit2=1000
        expense_name="internet/mobile expences"
    elif n=="7":
        limit2=15000
        expense_name="training/conferences"
    return expense_name,limit2
def submit():
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

