from math import trunc


def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
}
flag = True
while flag:
    current = 0
    num1 = int(input("Enter the First number: "))
    num2 = int(input("Enter the Second number: "))
    for i in operations:
        print(i)
    operation_symbol = input("Pick an Operation from Above: ")
    if operation_symbol == "+":
        print(f"The Addition of {num1} and {num2} is {add(num1,num2)}")
        current += add(num1,num2)
    elif operation_symbol == "-":
        print(f"The Subtraction of {num1} and {num2} is {sub(num1,num2)}")
        current += sub(num1,num2)
    elif operation_symbol == "*":
        current += mul(num1,num2)
        print(f"The Multiplication of {num1} and {num2} is {mul(num1,num2)}")

    elif operation_symbol == "/":
        current += div(num1,num2)
        print(f"The Division of {num1} and {num2} is {div(num1,num2)}")
    else :
        print("Invalid Symbol")
    dec= input("press Y to continue and N to quit: ").lower()
    if dec == "n":
        flag = False
        print("Thank you for using the Calculator")

 