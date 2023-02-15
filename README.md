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

We were to assume an account number would have ten digits. The numbers we wanted were always 7,8,9,10 and they were then presented as a string at the end of 6 'x's.

https://www.w3schools.in/python/repeat-string-in-python#:~:text=Sometimes%20we%20need%20to%20repeat,strings%20to%20a%20certain%20length.
