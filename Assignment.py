import numpy as np
import math
import matplotlib.pyplot as plt
import random
#######################################################################
#######################################################################
# Task 1 & 2 Solution Start
#######################################################################
#######################################################################

# Initialization

r = 1 # Radius of element
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

#############################################################################################################

# Task 3 Solution Start
#######################################################################
#######################################################################

# Function to filter the grid
# Takes in values -
# 1) Coordinates of center of filter circle (Center of circle) (circle_x, circle_y)
# 2) Distance upto which filter should be done (Radius of Circle) (rad)
# 3) Coordinates of points to be filtered (as array) (x,y)
# 4) Size of grid (n)
# 
# Output-
# 1) Array of filtered x and y coordinates
# 2) Array of count i.e. number of the point

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
rad = 10
filtered_x, filtered_y, count = isInside(circle_x, circle_y, rad, x, y, n)

#######################################################################
""" # Code to plot the filtered hexagonal n*n grid of elements # 

fig, ax = plt.subplots()
for i in range(0,len(filtered_y)):
    value = count[i]
    circles = plt.Circle((filtered_x[i], filtered_y[i]), r, color='black')
    ax.add_artist(circles) 
    plt.annotate(value, (filtered_x[i], filtered_y[i]), color = 'white')


ax.set_xlim(-r,n)
ax.set_ylim(-r,n)
plt.show() """
#######################################################################
# Applying probability logic to filtering of the elements
#probability = [0.0,0.3,0.5,0.8,1.0] ## Include this line for multiple probability figure

probability = [0.3]

for i in range (0,len(probability)):
    number_of_elements = probability[i]*len(count)

    filtered_count = np.random.choice(count, int(number_of_elements),replace=False)

    #######################################################################
    # Code to plot the filtered with "probability" hexagonal n*n grid of elements # 
    post_prob_filter_x = []
    post_prob_filter_y = []
    post_prob_filter_value = []
    fig, ax = plt.subplots()
    for i in range(0,len(filtered_count)):
        value = filtered_count[i]
        post_prob_filter_value.append(value)
        post_prob_filter_x.append(x[value])
        post_prob_filter_y.append(y[value])
        circles = plt.Circle((x[value], y[value]), r, color='black')
        ax.add_artist(circles) 
        plt.annotate(value, (x[value], y[value]), color = 'red')


    ax.set_xlim(-r,n)
    ax.set_ylim(-r,n)
    fig.savefig('hex_matrix.png')
    #######################################################################

#######################################################################
#######################################################################
# Task 3 Solution End

#############################################################################################################

# Task 4 Solution Start (Main Program Logic)
#######################################################################
#######################################################################


for i in range (0, len(post_prob_filter_value)):
    new_val = []
    
    for j in range (0, len(post_prob_filter_value)):

        if abs(math.dist([post_prob_filter_x[j],post_prob_filter_y[j]],[post_prob_filter_x[i],post_prob_filter_y[i]])) <= (2*r):
            new_val.append(post_prob_filter_value[j])
    
    
    print(" For point ", post_prob_filter_value[i], ", the touching points are --")
    for k in range (0, len(new_val)):
        if new_val[k] != post_prob_filter_value[i]:
            print(new_val[k])

