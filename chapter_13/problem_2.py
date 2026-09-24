
import math

def calculate_hcf(a, b):
    return math.gcd(a, b)

def calculate_lcm(a, b, hcf):
    return (a * b) // hcf

def main():
    a = int(input("Enter a number:"))
    b = int(input("Enter a number:"))

    HCF = calculate_hcf(a, b)
    LCM = calculate_lcm(a, b, HCF)

    print(f"HCF of {a} and {b} is : {HCF}")
    print(f"LCM of {a} and {b} is : {LCM}")

main()