
class Claim:
    def __init__(self, employee_id, amount):
        self.employee_id = employee_id
        self.amount = amount

    def summary(self):
        print(f"{self.employee_id}: {self.amount}")


class TravelClaim(Claim):
    def __init__(self, employee_id, amount, destination):
        super().__init__(employee_id, amount)
        self.destination = destination

    def display(self):
        print(f"{self.employee_id}: {self.amount} : {self.destination}")


c1 = Claim("001", "10000")
c1.summary()

c2 = TravelClaim(c1.employee_id, c1.amount, "hyd")
c2.display()
