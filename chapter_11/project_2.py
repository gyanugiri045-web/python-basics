import random
n = random.randint(1,100)
a= -1
guesses = 0

while(a != n):
    guesses += 1
    a = int(input("Guess the number :"))
    if (a > n):
        print("LOWER NUMBER PLEASE.")
    else:
        print("HIGHER NUMBER PLEASE.")

print(f"You have guessed a number {n} correctly in {guesses} attempt")
