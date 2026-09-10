def multiply(n):
    for i in range(1,11):
        print(f"{n}x{i} = {n*i}")
        i+=1
n=int(input("Enter a number:"))
multiply(n)