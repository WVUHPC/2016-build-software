#!/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 0, 0.1
s = np.random.normal(mu, sigma, 1000)

# Verify the mean and the variance
if not abs(mu - np.mean(s)) < 0.01:
    print("Distribution not normal")

if not abs(sigma - np.std(s, ddof=1)) < 0.01:
    print("Distribution not normal")

# Plot a histogram

count, bins, ignored = plt.hist(s, 30, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * 
            np.exp(-(bins-mu)**2 / (2*sigma**2)), linewidth=2, color='r')

plt.show()
