class Employee:
    language = "python"
    salary = 180000

    def __init__(self, name, salary, language):
        self.name = name
        self.language = language
        self.salary = salary
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    def greet(self):
        print("Good morning")


reyan = Employee("reyan", 1300000, "java")
print(reyan.name, reyan.salary)

ram = Employee("ram", 900000, "python")