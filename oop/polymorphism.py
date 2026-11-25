
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return " dazzy is my dog and she speak bow bow !"

class Cat(Animal):
    def speak(self):
        return " ramri is my cat and she speak Meow meow!"

animals = Dog(), Cat()

for animal in animals:
    print(animal.speak())