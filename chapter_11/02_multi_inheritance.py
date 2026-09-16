class employee:
    company="IIT"
    name="default name"
    def show(self):
        print(f"The name of employee is {self.name} and company is {self.company}")

class coder:
    language="python"
    def printlanguages(self):
        print(f"out of all the language here is your languege: {self.language}")

    
class programmer(employee, coder):
    company="ITC fortage"
    def showlanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")        ### Inheritance class

a = employee()
b= programmer()

b.show()
b.printlanguages()
b.showlanguage()