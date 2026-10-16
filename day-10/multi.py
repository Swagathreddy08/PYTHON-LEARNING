class Printable:
    def describe(self):
        return "printable"
class Exportable:
    def export(self):
        return "exported"
class Report(Printable, Exportable):
    pass
report = Report()
print(report)