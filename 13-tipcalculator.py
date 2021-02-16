print("***Welcome to the tip calculator***")
bill=float(input("Enter the total bill: "))
tip=int(input("What percentage of tip would you like to give? ? 10 ,12 or 15?" ))
hMP=int(input("How many people will pay the bill?"))

billWithTip= tip/100*bill +bill
paySiplit= (billWithTip/hMP)

print(paySiplit)

