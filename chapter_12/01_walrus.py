import random
n = random.randint(1, 100)
a = -1
guesses = 0

while(a != n):
    guesses += 1
    a = int(input("Enter a number:"))
    if (a > n):
        print("lower number please.")
    else:
        print("Higher number please.")

print(f"YOU HAVE GUESSED A CORRECT NUMBER {n} IN {guesses} ATTEMPTS.")
