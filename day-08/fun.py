students = [   {"id": 1, "name": "Asha", "marks": [80, 90, 85],'skills':set(    )},
                {"id": 2, "name": "Ravi", "marks": [70, 75, 80]}]
def find_student(student_id):    
    for student in students:        
        if student["id"] == student_id:            
            return student    
    return None 
def average():
    sum=0

    for i in students:
        for j in i["marks"]:
            sum=j+sum
        avg=sum/(len(i["marks"]))
        sum=0
        print(f' student {i['id']} average is {avg}')

print(find_student(2))
average()