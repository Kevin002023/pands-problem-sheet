# bank.py
# author: Kevin O'Leary
# Take cent uinput and output €

amount1 = int(input("Enter amount here (in cent):"))
amount2 = int(input("Enter second amount here (in cent):"))

a = amount1/100
b = amount2/100

c = (a+b)

d = str(c)


print(f"The sum of these is €" + d)
