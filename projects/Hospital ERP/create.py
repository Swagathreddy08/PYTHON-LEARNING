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
        self.id = patient_id
