# Pands-Problem-Sheet

## **Week01 - helloworld.py**

I created a programme that when initiated would present the user with the message "Hello World!"

This was done by following [the week one lecture](https://web.microsoftstream.com/video/5db36fd4-f7b5-42dd-925f-87b7530c1b2f)

## **Week02 - bank.py**

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

```
length = len(accountnum)
xnumber = int(length) -4
```

This code calculates how long the account number is and then how many X's we need in front of the last 4 digits. 

```
longnumber = "X"*xnumber + last4
print(longnumber)
```


This code presents the correct number of X's required. This was done by repeated a string (x) by the number of digits we want to replace. The formulat to repeat a string was found [here](https://www.w3schools.in/python/repeat-string-in-python#:~:text=Sometimes%20we%20need%20to%20repeat,strings%20to%20a%20certain%20length)


## **Week06 - sqrt.py**

I created a programm, that would use the Newton - Raphson method of calculating a square root. 

Reading the following [document](https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf)  I found the following formula;
xn+1 = (xn + (a/xn))/2.

The formula asks you to estimate a square root of a number. 

a= any number
xn =  estimate of the square root of a

The formuala gives an output which is a more accurate square root of a.  By using the above formula for a number of iterations each time replacing xn with the output of the forumla (xn_b), the approximate square roote gets more accurate each iteration. When the xn value and the xn_b value are the same, we have found the accurate square root of a. 

```
a = float(input("Insert a positive number here: "))
xn =(a*0.5)  
print(xn)

```
This code allows us to input any positive number to give our (a) value and makes an estimate of the square root by dividing it by 2, giving us our (xn) value.

```
xn_b = ((a/xn)+xn)*0.5 
while (xn_b != xn):
    xn = xn_b
    xn_b = ((a/xn)+xn)*0.5  
print(f"The square root of {a} is {xn_b}")
```

This code will run our (a) and our (xn) values through our formula - (a/xn)+xn)*0.5. The while loop will take the output of this formula and feed it back in as (xn_b). it will contineu to run iterations until the two values are the same. This value is the square root we were looking for. The code will then print this value.

**Part 2**

As the tasked asked for this in a function, I defined a function called sqrt(a) and used the above code. 

**References:**

https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf
https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo
https://www.youtube.com/watch?v=xdlIFw5EM4w
