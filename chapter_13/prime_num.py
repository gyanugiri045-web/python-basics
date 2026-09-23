
#### by using function


def prime():
    num = int(input("Enter a number: "))

    if num <= 1:
       is_prime = False
    else:
       is_prime = True
       i = 2
       while i * i <= num:
           if num % i == 0:
              is_prime = False
              break
           i += 1

    if is_prime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

prime()




### by using for loop 

n = int(input("Enter a number:"))

for i in range(2, n):
    if (n%i) == 0:
        print("It is not a prime number.")
        break

else:
    print("It is a prime number.")




### by using while loop

n = int(input("Enter a number:"))

i = 2
 
while (i <= n-1):
    if(n%i) == 0:
        print("It is not a prime number.")
        break
    i += 1
else:
    print("It is a prime number.")
