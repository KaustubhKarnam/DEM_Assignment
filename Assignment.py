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
    
    grid_x = []
    grid_y = []
    for i in range (0,n+1,2*r):
        for j in range (0,n+1,2*r): 
            grid_x.append(i)
            grid_y.append(j)
    plt.scatter(grid_x,grid_y)
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

# Part A - Brute Force method.

for i in range (0, len(post_prob_filter_value)):
    new_val = []
    
    for j in range (0, len(post_prob_filter_value)):

        if abs(math.dist([post_prob_filter_x[j],post_prob_filter_y[j]],[post_prob_filter_x[i],post_prob_filter_y[i]])) <= (2*r):
        
            new_val.append(post_prob_filter_value[j])
    
    
    """ print(" For point ", post_prob_filter_value[i], ", the touching points are --")
    for k in range (0, len(new_val)):
        if new_val[k] != post_prob_filter_value[i]:
            print(new_val[k]) """

### For some reason the last point is not checking for other points. Add a condition that 
### if one point has values, the correspoind point should also have the first point included
### in its list of touching points.

# Part B - Grid method.

# Making the grid with points

# Grid coordinates already added during plot ##

grid_x = []
grid_y = []
for i in range (0,n+1,2*r):
    for j in range (0,n+1,2*r): 
        grid_x.append(i)
        grid_y.append(j)

x_square = []
y_square = []
square_number = []
for j in range (0, len(grid_x)-((int(math.sqrt(len(grid_x))))+1)):
    x_square.append([grid_x[j],grid_x[j+1],grid_x[int(j+(n/2)+1)],grid_x[int(j+(n/2)+2)]])
    y_square.append([grid_y[j],grid_y[j+1],grid_y[int(j+(n/2)+1)],grid_y[int(j+(n/2)+2)]])
    square_number.append(x_square)

#print(len(square_number)) # 109 lists containing 4 values each
point_square_number = []
for i in range (0, len(square_number)):
    for j in range(0, len(post_prob_filter_x)):
        x_temp = np.array(x_square[i])
        y_temp = np.array(y_square[i])
        if (x_temp[0]<post_prob_filter_x[j]<=x_temp[3]) and (y_temp[0]<post_prob_filter_y[j]<=y_temp[3]):
            point_square_number.append(i)

print(len(point_square_number))
print(len(post_prob_filter_x))