from claim import *
from report import *

while True:
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

