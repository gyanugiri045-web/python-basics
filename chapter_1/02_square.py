
# find the square of the number 
a=int(input("Enter the number :"))

print("The square of the number is:", a**2) 
# or,
print("The square os the number is:", a*a)




###  by using function
def square():
    a=int(input("Enter a number:"))
    print("The square of the number is:", a*a)

square()


### by using f string
a = int(input("Enter a number:"))

print(f"The square of the number is:{a**2}")