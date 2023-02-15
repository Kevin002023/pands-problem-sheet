# Pands-Problem-Sheet

## **Week01 - helloworld.py**

I created a programme that when initiated would present the user with the message "Hello World!"

This was done by following [the week one lecture](https://web.microsoftstream.com/video/5db36fd4-f7b5-42dd-925f-87b7530c1b2f)

### **Week02 - bank.py**

I created a programme, that would prompt the user to enter two monetary amounts in cents, then add these together and then present them in a euro format to two decimal places.

This was done by following [the week two lecture](https://web.microsoftstream.com/video/a837d9b7-e63f-4df7-942f-461aade818e9)

However whenever the cent amount was a multiple of ten the programme would only output to 1 decimal place. I was able to correct this using the following [resource](https://pythonguides.com/python-print-2-decimal-places/) 

The code " format_b = "{:.2f}".format(b)"  ensures you get an output to 2 decimal places.

## **Week03 - pythonaccounts.py**

I created a programme that would prompt the user to enter a bank account number, then would present the last 4 digits as an identifier with the proceeding numbers replaced with an 'x'.

There were two parts to this task. 

**Part 1**

We were to assume an account number would have ten digits. The numbers we wanted were always 7,8,9,10. I spliced these out using a formula I found in [W3schools](https://www.w3schools.com/Python/python_strings_slicing.asp) and they were then presented as a string at the end of 6 'x's.

**Part 2**

We were to alter our code so that it would carry out the same function for an account number of any size.  The key information is still the last 4 digits however now we dont know how many digits preceed them. The solution to this is to find the first 4 numebrs when reading right to left. I used negative indexing to achieve this. 

``
last4 = accountnum[-4:]
``

This code isolates the important last 4 digits. 

`length = len(accountnum)

xnumber = int(length) -4`

This code calculates how long the account number is and then how many X's we need in front of the last 4 digits. 

`longnumber = "X"*xnumber + last4

print(longnumber)`

This code presents the correct number of X's required. This was done by repeated a string (x) by the number of digits we want to replace. The formulat to repeat a string was found [here](https://www.w3schools.in/python/repeat-string-in-python#:~:text=Sometimes%20we%20need%20to%20repeat,strings%20to%20a%20certain%20length)
