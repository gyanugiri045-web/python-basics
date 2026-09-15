from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo=trainNo

    def book(self,fro, to ):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to} ")

    def getstate(self):
        print(f"Train no {self.trainNo} is running on time")

    def getfare(self, fro, to ):
        print(f"Ticket are in train no: {self.trainNo} from {fro} to {to} is {randint(222,5555)}")

    
t= Train(12333)
t.book("ktm", "npj")
t.getstate()
t.getfare("ktm", "npj")