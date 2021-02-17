print("Welcome to the Pizza Delivery Programme")
size= input("What size pizza do you want to have?: S,M or L \n")
add_pepperoni = input("Do you want to have pepperoni? Y or N \n")
extra_cheese = input("Do you want to have extra cheese? Y or N \n")
bill=0
if size == "S":
    bill += 15
    print("Small size pizza is $15")
elif size == "M":
    bill += 20
    print("Medium size pizza is $20")
else:
    bill += 25
    print("Large size is $25")

if add_pepperoni == "Y":
    if size == "S":
        bill +=2
    else:
        bill +=3

if extra_cheese == "Y":
    bill += 1
print(f"Your bill is $ {bill} ")

