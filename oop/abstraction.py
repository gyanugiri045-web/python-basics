
# Abstraction mean hiding unnecessary implementation details and showing only the important features to the user.

# def tea(person):
#     print("Boil water")
#     print("Add chapati")
#     print("Add milk and sugar")
#     print(f"put into cup for {person}")

# tea("Ram")
# tea("Sita")




class TeaMaker:
    def __init__(self):
        self.__steps = ["Boil water","Add chapati","Add milk and sugar"]

    def make (self, person):
        for step in self.__steps:
            print(step)
            print(step)
            print(f"Pour into cup for {person}")

maker = TeaMaker()
maker.make("Ram")
maker.make("Sita")
