"""
Runtime: As shown in the graph we can see visually that the linear regression line fits
well. Unfortunately the R^2 value is quiet low but that is probably due to
operations being so fast, that noise is a larger factor.

Time Complexity: O(n) -> The algorithm performs a single loop that iterates n times 
and does constant work (2 constant calls (n-1) and (n-2) inside the loop, 
its time complexity is O(n)

Optimizations Made: I used memoization to store already seen values, making repetitive
calls constant time.
"""
import time
import numpy as np
import matplotlib.pyplot as plt

memo = {}
def layup_seq(n) -> int:
    if n in memo:
        return memo[n]
    else:
        if n == 1:
            ret = 1
        elif n == 2:
            ret = 2
        elif (n % 2) == 0:
            ret = layup_seq(n-1) + layup_seq(n-2)
        elif (n % 2) == 1:
            ret = 2 * layup_seq(n-1) + layup_seq(n-2)
        memo[n] = ret
        return ret

runtimes = []
N = 10001

for n in range(1, N):
    start_time = time.perf_counter()
    layup_seq(n)
    end_time = time.perf_counter()
    runtimes.append(end_time - start_time)
print("S(10000):", memo[10000])

# Convert to numpy arrays for regression analysis
x = np.arange(1, N)
y = np.array(runtimes)
coeffs = np.polyfit(x, y, 1)
line = np.poly1d(coeffs)
y_fit = line(x)

# Compute R-squared to measure goodness of fit
SS_res = np.sum((y - y_fit) ** 2)
SS_tot = np.sum((y - np.mean(y)) ** 2)
R_squared = 1 - (SS_res / SS_tot)
print(f"Slope: {coeffs[0]}, Intercept: {coeffs[1]}, R²: {R_squared}")

plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', s=10, label='Measured runtime')
plt.plot(x, y_fit, color='red', label=f'Linear fit (R² = {R_squared:.3f})')
plt.xlabel("Input Size (N)")
plt.ylabel("Runtime (seconds)")
plt.title("N vs Runtime for Layup Sequence with Linear Regression")
plt.legend()
plt.grid(True)
plt.show()
