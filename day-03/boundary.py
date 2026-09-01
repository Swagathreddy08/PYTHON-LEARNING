n=int(input("Enter a number: "))
age=int(input("Enter your age: "))
if n>0:
    print("The number is positive.")
elif n<0:
    print("The number is negative.")
else:
    print("The number is zero.")

print("classification based on age")
if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")