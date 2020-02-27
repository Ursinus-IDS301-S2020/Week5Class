"""
Programmer: Chris Tralie
Purpose: To make a simulation of the moon orbiting the earth
         by using VPython with Euler steps
"""
from vpython import *
import numpy as np
import time
import matplotlib.pyplot as plt

# Setup an earth vpython object and the center of the earth (which won't move)
p_earth = np.array([0, 0, 0])
earth = sphere(pos=vector(p_earth[0], p_earth[1], p_earth[2]), radius=6e7, color=vector(0, 0.5, 0.8))
M = 5.9740e24 # Mass of the earth in kilograms
G = 6.67408e-11 # Gravitational constant: meters^3/(kg*sec^2)

# Setup the initial position and velocity vectors of the moon,
# noting that the moon is about 384.4 miles away from the earth on
# average in its orbit, and that it goes at 1000 meters/second
# on average
p = p_earth + np.array([384400000, 0, 0])
v = np.array([0, 0, 1000]) # 1000 meters/second

# Setup a vpython object that will hold the moon.  
# Make it gray; (R, G, B) = (0.5, 0.5, 0.5)
moon = sphere(pos=vector(p[0], p[1], p[2]), radius=1e7, color=vector(0.5, 0.5, 0.5))

# Setup a label that will go along with the moon to tell us
# how much time has elapsed
L = label(pos=moon.pos,
    text='', xoffset=20,
    yoffset=50, space=30,
    height=16, border=4,
    font='sans')


SECONDS_IN_DAY = 3600*24
# Every second in the simulation is a day
speedup_fac = SECONDS_IN_DAY 
# Setup empty lists to store the distance of the moon 
# to the earth at every iteration of the loop, as well as
# the time elapsed at the beginning of every loop
rs = []
times = []
tic = time.time()
total_time = 0
while total_time < SECONDS_IN_DAY*60: # Go for 60 days
    ## Step 1: Figure out the elapsed time, noting that
    ## we're speeding up the animation by some factor
    toc = time.time()
    dt = (toc-tic)*speedup_fac
    total_time += dt
    tic = toc

    ## Step 2: Apply the laws of physics
    # First, setup the vector from the moon towards
    # the earth, which is p_earth - p
    direction = p_earth - p
    # Find the magnitude of this vector
    r = np.sqrt(np.sum(direction**2))
    # Divide the vector by its magnitude so it is a unit
    # vector
    direction = direction/r
    # Apply the vector law of gravitation to get the
    # acceleration
    a = direction*(G*M/r**2)
    # Update the velocity and position based on the acceleration
    v = v + dt*a
    p = p + dt*v

    ## Step 3: Update the graphics.  Change the position
    ## of the moon, and update the position/text of the label
    moon.pos = vector(p[0], p[1], p[2])
    L.pos = moon.pos
    L.text = '%.3g Days'%(total_time/(3600*24))

    ## Step 4: Save away information for plotting later
    rs.append(r)
    times.append(total_time)
    time.sleep(0.05)

## Plot the distance of the moon from the earth over time
## during the simulation.  We have to convert regular lists
## to python arrays by writing np.array(list) before plotting
times = np.array(times)/SECONDS_IN_DAY
rs = np.array(rs)
plt.plot(times, rs)
plt.xlabel("Time (days)")
plt.ylabel("Distance (meters)")
plt.show()