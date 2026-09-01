age = 20
if age >= 18:
    print('You are an adult')

age = int(input('Enter your age: '))
if age >= 18:
    print('Adult')
else:
    print('Minor')

score = int(input('Enter score: '))
if score >= 90:
    print('Excellent')
elif score >= 75:
    print('Good')
elif score >= 50:
    print('Pass')
else:
    print('Needs improvement')
