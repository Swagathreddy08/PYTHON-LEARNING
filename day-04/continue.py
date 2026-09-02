for number in range(1, 11):
    if number == 5:
        continue
    print(number)

for number in range(1, 11):
    if number % 2 == 0:
        continue
    print(f"Odd number: {number}")