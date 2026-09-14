with open("file.txt","r")as f:
    print(f.read())


##### take how many name want to print and print them using for loop 
n=int(input("how many name you want to enter:"))

for i in range(n):
    name=input(f"Enter your name{i + 1}:")
    print(f"HELLO WHATS UP, {name}!")



##### take how many name you want to print and print them using while loop 
n=int(input("Enter how many name you want to print:"))

i=0
while(i<n):
    name=input(f"Enter your name:{i +1}")
    print(f"Hello what's up, {name}.")
    i+=1
