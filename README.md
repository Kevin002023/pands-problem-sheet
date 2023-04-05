# **Pands-Problem-Sheet**

## **Table of Contents**

1. Week01 - [helloworld.py](#week01---helloworldpy)
2. Week02 - [bank.py](#week02---bankpy)
3. Week03 - [pythonaccounts.py](#week03---pythonaccountspy)
4. Week04 - [collatz.py](#week03---pythonaccountspy)
5. Week05 - [weekday.py](#week05---weekdaypy)
6. Week06 - [sqrt.py](#week06---sqrtpy)
7. Week07 - [es.py](#week07---espy)
8. Week08 - 


## **Week01 - helloworld.py**

I created a programme that when initiated would present the user with the message "Hello World!". We also set up this repository and linked it to our machines.

```
print("HelloWorld.py")
```

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

```
last4 = accountnum[-4:]
```

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


## **Week04 - collatz.py**

I created a program that would ask the user to input a postiive integer. It would then use this input in the collatz equations below

- if even then divide it by two 
- if odd then multiply it by three and add one. 

The idea is that no matter how many steps it takes all numbers will eventually reduce to the steps 4 - 2 - 1. This has been unable to be proven but seems to work for all numbers up to 2**68. This [video](https://www.youtube.com/watch?v=094y1Z2wpJg&t=1) explained the background of this problem to me. 

```
n = int(input("Insert number here: "))
```

This code asks the user to input a number which will then be used in the below calculations. 

```

while (n != 1):
        print(n,end=" ")      
```


This will output a list of all steps in the below calculations. I used 'end="" ' as I wanted them all to appear on the same line as per our task. I read about control flow and the while statement [here](https://s3-us-west-2.amazonaws.com/python-notes/a-whirlwind-tour-of-python-2.pdf)

```
 if (n%2 == 0):          
            n = n//2            
        else:               
            n = (n*3)+1
print(n)
```


Using 'n%2 == 0' we can find out if the integer is even. If it is then its directed to the next line, which divides it by 2. If the integer is odd it is directed to another equation using 'else'. This equation multiplies it by 3 and adds 1. 

The output is then added to our list and enters our 'while' function again. Once the number = 1 this ends. 

References:
https://www.youtube.com/watch?v=094y1Z2wpJg&t=1
https://s3-us-west-2.amazonaws.com/python-notes/a-whirlwind-tour-of-python-2.pdf
https://www.w3schools.com/python/python_while_loops.asp



## **Week05 - weekday.py**

I created a program, that could tell you if today is a weekday or weekend. 

Doing some research, I found [here](https://www.w3schools.com/python/python_datetime.asp), that you can import a module called datetime with useful functions. 

I first created a list of weekdays.

```
today = datetime.datetime.now()
```
This code will give you todays date

```
i = today.strftime("%A") 
```

This is a function from the datetime module that will take todays date and give you the day of the week (i).

Next I wanted to check if (i) was in our list of weekdays. I found a formula to check our list [here](https://www.geeksforgeeks.org/check-if-element-exists-in-list-in-python/)

```
if i in weekday:
    print("Yes, unfortunately today is a weekday")
else:
    print("It is the weekend, yay!")
```
This code checks if the value of (i) is in our list "Weekdays". If it is it prints that today "Yes, unfortunately today is a weekday" and if its not "It is the weekend, yay!"

References:

+ https://www.w3schools.com/python/python_datetime.asp
+ https://www.geeksforgeeks.org/check-if-element-exists-in-list-in-python/

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
if num < 0: 
    print("To find the sqaure root, we need a postive number. I will use the positive version of your number")
    num = abs(num)
```
in order to calculate a square root we need a postiive number. This code allows us to input any number to give our (a) value. There is then a check to ensure the input is greater than 0. If a negative number is given we convert it to the positive version using the abs()

```
xn =(a*0.5)  
print(xn)

```
This code  makes an estimate of the square root by dividing it by 2, giving us our (xn) value.

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

+ https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf 
+ https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo
+ https://www.youtube.com/watch?v=xdlIFw5EM4w


## **Week07 - e's.py**

I created a program that will take a filename from an argument on the command line, then open this file and calculate the number of times the character 'e' appears. 

To start with I copied this README.md file to a txt file in the pands-problem-sheet to use as an example. 

The first step was to create a function which would open a file in a readable manner and calculate the number of e's in it. I also used it to calculate the total character length. This was not required.

**This program will only work as long as the text file is in the same directory as the program**

```
def number_of_e(FILENAME): 
    with open(FILENAME, "r") as f:
        data = f.read()
        number_of_characters = len(data) 
        print(f"your file is {number_of_characters} characters long")
        e = data.count("e") 
        print(f"And the number of 'e's in the file is {e}")
```


The function number_of_e() is now defined. It opens "FILENAME" in a readbale format. Here, FILENAME serves as a placeholder. When actually using the funciton the value will be come from the command line. 

I found the formula for counting the occurences of a character [here](https://pythonexamples.org/python-count-occurrences-of-word-in-text-file/). This was e = data.count("e")


The next step was to be able to feed in the FILENAME from the command line. This took some research. [This](https://www.youtube.com/watch?v=PZN7vVxeh9M) gave me some much needed backround on how arguments work. 

I knew from this video I had to import sys and use sys.argv.

The following [video](https://www.youtube.com/watch?v=QJBVjBq4c7E) explained that the name of the code, in this case, Week07.es.py, will count as the first argument. The input will then be the second argument.

```
a = sys.argv[1]
```


The second argument [1] entered from the commandline will thefore be 'a'. Using my example file the user will input the below

```
python Week07.es.py example.txt
```


argv1[0] = Week07.es.py

argv[1] = example.txt

We can then feed this value into our original function number_of_e()

```
number_of_e(a)
```


This will then print out;
"Your file is {number_of_characters} characters long
And the number of 'e's in the file is {e}")


References: 
https://www.w3schools.com/python/python_file_handling.asp
https://pythonexamples.org/python-count-occurrences-of-word-in-text-file/
https://www.youtube.com/watch?v=PZN7vVxeh9M
https://www.youtube.com/watch?v=QJBVjBq4c7E