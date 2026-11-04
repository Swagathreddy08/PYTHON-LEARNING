def indi_serial(todo)->dict:
    return{
        "id":str(todo["_id"]),
        "name" : todo["name"],
        "branch" : todo["branch"],
        "status" : todo["status"],
        "age" : todo["age"]
    }
def list_of_indi_serial(todos)->list:
    return[indi_serial(todo) for todo in todos]
