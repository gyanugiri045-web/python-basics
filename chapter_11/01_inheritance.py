class employee:
    company="IIT"
    def show(self):
        print(f"The name of employee is {self.name} and salary is {self.salary}")
    
class programmer(employee):
    company="ITC fortage"
    def showlanguage(self):
        print(f"The name s {self.name} and henis good with {self.language} language")        ### inheritance class

a = employee()
b=programmer()

print(a.company, b.company)

