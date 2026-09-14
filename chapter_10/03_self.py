class Employee:
    language="py"       #This is class attrubute
    salary=120000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")


reyan=Employee()
reyan.language="java"     #This is an instance attribute
reyan.getInfo()