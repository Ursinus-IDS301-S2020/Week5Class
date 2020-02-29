#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 18:10:42 2020

@author: ctralie

Purpose: To show how to do a random walk
This example should help you in the chaos game assignment

"""
import numpy as np
import matplotlib.pyplot as plt

n_points = 2000
# Setup an array to hold all of the points that 
# we generate.  Each point is along a row.  
# The first column holds the x coordinates
# The second column holds the y coordinates
X = np.zeros((n_points, 2))
# Start at the point (0, 0)
p = np.array([0, 0])
for i in range(n_points):
    # Choose a random number that's 0, 1, 2, or 3
    choice = np.random.randint(4)
    if choice == 0:
        # Move one unit to the right if it's 0, so add 1 to x
        p[0] = p[0] + 1
    elif choice == 1:
        # Move one unit to the left if it's 1, so subtract 1 from x
        p[0] = p[0] - 1
    elif choice == 2:
        # Move one unit up if it's 2, so add 1 to y
        p[1] = p[1] + 1
    else:
        # Move one unit down if it's 3, so subtract 1 from y
        p[1] = p[1] - 1
    # Once we've updated p, add it to the ith row of our points
    X[i, :] = p


plt.scatter(X[:, 0], X[:, 1], c=np.arange(n_points), cmap='gray')
plt.show()