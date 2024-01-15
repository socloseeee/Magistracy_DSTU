import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics.gofplots import qqplot

data = pd.read_excel("assets/generated_data.xlsx")

# Создание пустого датафрейма для описательной статистики
stats_df = pd.DataFrame(columns=['Distribution', 'Count', 'Mean', 'Std', 'Min', '25%', '50%', '75%', 'Max'])


for column in data.columns:
    sample = data[column]

    # Описательная статистика
    stats = sample.describe()
    print(f"Описательная статистика для {column}:\n{stats}\n")

    # Добавление данных в датафрейм
    stats_df = pd.concat([stats_df, pd.DataFrame({
        'Distribution': [column],
        'Count': [stats['count']],
        'Mean': [stats['mean']],
        'Std': [stats['std']],
        'Min': [stats['min']],
        '25%': [stats['25%']],
        '50%': [stats['50%']],
        '75%': [stats['75%']],
        'Max': [stats['max']]
    })])

    # Гистограмма
    plt.figure(figsize=(10, 6))
    sns.histplot(sample, kde=True)
    plt.title(f"Гистограмма для {column}")
    plt.show()
    plt.savefig(f"results/1_BiPuExpNorm/{column}/Гистограмма.png")

    # Диаграмма ящик с усами
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=sample)
    plt.title(f"Диаграмма ящик с усами для {column}")
    plt.show()
    plt.savefig(f"results/1_BiPuExpNorm/{column}/Диаграмма ящик с усами.png")

    # Q-Q Plot для нормального распределения
    plt.figure(figsize=(10, 6))
    qqplot(sample, line='s')
    plt.title(f"Q-Q Plot для {column}")
    plt.show()
    plt.savefig(f"results/1_BiPuExpNorm/{column}/Q-Q Plot для нормального распределения.png")

    stats_df.to_excel(f"results/1_BiPuExpNorm/{column}/stats.xlsx", index=False)
    stats_df.drop(index=stats_df.index, inplace=True)
