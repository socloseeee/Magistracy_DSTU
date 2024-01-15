import numpy as np
from fractions import Fraction


# Метод Гаусса
def gauss_elimination(A, b):
    n = len(b)

    # Прямой ход
    for i in range(n):
        pivot_row = A[i]
        pivot_elem = pivot_row[i]

        # Делаем текущую главную диагональную ячейку равной 1
        pivot_row /= pivot_elem
        b[i] /= pivot_elem

        for j in range(i + 1, n):
            factor = A[j][i]
            A[j] -= factor * pivot_row
            b[j] -= factor * b[i]

    # Обратный ход
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]

    return x


# Метод LU-разложения
def lu_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        # Верхнетреугольная матрица U
        for j in range(i, n):
            U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))

        # Нижнетреугольная матрица L
        for j in range(i, n):
            if i == j:
                L[j][i] = 1
            else:
                L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]

    return L, U


# Решение методом LU-разложения
def lu_solve(L, U, b):
    # Решение Ly = b
    n = len(b)
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i] - sum(L[i][j] * y[j] for j in range(i))

    # Решение Ux = y
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i + 1, n))) / U[i][i]

    return x


# Метод прогонки
def solve_tridiagonal_system(A, b):
    n = len(b)
    alpha = np.zeros(n)
    beta = np.zeros(n)

    alpha[0] = A[0, 0]
    beta[0] = b[0] / alpha[0]

    for i in range(1, n):
        alpha[i] = A[i, i] - A[i, i - 1] * A[i - 1, i] / alpha[i - 1]
        beta[i] = (b[i] - A[i, i - 1] * beta[i - 1]) / alpha[i]

    x = np.zeros(n)
    x[-1] = beta[-1]

    for i in range(n - 2, -1, -1):
        x[i] = beta[i] - A[i, i + 1] * x[i + 1] / alpha[i]

    return x


# Rоэффициенты системы уравнений для Гаусса и Лу
A = np.array([[2, -2, 5],
              [1, 3, 7],
              [-1, -5, 1]], dtype=np.float64)
b = np.array([-12, 2, -6], dtype=np.float64)

gauss_solution = gauss_elimination(A.copy(), b.copy())
L, U = lu_decomposition(A.copy())
lu_solution = lu_solve(L, U, b.copy())

# Rоэффициенты системы уравнений для метода прогонки
A = np.array([[5, -4, 0, 0],
              [-3, 4, -1, 0],
              [0, -4, 11, -6],
              [0, 0, -7, 8]], dtype=np.float64)

b = np.array([-11, 10, 5, -5], dtype=np.float64)

progonka = solve_tridiagonal_system(A, b)

print("Решение методом Гаусса:", gauss_solution)
print("Решение методом Гаусса(ответ в виде дробей):",
      list(map(lambda x: Fraction(x).limit_denominator(), gauss_solution)))
print("Решение методом LU-разложения:", lu_solution)
print("Решение методом LU-разложения(ответ в виде дробей):",
      list(map(lambda x: Fraction(x).limit_denominator(), lu_solution)))
print("Решение методом прогонки:", progonka)
print("Решение методом прогонки(ответ в виде дробей):", list(map(lambda x: Fraction(x).limit_denominator(), progonka)))
