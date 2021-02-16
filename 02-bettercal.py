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
    print("Sıfıra bölünemez")

    a = int(input())
b = int(input())