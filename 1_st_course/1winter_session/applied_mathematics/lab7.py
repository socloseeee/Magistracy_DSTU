import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Определение функции f(x, y)
def f(x, y):
    denominator = 1 - x ** 2
    if np.abs(denominator) < 1e-6:
        return np.nan  # возвращаем NaN в случае деления на ноль
    return (2 * x ** 3 * y ** 3 - 2 * x * y) / denominator


# Метод Эйлера
def euler_method(x, h, y0):
    y = np.zeros_like(x)
    y[0] = y0  # начальное значение y
    for i in range(1, len(x)):
        y[i] = y[i - 1] + h * f(x[i - 1], y[i - 1])
    return y


# Метод Рунге-Кутты
def runge_kutta_method(x, h, y0):
    y = np.zeros_like(x)
    y[0] = y0  # начальное значение y
    for i in range(1, len(x)):
        k1 = h * f(x[i - 1], y[i - 1])
        k2 = h * f(x[i - 1] + h / 2, y[i - 1] + k1 / 2)
        k3 = h * f(x[i - 1] + h / 2, y[i - 1] + k2 / 2)
        k4 = h * f(x[i - 1] + h, y[i - 1] + k3)
        y[i] = y[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return y


# Метод Адамса-Бэшфорта
def adams_bashforth_method(x, h, y0):
    y = np.zeros_like(x)
    y[:4] = euler_method(x[:4], h, y0)  # используем метод Эйлера для первых 4 точек
    for i in range(4, len(x)):
        y[i] = y[i - 1] + h * (55 * f(x[i - 1], y[i - 1]) - 59 * f(x[i - 2], y[i - 2]) +
                               37 * f(x[i - 3], y[i - 3]) - 9 * f(x[i - 4], y[i - 4])) / 24
    return y


def exact_solution(x, h, y0):
    y = np.zeros_like(x)
    y[0] = y0  # начальное значение y
    for i in range(1, len(x)):
        k1 = h * f(x[i - 1], y[i - 1])
        k2 = h * f(x[i - 1] + h / 2, y[i - 1] + k1 / 2)
        k3 = h * f(x[i - 1] + h / 2, y[i - 1] + k2 / 2)
        k4 = h * f(x[i - 1] + h, y[i - 1] + k3)
        y[i] = y[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return y

# Создайте массив значений x для интервала от a до b
a = 0
b = 1
num_points = 100
x_values = np.linspace(a, b, num_points)

# Заданные параметры
y_initial = 1
h = (b - a) / num_points  # шаг

# Вычисление точных значений в узловых точках
exact_values = exact_solution(x_values, h, y_initial)

# Вычисление отклонений и максимумов для каждого метода
deviations_euler = np.abs(exact_values - euler_method(x_values, h, y_initial))
max_deviation_euler = np.max(deviations_euler)

deviations_runge_kutta = np.abs(exact_values - runge_kutta_method(x_values, h, y_initial))
max_deviation_runge_kutta = np.max(deviations_runge_kutta)

deviations_adams_bashforth = np.abs(exact_values - adams_bashforth_method(x_values, h, y_initial))
max_deviation_adams_bashforth = np.max(deviations_adams_bashforth)

# Вывод результатов
print("Max deviation for Euler Method:", max_deviation_euler)
print("Max deviation for Runge-Kutta Method:", max_deviation_runge_kutta)
print("Max deviation for Adams-Bashforth Method:", max_deviation_adams_bashforth)

# Создание сводной таблицы
data = {
    'Method': ['Euler', 'Runge-Kutta', 'Adams-Bashforth'],
    'Max Deviation': [max_deviation_euler, max_deviation_runge_kutta, max_deviation_adams_bashforth],
}

results_table = pd.DataFrame(data)
print(results_table)

# Создайте графики для каждого метода
plt.figure(figsize=(12, 8))

plt.subplot(221)
plt.plot(x_values, euler_method(x_values, h, y_initial), label='Euler Method')
plt.title('Euler Method')

plt.subplot(222)
plt.plot(x_values, runge_kutta_method(x_values, h, y_initial), label='Runge-Kutta Method')
plt.title('Runge-Kutta Method')

plt.subplot(223)
plt.plot(x_values, adams_bashforth_method(x_values, h, y_initial), label='Adams-Bashforth Method')
plt.title('Adams-Bashforth Method')

# Создайте график для всех методов вместе
plt.subplot(224)
plt.plot(x_values, euler_method(x_values, h, y_initial), label='Euler Method')
plt.plot(x_values, runge_kutta_method(x_values, h, y_initial), label='Runge-Kutta Method')
plt.plot(x_values, adams_bashforth_method(x_values, h, y_initial), label='Adams-Bashforth Method')
plt.title('All Methods')

plt.legend()
plt.savefig("lab7.png")
plt.show()

