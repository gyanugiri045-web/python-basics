def atm():
    balance = 12000
    pin = 1234

    enter_pin = int(input("Enter a pin:"))
    if enter_pin != pin:
        print("Invalid pin!!!")
        return
    
    while True:
        print("\n--Select your choice--")
        print("1. check balance")
        print("2. cash withdraw")
        print("3. deposite")
        print("4. Exit")

        choice = int(input("Enter your choice (1-4):"))

        if choice == 1:
            print(f"Your balance is: {balance} ")

        elif choice == 2:
            amount = float(input("Enter amount to withdraw:"))
            if amount > balance:
                print("Insufficient amount!!")
            elif amount <= 0:
                print("Invalid amount!!")
            else:
                balance -= amount
                print("Succesfully cash withdraw!!")
                print(f"Remaining balance is: {balance}")
        elif choice == 3:
            amount = float(input("Enter a amount to deposite: "))
            if amount > 0:
                balance += amount
                print("Successfully deposited!!")
                print(f"Your new balance is: {balance}")
            else:
                print("Invalid amount!!")
            
        elif choice == 4:
            print("Thank you for visiting us !!")
            break
        else:
            print("Invalid choice!!")

atm()