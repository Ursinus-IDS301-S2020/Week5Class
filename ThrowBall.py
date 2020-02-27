"""
Programmer: Chris Tralie
Purpose: To simulate gravitation at the earth's surface
         with Euler steps and vpython, and to apply a simple
         elastic collision with the ground
"""
from vpython import *
import numpy as np
import time

# Make a vpython square box for the floor
floorbox = box(pos=vector(0, 0, 0), length=100, height=0.1, width=100, color=color.cyan) 

# Setup variables for the sphere
radius = 1
a = np.array([0, -9.81, 0]) # Acceleration vector
p = np.array([0, 10, 0]) # Initial position vector
v = np.array([0, 10, 0]) # Initial velocity vector
# Setup a vpython object to store the 
ball = sphere(pos=vector(p[0], p[1], p[2]), radius=radius, color=vector(1, 1, 0))

# The animation loop
tic = time.time()
while True:
    ## Step 1: Figure out the elapsed time
    toc = time.time()
    dt = toc-tic
    tic = toc # Save the timestamp for next time
    ## Step 2: Apply physics
    v = v + dt*a
    p = p + dt*v
    if p[1] < radius/2:
        # Make the ball bounce by flipping the velocity
        # Play with fac to change how much it bounces
        # If it's 1, it bounces back with all energy in y
        # If it's 0, it loses all its energy in y 
        fac = 0.5
        p[1] = radius
        v[1] = -fac*v[1]
    ## Step 3: Update the graphics by passing over the numpy array
    ## to the position object and setting it to be a vpython vector
    ball.pos = vector(p[0], p[1], p[2])