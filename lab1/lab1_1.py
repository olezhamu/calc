import numpy as np
import matplotlib.pyplot as plt

def z(x, y):
    return (2*x**2 + y**2) * np.exp(-x**2 - y**2)

x = np.linspace(-2.5, 2.5, 400)
y = np.linspace(-2.5, 2.5, 400)
X, Y = np.meshgrid(x, y)
Z = z(X, Y)

points = [(0, 0), (1, 0), (-1, 0)]
labels = ['Min', 'Max', 'Max']

fig = plt.figure(figsize=(14, 6))

ax1 = fig.add_subplot(121, projection='3d')
surf = ax1.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.8)
ax1.set_title('3D поверхность функции')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')

for (px, py), label in zip(points, labels):
    pz = z(px, py)
    ax1.scatter(px, py, pz, color='red', s=50, zorder=10)
    ax1.text(px, py, pz, f'  {label}', color='red', fontweight='bold')

ax2 = fig.add_subplot(122)
contour = ax2.contour(X, Y, Z, levels=20, cmap='viridis')
ax2.clabel(contour, inline=True, fontsize=8)
ax2.set_title('Линии уровня (Contour plot)')
ax2.set_xlabel('x')
ax2.set_ylabel('y')

for (px, py), label in zip(points, labels):
    color = 'blue' if label == 'Min' else ('red' if label == 'Max' else 'black')
    ax2.plot(px, py, marker='x', color=color, markersize=10, markeredgewidth=2)
    ax2.text(px + 0.1, py + 0.1, label, color=color, fontweight='bold')

plt.tight_layout()
plt.show()