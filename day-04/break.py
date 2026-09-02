for number in range(1, 11):
    if number == 5:
        break
    print(number)

print(" continued ")

while True:
    command = input("Enter command: continue or quit: ").lower()
    if command == "quit":
        break
    print("You entered:", command)
