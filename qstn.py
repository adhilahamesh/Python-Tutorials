# Q12
a = int(input("Enter no:of days:"))
print("Weeks:",a // 7)
print("Remaining days:",a % 7)

# Q13
a = float(input("Enter no:of seconds:"))
print("Minutes:",a // 60)
print("Remaining seconds:",a % 60)

# Q14
amount = float(input("Enter amount in rupees:"))
discount = float(input("Enter Discount Percentage:"))
discountpercent = (amount * discount)/100
finalamount = amount - discountpercent
print("Discount amount is",discountpercent)
print("Final amount is",finalamount)