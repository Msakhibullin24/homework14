import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_function_seaborn(func, x_range, step=0.01):
    x = np.arange(x_range[0], x_range[1] + step, step)
    y = func(x)
    # DataFrame для использования с seaborn
    df = pd.DataFrame({'x': x, 'y': y})

    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='x', y='y', data=df, color='blue', linewidth=2.0)
    plt.xlabel("x", fontsize=12)
    plt.ylabel("y(x)", fontsize=12)
    plt.title("График функции", fontsize=16)
    plt.grid(True)  # Отображение сетки
    plt.show()
def my_function(x):
    return np.cos(20 * x) / (x + 0.1)
x_range = (0, 4) # Диапазон x и шаг котоыре у нас так то в домашке
step = 0.01

plot_function_seaborn(my_function, x_range, step)
