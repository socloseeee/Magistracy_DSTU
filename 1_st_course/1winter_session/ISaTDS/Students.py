import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import statsmodels.api as sm

# Загрузка данных из Excel файла
from scipy.stats import chi2

file_path = "assets/Statistika_V_Excel.xlsx"
students = pd.read_excel(file_path, skiprows=4)


# Выделение выборок
group_1 = students["Гр1.9"]
group_2 = students["Гр2.9"]

# Описательная статистика для группы 1
print("Группа 1:")
print("Размах:", np.ptp(group_1))
print("Минимальное значение:", np.min(group_1))
print("Максимальное значение:", np.max(group_1))
print("Выборочное среднее:", np.mean(group_1))
print("Выборочная дисперсия:", np.var(group_1))
print("Коэффициент вариации:", np.std(group_1) / np.mean(group_1))
print("Ассиметрия:", stats.skew(group_1))
print("Эксцесс:", stats.kurtosis(group_1))

# Описательная статистика для группы 2
print("\nГруппа 2:")
print("Размах:", np.ptp(group_2))
print("Минимальное значение:", np.min(group_2))
print("Максимальное значение:", np.max(group_2))
print("Выборочное среднее:", np.mean(group_2))
print("Выборочная дисперсия:", np.var(group_2))
print("Коэффициент вариации:", np.std(group_2) / np.mean(group_2))
print("Ассиметрия:", stats.skew(group_2))
print("Эксцесс:", stats.kurtosis(group_2))

# Гистограммы
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.histplot(group_1, kde=True, color='blue')
plt.title('Группа 1')

plt.subplot(1, 2, 2)
sns.histplot(group_2, kde=True, color='orange')
plt.title('Группа 2')
plt.savefig('results/2_Students/Гистограмма.png')
plt.show()

# Диаграммы ящик с усами
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.boxplot(y=group_1, color='blue')
plt.title('Группа 1')

plt.subplot(1, 2, 2)
sns.boxplot(y=group_2, color='orange')
plt.title('Группа 2')
plt.savefig('results/2_Students/Ящик_с_усами.png')
plt.show()

# Графики Q-Q Plot
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
stats.probplot(group_1, dist="norm", plot=plt)
plt.title('Q-Q Plot для Группы 1')

plt.subplot(1, 2, 2)
stats.probplot(group_2, dist="norm", plot=plt)
plt.title('Q-Q Plot для Группы 2')
plt.savefig('results/2_Students/Q-Q_Plot.png')
plt.show()

# Проверка гипотезы о нормальном законе распределения
_, p_value1 = stats.shapiro(group_1)
_, p_value2 = stats.shapiro(group_2)

print("\nShapiro-Wilk тест:")
print("Группа 1 p-значение:", p_value1)
print("Группа 2 p-значение:", p_value2)

# Доверительные интервалы для математического ожидания и дисперсии
confidence_level = 0.95

# Группа 1
desc_group_1 = sm.stats.DescrStatsW(group_1)
ci_mean_group_1 = desc_group_1.tconfint_mean(alpha=confidence_level)
var_group_1 = desc_group_1.var
df_group_1 = len(group_1) - 1
ci_var_group_1 = (df_group_1 * var_group_1 / chi2.ppf((1 + confidence_level) / 2, df_group_1),
                  df_group_1 * var_group_1 / chi2.ppf((1 - confidence_level) / 2, df_group_1))

# Группа 2
desc_group_2 = sm.stats.DescrStatsW(group_2)
ci_mean_group_2 = desc_group_2.tconfint_mean(alpha=confidence_level)
var_group_2 = desc_group_2.var
df_group_2 = len(group_2) - 1
ci_var_group_2 = (df_group_2 * var_group_2 / chi2.ppf((1 + confidence_level) / 2, df_group_2),
                  df_group_2 * var_group_2 / chi2.ppf((1 - confidence_level) / 2, df_group_2))

print("\nДоверительные интервалы для математического ожидания:")
print("Группа 1:", ci_mean_group_1)
print("Группа 2:", ci_mean_group_2)

print("\nДоверительные интервалы для дисперсии:")
print("Группа 1: Дисперсия =", var_group_1, "Интервал =", ci_var_group_1)
print("Группа 2: Дисперсия =", var_group_2, "Интервал =", ci_var_group_2)

# Проверка существенных различий между группами
_, p_value_ttest = stats.ttest_ind(group_1, group_2)
print("\nT-тест для сравнения средних:")
print("p-значение:", p_value_ttest)

alpha = 0.05
if p_value_ttest < alpha:
    print("Отвергаем нулевую гипотезу: существуют существенные различия между группами.")
else:
    print("Нет достаточных доказательств для отвержения нулевой гипотезы.")

# Дополнительно можно использовать другие тесты, например, Mann-Whitney U test для непараметрического сравнения
_, p_value_mw = stats.mannwhitneyu(group_1, group_2)
print("\nMann-Whitney U тест:")
print("p-значение:", p_value_mw)

if p_value_mw < alpha:
    print("Отвергаем нулевую гипотезу: существуют существенные различия между группами.")
else:
    print("Нет достаточных доказательств для отвержения нулевой гипотезы.")

# Создание DataFrame с описательной статистикой
data = {
    'Группа': ['Группа 1', 'Группа 2'],
    'Размах': [np.ptp(group_1), np.ptp(group_2)],
    'Минимальное значение': [np.min(group_1), np.min(group_2)],
    'Максимальное значение': [np.max(group_1), np.max(group_2)],
    'Выборочное среднее': [np.mean(group_1), np.mean(group_2)],
    'Выборочная дисперсия': [np.var(group_1), np.var(group_2)],
    'Коэффициент вариации': [np.std(group_1) / np.mean(group_1), np.std(group_2) / np.mean(group_2)],
    'Ассиметрия': [stats.skew(group_1), stats.skew(group_2)],
    'Эксцесс': [stats.kurtosis(group_1), stats.kurtosis(group_2)],
    'Shapiro-Wilk тест p-значение': [p_value1, p_value2],
    'Доверительный интервал для среднего': [ci_mean_group_1, ci_mean_group_2],
    'Доверительный интервал для дисперсии': [ci_var_group_1, ci_var_group_2],
    'T-тест p-значение': [p_value_ttest, None],
    'Mann-Whitney U тест p-значение': [p_value_mw, None]
}

df = pd.DataFrame(data)
df.to_excel("results/2_Students/students.xlsx", index=False)
