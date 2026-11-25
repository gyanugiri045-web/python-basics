 # It allows one class to get or reuse the properties and method of another class .



class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def speak(self):  
        print(f"{self.name} says bow bow!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")


dog = Dog("dazy")
cat = Cat("biralo")
  
dog.speak()      
cat.speak()    

