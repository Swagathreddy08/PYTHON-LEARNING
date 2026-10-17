def madmin():
    while True:
        ch=input('''
1)New Doctor
2)New Patients
3)Leave Aproval
4)All THE DETAILS
5)LOG OUT 
''')
        match ch:
            case "1":
                print("new doc")
            case "2":
                print("new patient")
            case "3":
                print("leave request")
            case "4":
                print("ALL details")
            case "5":
                break
            case _:
                print("Wrong Input")

def mdoc():
    while True:
        ch=input('''
1)View appointments
2)leave
3)LOG OUT''')
        match ch:
            case "1":
                print("view appointments")
            case "2":
                print("Leave request")
            case "3":
                break
            case _ :
                print("wrong input")

def mpat():
    while True:
        ch=input('''
1)Book Appointment
2)Medical History
3)Appointment 
4)Logout
''')