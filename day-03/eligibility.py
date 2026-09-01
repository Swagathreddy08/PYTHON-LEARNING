age = int(input("Enter your age: "))
doc = input("Do you have a doctor's note? (yes/no): ")
score = int(input("Enter your score: "))
if(age >= 18 and doc.lower() == "yes" and score >= 50):
    print("You are eligible.")
elif(age >= 18 and doc.lower() == "no" and score <= 50):
    print("You are not eligible. only age isw accepted")
elif(age >= 18 and doc.lower() == "no" and score >= 50):
    print("You are not eligible. document is not accepted")
elif(age >= 18 and doc.lower() == "yes" and score <= 50):
    print("You are not eligible. ")
elif(age < 18 and doc.lower() == "yes" and score <= 50):
    print("You are not eligible.")
elif(age < 18 and doc.lower() == "no" and score >= 50):
    print("You are not eligible.")
elif(age < 18 and doc.lower() == "yes" and score >= 50):
    print("You are not eligible.")
else:
    print("You are not eligible.")
