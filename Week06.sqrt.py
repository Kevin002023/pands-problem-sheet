# sqrt.py   
# Author: Kevin
# Define a functiont that will calculate an approximate square root. 

# rearching the Newton-Raphson method i foudn the formula xn+1 = (xn + (a/xn))/2.


#a = float(input("Insert a positive number here: "))
#print(a)

# we start by finding an approximate sqaure root (xn). This can be done by diving by 2. 

#xn =(a*0.5)  
#print(xn)


# then we run xn through a series of iterations of the formula  = 0.5(xn=(a/xn)

#xn_b = ((a/xn)+xn)*0.5 # xn is an approximate square root. xn_b is a more accurate square root of a
#while (xn_b != xn):
#    xn = xn_b
#    xn_b = ((a/xn)+xn)*0.5  # when xn and xn_b have the same value, this is the square root of a
#print(f"The square root of {a} is {xn_b}")


#https://www.youtube.com/watch?v=xdlIFw5EM4w

def sqrt(a):
    
    xn =(a*0.5)
    xn_b = ((a/xn)+xn)*0.5 # xn is an approximate square root. xn_b is a more accurate sqare root of a
    while (xn_b != xn):
        xn = xn_b
        xn_b = ((a/xn)+xn)*0.5  # when xn and xn_b have the same value, this is the square root of a
    print(f"The square root of {a} is {xn_b}")

num = float(input("Insert a postive number to square here: "))
if num < 0: 
    print("To find the sqaure root, we need a postive number. I will use the positive version of your number")
    num = abs(num)
    
sqrt(num)