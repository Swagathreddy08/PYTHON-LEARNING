age=input("ENTER YOUR AGE")
try:
    age=int(age)
except ValueError:
    print("enter a whole number")
else:
    print (age+1,"next year age will be")
finally:
    print(age)
