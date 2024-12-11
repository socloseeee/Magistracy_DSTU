import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange, interp1d, CubicSpline
from scipy.optimize import curve_fit

# Заданные значения
x_values = np.array([1, 2, 3, 6, 7, 9, 10, 13, 15])
y_values = np.array([4, 8, 2, 7, -1, 2, 4, 8, 3])

# Точки для построения графика
x_plot = np.linspace(1, 15, 1000)

# Точные значения функции (для сравнения)
y_exact = lambda x: np.interp(x, x_values, y_values)

# Интерполяционный полином Лагранжа
poly_lagrange = lagrange(x_values, y_values)
y_lagrange = poly_lagrange(x_plot)


# Интерполяционный полином Ньютона
poly_newton = interp1d(x_values, y_values, kind='cubic')
y_newton = poly_newton(x_plot)

# Интерполяционный кубический сплайн
spline = CubicSpline(x_values, y_values)
y_spline = spline(x_plot)

# Метод минимальных квадратов для линейной регрессии
def linear_fit(x, a, b):
    return a * x + b

params_linear, _ = curve_fit(linear_fit, x_values, y_values)
y_linear = linear_fit(x_plot, *params_linear)

# Метод минимальных квадратов для квадратичной регрессии
def quadratic_fit(x, a, b, c):
    return a * x**2 + b * x + c

params_quadratic, _ = curve_fit(quadratic_fit, x_values, y_values)
y_quadratic = quadratic_fit(x_plot, *params_quadratic)

# Метод минимальных квадратов для кубической регрессии
def cubic_fit(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

params_cubic, _ = curve_fit(cubic_fit, x_values, y_values)
y_cubic = cubic_fit(x_plot, *params_cubic)

# Данные для интерполяционного тригонометрического полинома
y_values_interp = np.array([6, 8, 0, 5, 3, 5, 7])

# Интерполяционный тригонометрический полином
theta_interp = np.linspace(0, 2 * np.pi, len(y_values_interp))
y_interp_trig = np.zeros_like(theta_interp)

for i in range(len(y_values_interp)):
    y_interp_trig += y_values_interp[i] * np.cos(i * theta_interp)

# График
plt.plot(theta_interp, y_interp_trig, label='Интерполяционный тригонометрический полином')

plt.plot(x_plot, y_linear, label='Линейная регрессия')
plt.plot(x_plot, y_quadratic, label='Квадратичная регрессия')
plt.plot(x_plot, y_cubic, label='Кубическая регрессия')

plt.plot(x_plot, y_spline, label='Кубический сплайн')

plt.plot(x_plot, y_lagrange, label='Лагранж')
plt.plot(x_plot, y_newton, label='Ньютон')

# График точных значений
plt.plot(x_plot, y_exact(x_plot), label='Точное решение', linestyle='dashed')

# Оформление графика
plt.scatter(x_values, y_values, color='red', label='Заданные значения')
plt.title('Сравнение различных методов интерполяции и аппроксимации')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.savefig("lab6.png")
plt.show()
