import numpy as np


def bisection_method(func, a, b, tol=1e-6, max_iter=100):
    if func(a) * func(b) >= 0:
        raise ValueError("Функция на концах интервала должна иметь разные знаки")

    for i in range(max_iter):
        c = (a + b) / 2
        if func(c) == 0 or (b - a) / 2 < tol:
            return c
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
    raise ValueError("Метод половинного деления не сошелся")


def chord_method(func, a, b, tol=1e-6, max_iter=100):
    if func(a) * func(b) >= 0:
        raise ValueError("Функция на концах интервала должна иметь разные знаки")

    for i in range(max_iter):
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))
        if func(c) == 0 or abs(func(c)) < tol:
            return c
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
    raise ValueError("Метод хорд не сошелся")


def secant_method(func, x0, x1, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        x2 = x1 - (func(x1) * (x1 - x0)) / (func(x1) - func(x0))
        if func(x2) == 0 or abs(x2 - x1) < tol:
            return x2
        x0, x1 = x1, x2
    raise ValueError("Метод секущих не сошелся")


# Производная функции
def derivative(func, x, h=1e-6):
    return (func(x + h) - func(x)) / h


def newton_method(func, x0, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        x1 = x0 - func(x0) / derivative(func, x0)
        if func(x1) == 0 or abs(x1 - x0) < tol:
            return x1
        x0 = x1
    raise ValueError("Метод Ньютона не сошелся")


# Уравнение ln(x) + x - 2 = 0
def equation(x):
    return np.log(x) + x - 2


# Интервал, в котором ищем корень
a = 1.0
b = 3.0

root_bisection = bisection_method(equation, a, b)
root_chord = chord_method(equation, a, b)
root_secant = secant_method(equation, a, b)
root_newton = newton_method(equation, a)
print(f"Метод половинного деления: x = {root_bisection}")
print(f"Метод хорд: x = {root_chord}")
print(f"Метод секущих: x = {root_secant}")
print(f"Метод Ньютона: x = {root_newton}")
