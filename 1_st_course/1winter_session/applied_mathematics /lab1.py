import math


# Функция, которую мы интегрируем
def f(x):
    return x ** 2 / math.sqrt(x ** 2 - 25)


# Границы интегрирования
a = 10
b = 20

# Количество интервалов для разбиения
n = 1000


# Метод прямоугольника
def rectangle_method(f, a, b, n):
    h = (b - a) / n
    integral = 0
    for i in range(n):
        x_i = a + i * h
        integral += f(x_i)
    integral *= h
    return integral


# Метод трапеций
def trapezoidal_method(f, a, b, n):
    h = (b - a) / n
    integral = 0
    for i in range(n):
        x_i = a + i * h
        x_next = a + (i + 1) * h
        integral += (f(x_i) + f(x_next)) / 2
    integral *= h
    return integral


# Метод симпсона
def simpson_method(f, a, b, n):
    h = (b - a) / n
    integral = 0
    for i in range(n):
        x_i = a + i * h
        x_next = a + (i + 1) * h
        x_mid = (x_i + x_next) / 2
        integral += (f(x_i) + 4 * f(x_mid) + f(x_next))
    integral *= h / 6
    return integral


# Вычисление интегралов
integral_rectangle = rectangle_method(f, a, b, n)
integral_trapezoidal = trapezoidal_method(f, a, b, n)
integral_simpson = simpson_method(f, a, b, n)

print("Метод прямоугольника:", integral_rectangle)
print("Метод трапеций:", integral_trapezoidal)
print("Метод симпсона:", integral_simpson)
