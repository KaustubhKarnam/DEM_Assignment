import numpy as np
import math
import matplotlib.pyplot as plt
#######################################################################
#######################################################################
# Task 1 & 2 Solution Start
#######################################################################
#######################################################################

# Initialization

r = 0.5 # Radius of element
n = 20  # size of matrix

#######################################################################
# Function to return co-ordinates of location center of the circles (elements) ...
# ... as an array of x,y
#
# Takes in values - 
# 1) size of matrix 
# 2) radius of circles (elements)
#
# Returns - 
# 1) x, y co-ordinates of elements as numpy array.


def x_y_coordinates_array (size_of_matrix,radius_of_element):
    x = []
    y = []
    r = radius_of_element
    n = size_of_matrix
    for j in range (0, n):
        for i in range (0, n):
            y.append (math.sqrt(((2*r)**2)-((r)**2))*i)
            

    for i in range (1, ((2*n)+1), 2):
        for j in range(0, int(n/2)):
            x.append ((r*i))
            x.append (r*(i-1))
    
    x = np.array(x)
    y = np.array(y)
    return (x,y)

x,y = x_y_coordinates_array(n,r) # Funtion call to get x,y values as numpy array.

""" #######################################################################
# Code to plot the hexagonal n*n grid of elements # 

fig, ax = plt.subplots()
for i in range(0,n*n):
    circles = plt.Circle((x[i], y[i]), r, color='black')
    ax.add_artist(circles) 
    plt.annotate(i, (x[i], y[i]), color = 'white')


ax.set_xlim(-r,n)
ax.set_ylim(-r,n)
plt.show()
#######################################################################  """

#######################################################################
#######################################################################
# Task 1 & 2 Solution End
#######################################################################
#######################################################################

#######################################################################
#######################################################################
# Task 3 Solution Start
#######################################################################
#######################################################################

def isInside(circle_x, circle_y, rad, x, y,n): 
    count = []
    filtered_funtion_x = []
    filtered_funtion_y = []
    # Compare radius of circle 
    # with distance of its center 
    # from given point 
    for i in range (0,n*n):
        if ((x[i] - circle_x) * (x[i] - circle_x) + 
            (y[i] - circle_y) * (y[i] - circle_y) <= rad * rad): 
            count.append(i)
            filtered_funtion_x.append(x[i])
            filtered_funtion_y.append(y[i])
    return (np.array(filtered_funtion_x),np.array(filtered_funtion_y),np.array(count))       
         
  
# calling 
circle_x = 10 
circle_y = 10  
rad = 5
filtered_x, filtered_y, count = isInside(circle_x, circle_y, rad, x, y, n)

#######################################################################
# Code to plot the hexagonal n*n grid of elements # 

fig, ax = plt.subplots()
for i in range(0,len(filtered_y)):
    value = count[i]
    circles = plt.Circle((filtered_x[i], filtered_y[i]), r, color='black')
    ax.add_artist(circles) 
    plt.annotate(value, (filtered_x[i], filtered_y[i]), color = 'white')


ax.set_xlim(-r,n)
ax.set_ylim(-r,n)
plt.show()
#######################################################################

#######################################################################
#######################################################################
# Task 3 Solution End
#######################################################################
#######################################################################