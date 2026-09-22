try:
    a = int(input("hello , Enter a number: "))
    print(a)

except ValueError as v:
    print("hey")
    print(v)

except Exception as e:
    print(e)

print("Thank you")
