print("******************************************")
print("CLI ATM Simulator")
print("******************************************")
pin=1234
bal=1000
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")
n = int(input("Enter your choice: "))
while True:
    if n == 1:
        p1=int(input("Enter your PIN: "))
        if p1==pin:
            print(f"Your balance is: RS{bal}")
            continue
        else:
            print("Incorrect PIN. Access denied.")
    
    elif n == 2:
        p2=int(input("Enter your PIN: "))
        if p2==pin:
            dep=int(input("Enter amount to deposit: "))
            bal+=dep
            print(f"Deposit successful. New balance is: RS{bal}")
        else:
            print("Incorrect PIN. Access denied.")

    elif n == 3:
        p3=int(input("Enter your PIN: "))
        if p3==pin:
            wit = int(input("Enter amount to withdraw: "))
            if wit <= bal:
                bal -= wit
                print(f"Withdrawal successful. New balance is: RS{bal}")
            else:
                print("Insufficient funds.")
        else:
            print("Incorrect PIN. Access denied.")
    elif n == 4:
        print("Thank you for using the CLI ATM Simulator. Goodbye!")
        break;
    elif n not in range(1,5):
        print("Invalid choice. Please try again.")  
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    n = int(input("Enter your choice: "))


