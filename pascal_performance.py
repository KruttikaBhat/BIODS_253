import time
import numpy as np
import matplotlib.pyplot as plt
from pascal import pascal

# test parameters
line_counts = range(5, 21, 5)  # test 5, 10, 15, 20 lines
trials_per_count = 3

# store results
times = []
x_values = []

# measure execution time for each line count
for n in line_counts:
    trial_times = []
    for _ in range(trials_per_count):
        start_time = time.time()
        pascal(n)
        end_time = time.time()
        trial_times.append(end_time - start_time)
    
    # store average time for this line count
    avg_time = np.mean(trial_times)
    times.append(avg_time)
    x_values.append(n)

# create the plot
plt.figure(figsize=(8, 6))
plt.plot(x_values, times, 'bo-')
plt.xlabel('Number of Lines')
plt.ylabel('Time (seconds)')
plt.title('Pascal Triangle Generation Performance')
plt.grid(True)
plt.savefig('pascal_performance.png')
plt.close() 