import numpy as np
import matplotlib.pyplot as plt


class Drawer():
    def __init__(self, files_y: list[str], file_x: str) -> None:
        self._nums_y = _getFiles_y(files_y);

    def _getFiles_y() -> list[list[int]]:


x = np.loadtxt("x.txt")
y1 = np.loadtxt("y1.txt")
y2 = np.loadtxt("y2.txt")
y3 = np.loadtxt("y3.txt")

# Создаём 3 вертикальных подграфика
fig, axes = plt.subplots(3, 1, figsize=(8, 10))

axes[0].plot(x, y1, 'b-')
axes[0].set_ylabel('Y1')
axes[0].grid(True)
axes[0].set_title('График 1')

axes[1].plot(x, y2, 'r--')
axes[1].set_ylabel('Y2')
axes[1].grid(True)
axes[1].set_title('График 2')

axes[2].plot(x, y3, 'g-.')
axes[2].set_xlabel('X')
axes[2].set_ylabel('Y3')
axes[2].grid(True)
axes[2].set_title('График 3')

plt.tight_layout()
plt.show()
