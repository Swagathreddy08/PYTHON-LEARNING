count = int(input("Enter a number to countdown from: "))
if count < 0:
    print("Please enter a non-negative integer.")
elif count == 0:
    print("Countdown: 0")
else:
    while count >= 0:
        print(count)
        if count == 0:
            print("COUNTDOWN COMPLETE!")
        count = count - 1
