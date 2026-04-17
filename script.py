import numpy as np
import matplotlib.pyplot as plt
import random


def f(x):
    return x ** 3


def integral_sum(a, b, n, method='right'):
    """Вычисляет интегральную сумму для f(x) на [a,b] с равномерным разбиением"""
    x = np.linspace(a, b, n + 1)
    dx = (b - a) / n
    total = 0.0

    if method == 'left':
        for i in range(n):
            total += f(x[i]) * dx
    elif method == 'right':
        for i in range(1, n + 1):
            total += f(x[i]) * dx
    elif method == 'mid':
        for i in range(n):
            total += f((x[i] + x[i + 1]) / 2) * dx
    elif method == 'random':
        for i in range(n):
            xi = random.uniform(x[i], x[i + 1])
            total += f(xi) * dx
    else:
        raise ValueError("method must be 'left', 'right', 'mid' or 'random'")
    return total


def trapezoidal_rule(a, b, n):
    """Метод трапеций"""
    x = np.linspace(a, b, n + 1)
    dx = (b - a) / n
    total = 0.5 * (f(x[0]) + f(x[-1]))
    for i in range(1, n):
        total += f(x[i])
    return total * dx

def plot_stepped(a, b, n, method='right'):
    """Рисует функцию и ступенчатую фигуру для интегральной суммы"""
    x_vals = np.linspace(a, b, 1000)
    y_vals = f(x_vals)

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, 'b-', label='f(x)=x³')

    # Построение ступенчатой фигуры
    x_nodes = np.linspace(a, b, n + 1)
    dx = (b - a) / n

    if method == 'left':
        xi = x_nodes[:-1]
    elif method == 'right':
        xi = x_nodes[1:]
    elif method == 'mid':
        xi = (x_nodes[:-1] + x_nodes[1:]) / 2
    else:  # random
        xi = [random.uniform(x_nodes[i], x_nodes[i + 1]) for i in range(n)]

    for i in range(n):
        height = f(xi[i])
        plt.bar(x_nodes[i], height, width=dx, align='edge', alpha=0.3,
                edgecolor='red', color='red', label='ступеньки' if i == 0 else "")

    plt.title(f'Интегральная сумма (метод "{method}"), n={n}\nS = {integral_sum(a, b, n, method):.6f}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()


# Параметры
a, b = 0, 2
true_value = 4.0

# Примеры вычислений
print("=== Вариант 14: f(x)=x³, [0,2] ===")
print(f"Точное значение интеграла: {true_value}\n")

for n in [10, 100]:
    print(f"Разбиение n = {n}:")
    for method in ['left', 'right', 'mid', 'random']:
        s = integral_sum(a, b, n, method)
        print(f"  {method:6s}: {s:.6f} (ошибка {abs(s - true_value):.6f})")
    # Метод трапеций
    trap = trapezoidal_rule(a, b, n)
    print(f"  трапеции: {trap:.6f} (ошибка {abs(trap - true_value):.6f})\n")

# Построение графиков для n=10 и n=100 для различных оснащений
for n in [10, 100]:
    for method in ['left', 'right', 'mid']:
        plot_stepped(a, b, n, method)