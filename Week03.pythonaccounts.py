# pythonaccounts.py
# Author: Kevin O'Leary
# take an account number and output a censored verison with only hte last four digits visible.

accountnum = input("Type account number here: ")

# account numbers are 10 digints long so we only want from 7-10

accountnum2 = accountnum[6:]
print("XXXXXX"+accountnum2)


# Extra: 
# modify above code to deal with account numebrs of any length. 
# as we still want the last 4 digits we should be searching for the first four going from right to left. 
# this is done with engative indexing

last4 = accountnum[-4:]
length = len(accountnum) # to find out how many X's need to go before the last 4 digits, we need to know how ong the card is. 
xnumber = int(length) -4 # the number of X's required
longnumber = "X"*xnumber + last4
print(longnumber)