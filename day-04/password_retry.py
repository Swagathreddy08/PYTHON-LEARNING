correct_password = "python123"
password = input("Enter password: ")
while password != correct_password:
    password = input("Enter password: ")
    c+=1
    if c == 3:
        print("Too many incorrect attempts. Access denied.")
        break
else:
    print("Access granted!")