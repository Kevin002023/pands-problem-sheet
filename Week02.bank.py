# bank.py
# author: Kevin O'Leary
# Take cent input and output €

amount1 = int(input("Enter amount here (in cent):"))
amount2 = int(input("Enter second amount here (in cent):"))

# in order to avoid floats I used floor division to obtain the euro and modulus the cent totals
total = amount1+amount2

euro = str(total//100)
cent = str(total%100)


print(f"The sum of these is €" + euro + "." + cent.zfill(2) )
