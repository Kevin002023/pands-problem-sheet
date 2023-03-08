# weekday.py
# Author: Kevin
# A program that outputs whether today is a weekday or weekend


import datetime

weekday = ["Monday", "Tuesday", "Wednesday", "Thrusday", "Friday"]

today = datetime.datetime.now()

# from W3 schools i found a way of displaying the current day https://www.w3schools.com/python/python_datetime.asp

i = today.strftime("%A") # this generates todays day and equates it to i


if i in weekday: # this checks if i(today) is in the list weekday https://www.geeksforgeeks.org/check-if-element-exists-in-list-in-python/
    print("Yes, unfortunately today is a weekday")
else:
    print("It is the weekend, yay!")


