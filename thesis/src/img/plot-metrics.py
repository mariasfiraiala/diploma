import matplotlib.pyplot as plt
import numpy as np

libs = ["lib-qemu", "lib-musl", "lib-lwip", "lib-nginx", "lib-python3"]
sources = [1091, 1895, 25, 69, 237]

bars = plt.bar(libs, sources)
plt.bar_label(bars)

plt.title("Number of sources in popular Unikraft libraries")
plt.show()