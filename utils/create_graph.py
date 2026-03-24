import numpy as np
import matplotlib.pyplot as plt

x = np.loadtxt("output/sizes.txt")
y1 = np.loadtxt("output/bubble_sort.txt")
y2 = np.loadtxt("output/merge_sort.txt")
y3 = np.loadtxt("output/quick_sort.txt")

# Создаём 3 вертикальных подграфика
fig, axes = plt.subplots(3, 1, figsize=(8, 10))

axes[0].plot(x, y1, "b-")
axes[0].set_ylabel("Y1")
axes[0].grid(True)
axes[0].set_title("bubble_sort")

axes[1].plot(x, y2, "r--")
axes[1].set_ylabel("Y2")
axes[1].grid(True)
axes[1].set_title("merge_sort")

axes[2].plot(x, y3, "g-.")
axes[2].set_xlabel("X")
axes[2].set_ylabel("Y3")
axes[2].grid(True)
axes[2].set_title("quick_sort")

plt.tight_layout()
plt.savefig("output/result.png", dpi=300)
print("График сохранён в output/result.png")
