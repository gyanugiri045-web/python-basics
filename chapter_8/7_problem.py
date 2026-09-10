# #### using a enter controlled loop 
n=int(input("Enter a number:"))
i=100

while (i<=10):
    print(i)
    i+=1



#### using a exit controlled loop 
while True:
    number=int(input("Enter a number:"))
    print("You entered a number")
    choice=input("Do you want to continue? (yes/no):")

    if choice == "no":
        break
 

#### print a even number from 1 to 10

for i in range(1, 11):

    if i % 2 != 0:
        continue
    print(f"{i} is a even number")

    if i == 6:
        continue
    print("it is prime number is not 3")



n=int(input("Enter a number:"))

for i in range(2, n):
    if(n%i) == 0:
        print("Number is not prime.")
        break

    else:
        print("Number is prime.")