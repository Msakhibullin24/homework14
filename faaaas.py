import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Функция для построения графика с использованием seaborn
def plot_function_seaborn(func, x_range, step=0.01):
    # Генерация данных
    x = np.arange(x_range[0], x_range[1] + step, step)
    y = func(x)
    data = pd.DataFrame({'x': x, 'y': y})
    
    # Настройка стиля
    sns.set(style="whitegrid")
    
    # Построение графика
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='x', y='y', data=data, color="blue", linewidth=2.5)
    plt.xlabel("x", fontsize=12)
    plt.ylabel("y(x)", fontsize=12)
    plt.title("График функции y(x) = cos(20x) / (x + 0.1)", fontsize=14)
    plt.grid(True)  # Дополнительная сетка для визуализации
    plt.show()

# Функция, которую мы отображаем
def my_function(x):
    return np.cos(20 * x) / (x + 0.1)

# Заданные параметры
x_range = (0, 4)  # Диапазон x
step = 0.01  # Шаг

# Вызов функции для построения графика
plot_function_seaborn(my_function, x_range, step)
