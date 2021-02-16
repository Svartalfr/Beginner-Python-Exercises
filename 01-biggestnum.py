first= int(input("Enter first number: "))
second= int( input ("Enter second number: "))
third= int(input ("Enter third number: "))

if ( first >= second and first >= third):
    print("The biggest number is: ", first)
elif( second>= first and second >= third):
    print("The biggest number is: ",second)
elif( third>= first and third>= second):
    print("The biggest number is: " ,third)
else:
    ("Invalid number")
