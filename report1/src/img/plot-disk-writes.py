import matplotlib.pyplot as plt
import numpy as np

env = ["Dom0", "MiniOS Stubdom", "Linux Stubdom"]
speed = [126, 41, 126]

plt.bar(env, speed, width=0.25)

plt.title("Disk Write Speed in MB/s")
plt.ylabel('MB/s')
plt.show()