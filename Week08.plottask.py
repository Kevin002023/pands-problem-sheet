# plottask.py
# Author: Kevin
# create a  progaram to create normal distrubition of 1000 values and display on a histogram

import numpy as np
import matplotlib.pyplot as plt
import random


val =  np.random.normal(5, 2, 1000)
print(val)


xpoints = np.array(range(1,11))
ypoints = xpoints*xpoints*xpoints

font1 = {'family':'serif', 'color': 'blue', 'size' : 20} # https://www.w3schools.com/python/matplotlib_labels.asp
font2 = {'family':'serif', 'color': 'red', 'size' : 15} # https://www.w3schools.com/python/matplotlib_labels.asp

plt.hist(val)
plt.title("X Cubed", fontdict = font1)
plt.xlabel("Value of x", fontdict =font2)
plt.ylabel("x^3", fontdict =font2)
plt.plot(xpoints,ypoints, color = 'r', marker ='D' )
plt.xlim(0, 11)
plt.ylim(-1, 1100) # used the limit of 1100 so you can fully see the final point. 
plt.grid() # https://www.w3schools.com/python/matplotlib_grid.asp
plt.show()
plt.savefig("Week08 task plot")
