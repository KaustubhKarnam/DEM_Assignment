import numpy as np
import math
import matplotlib.pyplot as plt
r = 0.5
n = 20 #Size of y in grid
m = 20 #Size of x in grid
x = []
y = []
for j in range (0, m):
    for i in range (0, n):
        y.append (math.sqrt(((2*r)**2)-((r)**2))*i)
        

for i in range (1, ((2*m)+1), 2):
    for j in range(0, int(n/2)):
        x.append ((r*i))
        x.append (r*(i-1))
 
x = np.array(x)
y = np.array(y)

""" print (x)
print(len(x)) """
fig, ax = plt.subplots()
for i in range(0,n*m):
    circles = plt.Circle((x[i], y[i]), r, color='black')
    ax.add_artist(circles) 
    plt.annotate(i, (x[i], y[i]), color = 'white')


ax.set_xlim(-r,n)
ax.set_ylim(-r,m)
plt.show()