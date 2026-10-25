import numpy as np
import matplotlib.pyplot as plt
import time

def z(x, y):
    return (2*x**2 + y**2) * np.exp(-x**2 - y**2)

def grad_z(x, y):
    e = np.exp(-x**2 - y**2)
    dz_dx = 2*x*e*(2 - 2*x**2 - y**2)
    dz_dy = 2*y*e*(1 - 2*x**2 - y**2)
    return np.array([dz_dx, dz_dy])

start_point = np.array([0.5, 0.5])
eps = 1e-6
delta = 1e-6
max_iter = 10000
a0 = 0.2
gamma = 0.05

path = [start_point]
current_point = start_point
z_curr = z(*current_point)

start_time = time.time()

for k in range(max_iter):
    grad = grad_z(*current_point)
    a_k = a0 / (1 + gamma * k)
    next_point = current_point - a_k * grad
    z_next = z(*next_point)
    
    delta_f = abs(z_next - z_curr)
    delta_arg = np.linalg.norm(next_point - current_point)
    
    path.append(next_point)
    
    if delta_f < eps or delta_arg < delta:
        current_point = next_point
        z_curr = z_next
        stop_reason = "Малое приращение функции (|Δf| < ε)" if delta_f < eps else "Малое приращение аргумента (||Δr|| < δ)"
        break
        
    current_point = next_point
    z_curr = z_next

end_time = time.time()
path = np.array(path)

print(f"Критерий остановки: {stop_reason}")
print(f"Число итераций: {k}")
print(f"Полученная точка: ({current_point[0]:.6f}, {current_point[1]:.6f})")
print(f"Значение функции: {z_curr:.8f}")
print(f"Время работы: {end_time - start_time:.4f} сек.")
print(f"Точный ответ (глобальный минимум): z(0,0) = 0.0")

plt.figure(figsize=(8, 6))
x_grid = np.linspace(-1, 1, 300)
y_grid = np.linspace(-1, 1, 300)
X, Y = np.meshgrid(x_grid, y_grid)
Z = z(X, Y)

contour = plt.contour(X, Y, Z, levels=25, cmap='viridis')
plt.colorbar(contour, label='Значение z')
plt.plot(path[:, 0], path[:, 1], 'ro-', markersize=2, linewidth=1, label='Траектория')
plt.plot(path[0, 0], path[0, 1], 'bo', markersize=8, label=f'Старт ({start_point[0]}, {start_point[1]})')
plt.plot(0, 0, 'g*', markersize=15, label='Цель (0, 0)')
plt.plot(current_point[0], current_point[1], 'rx', markersize=10, markeredgewidth=2, label='Результат')

plt.title('Траектория градиентного спуска')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()