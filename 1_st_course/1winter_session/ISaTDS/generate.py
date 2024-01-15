import numpy as np
import pandas as pd

# Заданные параметры
mean_normal = 0
sigma_normal = 2

low_uniform = 0
high_uniform = 6

lambda_exponential = 0.5

n_binomial = 5
p_binomial = 0.8

lambda_poisson = 1.5

# Задаем seed для воспроизводимости результатов
np.random.seed(42)

# Генерация данных
normal_data = np.random.normal(mean_normal, sigma_normal, 50)
uniform_data = np.random.uniform(low_uniform, high_uniform, 50)
exponential_data = np.random.exponential(lambda_exponential, 50)
binomial_data = np.random.binomial(n_binomial, p_binomial, 50)
poisson_data = np.random.poisson(lambda_poisson, 50)

# Создаем DataFrame
data = pd.DataFrame({
    'Normal': normal_data,
    'Uniform': uniform_data,
    'Exponential': exponential_data,
    'Binomial': binomial_data,
    'Poisson': poisson_data
})

# Выводим полученные данные
print(data)

# Сохранение
data.to_excel("assets/generated_data.xlsx", index=False)
