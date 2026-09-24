### simple calculator



num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))

operator = input("choices(+,-,*,/):")

if operator == "+":
    answer = num1 + num2
    print(f"answer = {answer}")

elif operator == "-":
    answer = num1 - num2
    print(f"answer = {answer}")

elif operator == "*":
    answer = num1 * num2
    print(f"answer = {answer}")

elif operator == "/":
    answer = num1 / num2
    print(f"answer = {answer}")

else:
    print("Invalid number!")
