import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.graph_objects as go

def mathplot_chart(mass):
    plt.plot(mass)
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('таблица 1')
    plt.show()

def seaborn_chart(mass):
    sns.set_style("ticks", {"axes.grid": True})
    df = pd.DataFrame({'x': np.arange(0, 4.01, 0.01), "y": mass})
    sns.lineplot(data=df, x='x', y='y', color='red')
    plt.show()

def plotly_chart(mass):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=np.arange(0, 4.01, 0.01), y=mass, line=dict(color='Green')))
    fig.update_layout(title='таблица 3')
    fig.show()

a = np.array([np.cos(20 * x_) / (x_ + 0.1) for x_ in np.arange(0, 4.01, 0.01)])


mathplot_chart(a)
seaborn_chart(a)
plotly_chart(a)
