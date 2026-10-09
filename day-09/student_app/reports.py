from data import student

def allstd():
    for i in student:
        print(f"{i}\n")

def rep():
    for i in student:
        if any(mark < 35 for mark in i["marks"].values()):
            i["Status"]="Fail"
        else:
            i["Status"]="Pass"
    for i in student:
        print(f"{i["uid"]} : {i["Status"]}")