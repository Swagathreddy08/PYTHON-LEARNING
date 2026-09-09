expenses=[]
amt=[]
while True:
    print("this is a simple expense tracker app")
    print("1. Add expense")
    print("2. view expences")
    print("3. total expence")
    c=int(input("enter your chice"))
    if c==1:
        name=input("enter the expence name").strip()
        amount=int(input("enter the amount spent"))
        expenses.append(name)
        amt.append(amount)
    elif c==2:
        for expence,amount in zip(expenses,amt):
            print(expenses)
            print(amt)
    elif c==3:
        total=sum(amt)
        print(" the total count is",len(expenses))
        print("the total sum of expences is",total
              )
    else:
        print("invalid choice")
