num1 = float(input("Enter first number: "))
op = input("Enter an operator : ")
num2 = float(input("Enter second number: "))

try:
    if op=="+":
        print(num1 + num2)
    elif op=="-":
        print(num1 - num2)
    elif op=="/":
        print(num1 / num2)
    elif op =="*":
        print(num1 * num2)
    else:
        print("Invalid operator")
except ZeroDivisionError:
    print("Cannot be divided by 0")

    a = int(input())
b = int(input())
