import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.graph_objects as go  # Исправление: импортируем нужный модуль

def mathplot_chart(mass):
    plt.plot(mass)
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('таблица 1')
    plt.show()

def seaborn_chart(mass):
    sns.set_style("ticks", {"axes.grid": True})
    df = pd.DataFrame({'x': np.arange(0, 4.01, 0.01), "y": mass})  # Исправлен вызов np.arange
    sns.lineplot(data=df, x='x', y='y', color='red')  # Исправлен вызов lineplot
    plt.title('таблица 2')
    plt.show()

def plotly_chart(mass):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=np.arange(0, 4.01, 0.01), y=mass, line=dict(color='Green')))
    fig.update_layout(title='таблица 3')
    fig.show()

# Исправление ошибки с 'x_' вместо 'x'
a = np.array([np.cos(20 * x_) / (x_ + 0.1) for x_ in np.arange(0, 4.01, 0.01)])  # Здесь используется x_

# Вызываем функции построения графиков
mathplot_chart(a)
seaborn_chart(a)
plotly_chart(a)
