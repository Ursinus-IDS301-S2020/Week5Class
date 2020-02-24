#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 11:25:13 2020

@author: ctralie
"""
import numpy as np
import matplotlib.pyplot as plt

n_trials = 10000
experiments = np.zeros(n_trials)
for trial in range(n_trials):
    # The outer loop does some fixed number of experiments
    num_in_row = 0
    total_flips = 0
    while num_in_row < 10:
        # The inner loop performas a single experiment of
        # flipping until 10 yeads in a row
        if np.random.randint(2) == 0:
            ## Heads
            num_in_row = num_in_row + 1
        else:
            ## Tails
            num_in_row = 0
        total_flips = total_flips + 1
    # Save off the result of this experiment
    experiments[trial] = total_flips
# Make a histogram of all of the experiments
plt.hist(experiments, bins=50)
plt.xlabel("Number of flips to get 10 in a row")
plt.ylabel("How many times that happened")
plt.show()
