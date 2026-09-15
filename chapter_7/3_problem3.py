## using for loop 

n=int(input("Enter a number:"))

for i in range(2, n):
    if(n%i) == 0:
        print("Number is not prime.")
        break

    else:
        print("Number is prime.")
\





# using while loop to check number is prime or not 

n = int(input("Enter a number: "))

is_prime = True   # assume prime until proven otherwise

if n < 2:
    is_prime = False   # numbers less than 2 are not prime
else:
    i = 2
    while i < n:
        if n % i == 0:
            is_prime = False
            break        # no need to keep checking once we find a divisor
        i += 1

if is_prime:
    print("The number is prime.")
else:
    print("The number is not prime.")