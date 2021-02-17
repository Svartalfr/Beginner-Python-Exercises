print("Welcome to the leap year calculator!")

year=int(input("Which year do you want to check?: "))

if year % 4 ==0:
    if year % 100 == 0:
        if year %400==0:
            print("It is a leap year!")
        else:
            print("It is not a leap year!")
    else:
        print("It is a leap year!")
else:
    print("It is not a leap year!")

