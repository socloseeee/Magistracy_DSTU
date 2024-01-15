import numpy as np
import matplotlib.pyplot as plt

# Заданные параметры
def f(t, y):
    return -2*y + np.cos(t) + np.sin(t)

def exact_solution(t):
    return np.exp(-2*t) + np.sin(t) + 2*np.cos(t)

# Метод Эйлера
def euler_method(f, y0, t_values):
    y_values = [y0]
    for i in range(1, len(t_values)):
        h = t_values[i] - t_values[i-1]
        y_next = y_values[-1] + h * f(t_values[i-1], y_values[-1])
        y_values.append(y_next)
    return y_values

# Метод Рунге-Кутта второго порядка
def runge_kutta2_method(f, y0, t_values):
    y_values = [y0]
    for i in range(1, len(t_values)):
        h = t_values[i] - t_values[i-1]
        k1 = h * f(t_values[i-1], y_values[-1])
        k2 = h * f(t_values[i-1] + 0.5*h, y_values[-1] + 0.5*k1)
        y_next = y_values[-1] + k2
        y_values.append(y_next)
    return y_values

# Метод Рунге-Кутта четвертого порядка
def runge_kutta4_method(f, y0, t_values):
    y_values = [y0]
    for i in range(1, len(t_values)):
        h = t_values[i] - t_values[i-1]
        k1 = h * f(t_values[i-1], y_values[-1])
        k2 = h * f(t_values[i-1] + 0.5*h, y_values[-1] + 0.5*k1)
        k3 = h * f(t_values[i-1] + 0.5*h, y_values[-1] + 0.5*k2)
        k4 = h * f(t_values[i-1] + h, y_values[-1] + k3)
        y_next = y_values[-1] + (k1 + 2*k2 + 2*k3 + k4) / 6
        y_values.append(y_next)
    return y_values

# Задание начальных условий
y0 = 3
t_values = np.linspace(0, 5, 100)

# Решение уравнения для каждого метода
euler_solution = euler_method(f, y0, t_values)
rk2_solution = runge_kutta2_method(f, y0, t_values)
rk4_solution = runge_kutta4_method(f, y0, t_values)

# Точное решение
exact_solution_values = exact_solution(t_values)

# Построение графиков
plt.figure(figsize=(10, 6))
plt.plot(t_values, exact_solution_values, label='Точное решение', linewidth=2)
plt.plot(t_values, euler_solution, label='Метод Эйлера', linestyle='--')
plt.plot(t_values, rk2_solution, label='Рунге-Кутта 2 порядка', linestyle='-.')
plt.plot(t_values, rk4_solution, label='Рунге-Кутта 4 порядка', linestyle=':')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.title('Сравнение численных методов с точным решением')
plt.grid(True)
# plt.savefig("lab5.png")
plt.show()
"""
9.  От чего зависит погрешность численного решения задачи Коши?
Погрешность зависит от выбранного численного метода, 
шага интегрирования, исходных условий, а также свойств 
самого уравнения. Уменьшение шага интегрирования обычно приводит к уменьш
"""