import json
def addv(ID):
    with open ("day-09/student_app/student.json","r") as file2:
            data=json.load(file2)
    for i in data:
        if i["uid"]==ID:
            return True
    else:
        return False