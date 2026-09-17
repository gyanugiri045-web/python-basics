class ATM:
    def __init__(self,pin=123,balance=12000):
        self.pin=pin
        self.balance=balance
   
    def authenticate(self):
        entered_pin = int(input("Enter your 4-digit pin: "))
        if entered_pin != self.pin:
            print("Incorrect pin")
            return False
        return True
    
    def check_balance(self):
        print(f"If your balance is {self.balance}")

    def withdraw(self):
        amount=float(input("Enter a amout you want to withdraw:"))
        if amount<=0:
            print("Invalid amount!")

        elif(amount>self.balance):
            print("Insufficient balance!")

        else:
            self.balance-= amount
            print("Successfully withdrawn")
            print(f"Remaining balance is {self.balance}")

    def deposite(self):
        amount = float(input("Enter amount to deposite:"))
        if amount > 0:
            self.balance += amount
            print("successfully deposited!!")
            print(f"New balance is: {self.balance}")
        else:
            print("Invalid amount!!!")

    def run(self):
        if not self.authenticate():
            return
        
        while True:
            print("1. chack balance")
            print("2. deposite")
            print("3. withdrawn")
            print("4. exit")

            choice = input("Enter your choice (1-4):")

            if choice == "1":
                self.check_balance()

            elif choice == "2":
                self.deposite()

            elif choice == "3":
                self.withdraw()

            elif choice == "4":
                print("Thank you for visiting!!")
                break
            else:
                print("Invalid choice!!")

my_ATM = ATM()
my_ATM.run()