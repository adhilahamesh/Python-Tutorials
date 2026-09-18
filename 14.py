# Q15
price = float(input("Enter the price of product:"))
quantity = float(input("Enter the Quantity:"))
print("Total Bill is",price * quantity)

# Q16
a = float(input("Enter the total Bill:"))
b = float(input("Enter the number of people:"))
print("Each Person should pay", a/b)

# Q17
salary = float(input("Enter basic salary:"))
hra = 20 * salary/100
da = 10 * salary/100
print("Total salary is",salary+hra+da)

# Q18
p = float(input("Enter the principal:"))
r = float(input("Enter rate of interest:"))
t = float(input("Enter time:"))
print("Simple interest is",(p * r * t)/100)

# Q19
s1 = float(input("Mark of subject 1:"))
s2 = float(input("Mark of subject 2:"))
s3 = float(input("Mark of subject 3:"))
s4 = float(input("Mark of subject 4:"))
s5 = float(input("Mark of subject 5:"))
totalmark = s1 + s2+s3+s4+s5
print("Total marks is",totalmark)
print("Average mark is",totalmark/5)

# Q20
num = float(input("Enter a number:"))
print("Square of the number is",num*num)
print("cube of the number is",num*num*num)

