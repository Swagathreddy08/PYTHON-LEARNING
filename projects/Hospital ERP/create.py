from valid import *
class hospital:
    def __init__(self):
        self.hname = "APPOLO 24/7"
class pcreate(hospital):
    def __init__(self, patient_id):
        super().__init__()
        self.psw = input("Enter the Password ")
        self.name = input("NAME : ")
        self.ref = input("Reference : ")
        self.num = input("Phone No : ")
        self.add = input("Address : ")
        self.id = patient_id

class dcreate(hospital):
    def __init__(self, doctorid):
        super().__init__()
        self.psw = input("Enter the Password ")
        self.name = input("Name : ")
        self.branch = input("Branch : ")
        self.num = input("Phone No : ")
        self.add = input("Address : ")
        self.id = doctorid

class acreate(hospital):
    def __init__(self, Admin_id):
            super().__init__()
            self.psw = input("Enter the Password ")
            self.name = input("Name : ")
            self.branch = input("Branch : ")
            self.num = input("Phone No : ")
            self.add = input("Address : ")
            self.id = Admin_id
        

