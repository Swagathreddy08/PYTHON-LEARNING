def repo():
    report=input(" is it pre aproved by manager?:(True/False) ").title()
    if report in ['True','False']:
        return report
    else:
        print("Please follow the instructions properly")
        return repo()

def spent():
    sp=int(input("ENTER THE SPENT AMOUNT"))
    if sp>0:
        return sp
    else:
        print("enter a correct ammount")
        return spent()

def dep():
    dp=int(input("enter the dept no"))
    if dp in [10,20,30,40,50]:
        return dp
    else:
        print("enter the correct dept no")
        return dep()