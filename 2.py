import numpy as np
import matplotlib.pyplot as plt

def plot_function():
    x = np.arange(0, 4.01, 0.01)  # Создаем массив x с шагом 0.01
    y = np.cos(20 * x) / (x + 0.1) # Вычисляем значения y

    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("y(x)")
    plt.title("График функции y(x) = cos(20x) / (x + 0.1)")
    plt.grid(True)
    plt.show()

plot_function()
