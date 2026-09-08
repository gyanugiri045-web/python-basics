########### write a code wheather i can vote or not
n=int(input("Enter your age:"))
if(n==0):
    print("invalid age.")
elif(n>=18):
    print("You are allowed to vote.")

elif (n<18):
    print("you are not allowed to vote.")

else:
    print("invalid age.")



###########  to find the number is positive negative or zero
n=int(input("Enter a number:"))
if(n==0):
    print("Number is zero.")
elif (n>0):
    print("Number is positive.")
else:
    print("Number is negative.")




############# user will enter the number and i need all the multiplication table of it 
n=int(input("Enter a number:"))
for i in range(1,11):
    print(f"{n}x{i} = {n * i}")


    # or by using while loop

n=int(input("Enter a number:"))
i=1

while (i<=10):
    print(n, "x", i, "=", n * i)
    i +=1
    