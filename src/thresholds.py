import numpy as np

def discover_thresholds(residuals):
    mean = np.mean(residuals)
    std = np.std(residuals)

    MinC = mean + 2 * std
    MaxC = mean + 3 * std
    T = 4  # seconds

    return MinC, MaxC, T