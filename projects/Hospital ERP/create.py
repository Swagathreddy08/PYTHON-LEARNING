from valid import *
class hospital:
    def __init__(self):
        self.hname="APPOLO 24/7"
class pcreate(hospital):
        super().__init__()
        def __init__(self,id):
                self.psw=input("Enter the Password ")
                self.name=input("NAME : ")
                self.ref=input("Reference : ")
                self.id=id
            

