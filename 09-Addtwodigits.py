two_digit_number=input("Enter two digit numbers: ")
#Do not change the code above

#Check the data type

print(type(two_digit_number))

#Get the first and second digits using subscripting then convert string to int.

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

#Add the two digits togeter
two_digit_number = first_digit + second_digit

print(two_digit_number)
