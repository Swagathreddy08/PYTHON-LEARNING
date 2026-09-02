c=1
sec=12345
i=int(input("Enter the secret number you think is correct: "))
while i!=sec:
    print("Incorrect secret number. Try again.")
    i=int(input("Enter the secret number you think is correct: "))
    c+=1
print(f"You guessed the correct secret number {sec} in {c} attempts.")