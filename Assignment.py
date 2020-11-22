import numpy as np
import math
import matplotlib.pyplot as plt
r = 0.5
n = 10 #Size of y in grid
m = 10 #Size of x in grid
x = []
y = []
for j in range (0, m):
    for i in range (0, n):
        y.append (math.sqrt(((2*r)**2)-((r)**2))*i)
        

for i in range (1, 2*(m+1), 2):
    for j in range(0, 2*n, n):
        x.append ((r*2)*i)
        x.append (r * i)
 
x = np.array(x)
y = np.array(y)

fig, ax = plt.subplots()
for i in range(0,n*m):
    circles = plt.Circle((x[i], y[i]), r, color='black')
    ax.add_artist(circles) 
    plt.annotate(i, (x[i], y[i]), color = 'white')


ax.set_xlim(-r,10)
ax.set_ylim(-r,9)
plt.show()