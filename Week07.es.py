# es.py
# Author: Kevin
# A program that can read in any text file and output the number of 'e' characters

import sys


 # i created a function which will take in a filename and output the number of e's in the text

def number_of_e(FILENAME):  # i created a function whihc will take in a filename and output the number of e's in the text
    with open(FILENAME, "r") as f:
        data = f.read() # opens a readable version of the file as text
        number_of_characters = len(data) # not needed but i thougt it was interesting
        print(f"your file is {number_of_characters} characters long")
        e = data.count("e") # using the count function to find the string "e"
        print(f"And the number of 'e's in the file is {e}")

a = sys.argv[1]  # taking the name of the file from a command line argument. the arguments are "name of code" , input text. We only 
                #  want the second so we look for [1] which then ignores [0] (aka) the name of the code
number_of_e(a)

