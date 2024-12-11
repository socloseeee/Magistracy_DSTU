import numpy as np


# Метод Якоби
def Yakobi(A, b, max_iterations=100, tolerance=1e-6):
    n = len(b)
    x = np.zeros(n)

    for iteration in range(max_iterations):
        x_new = np.copy(x)
        for i in range(n):
            sigma = 0
            for j in range(n):
                if j != i:
                    sigma += A[i, j] * x[j]
            x_new[i] = (b[i] - sigma) / A[i, i]
        if np.linalg.norm(x_new - x) < tolerance:
            return x_new
        x = x_new
    return x


# Метод Зейделя
def Zejdel(A, b, max_iterations=100, tolerance=1e-6):
    n = len(b)
    x = np.zeros(n)

    for iteration in range(max_iterations):
        for i in range(n):
            sigma1 = np.dot(A[i, :i], x[:i])
            sigma2 = np.dot(A[i, i+1:], x[i+1:])
            x[i] = (b[i] - sigma1 - sigma2) / A[i, i]
        if np.linalg.norm(np.dot(A, x) - b) < tolerance:
            return x
    return x


# Метод минимальных невязок
def conjugate_gradient_method(A, b, max_iterations=100, tolerance=1e-6):
    n = len(b)
    x = np.zeros(n)
    r = b - np.dot(A, x)
    p = r

    for iteration in range(max_iterations):
        Ap = np.dot(A, p)
        alpha = np.dot(r, r) / np.dot(p, Ap)
        x = x + alpha * p
        r_new = r - alpha * Ap
        if np.linalg.norm(r_new) < tolerance:
            return x
        beta = np.dot(r_new, r_new) / np.dot(r, r)
        p = r_new + beta * p
        r = r_new
    return x


# Метод скорейшего спуска
def steepest_descent_method(A, b, max_iterations=100, tolerance=1e-6):
    n = len(b)
    x = np.zeros(n)
    r = b - np.dot(A, x)
    p = r

    for iteration in range(max_iterations):
        Ap = np.dot(A, p)
        alpha = np.dot(r, r) / np.dot(p, Ap)
        x = x + alpha * p
        r_new = r - alpha * Ap
        if np.linalg.norm(np.dot(A, x) - b) < tolerance:
            return x
        beta = np.dot(r_new, r_new) / np.dot(r, r)
        p = r_new + beta * p
        r = r_new
    return x


A = np.array([[9, -2, 5],
              [-2, 10, 7],
              [5, 7, 12]], dtype=np.float64)

b = np.array([-12, 2, -6], dtype=np.float64)

yakobi = Yakobi(A, b)
zejdel = Zejdel(A, b)
con_meth = conjugate_gradient_method(A, b)
steep_des_meth = steepest_descent_method(A, b)

print(f"Метод Якоби: {yakobi}\n")
print(f"Метод Зейделя: {zejdel}\n")
print(f"Метод минимальных невязок: {con_meth}\n")
print(f"Метод скорейшего спуска:{steep_des_meth}\n")

