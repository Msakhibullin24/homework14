import numpy as np
import plotly.graph_objects as go

def plot_function_plotly(func, x_range, step=0.01):

    x = np.arange(x_range[0], x_range[1] + step, step)
    y = func(x)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='y(x)', line=dict(color='blue', width=2)))


    fig.update_layout(
        title="График функции y(x) = cos(20x) / (x + 0.1)",
        xaxis_title="x",
        yaxis_title="y(x)",
        template="plotly_white",
        width=800,
        height=500
    )

    # Выводим график
    fig.show()


# по тзшки из дзшки
def my_function(x):
    return np.cos(20 * x) / (x + 0.1)



x_range = (0, 4)  # Диапазон x
step = 0.01  # Шаг

plot_function_plotly(my_function, x_range, step)
