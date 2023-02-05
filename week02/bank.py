# bank.py
# author: Kevin O'Leary
# Take cent uinput and output €

x = float(input("Enter amount here (in cent):"))
y = float(input("Enter second amount here (in cent):"))

a = x/100
b = y/100

c = (a+b)

d = str(c)


print(f"The sum of these is €" + d)
