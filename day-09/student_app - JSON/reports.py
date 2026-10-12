import json
with open ("day-09/student_app/student.json","r") as file2:
        data=json.load(file2)
def allstd():
    for i in data:
        print(i)
        

def rep():
    for i in data:
        if any(mark < 35 for mark in i["marks"].values()):
            i["Status"]="Fail"
        else:
            i["Status"]="Pass"
    for i in data:
        print(f"{i["uid"]} : {i["Status"]}")