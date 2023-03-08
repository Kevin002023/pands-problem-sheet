# collatz.py
# Author: Kevin O'Leary
# Prompt the user to input an integer, then output successive values. 
# if value is even divide it by 2. If the value is odd then multiply it by 3 and add 1



n = int(input("Insert number here: "))

while (n != 1):
        print(n,end=" ")        # wanted the printout to be all ont eh same line as per the example in question
        if (n%2 == 0):          # if the number is even
            n = n//2            # to ensure its a rounded number
        else:                   # if number is odd
            n = (n*3)+1
print(n)