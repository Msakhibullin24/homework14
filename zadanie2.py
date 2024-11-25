import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

saved_file = "car_data.csv"
data = pd.read_csv(saved_file)
# 1. Boxplot
numb = "Annual Income"
categ = "Dealer_Name"

fig1 = px.box(
    data_frame=data,
    x=numb,
    y=categ,
    orientation='h',
    title="Зависимость Annual Income от Dealer_Name",
    labels={numb: "Годовой доход", categ: "Название дилера"}
)
fig1.show()
# 2. Scatterplot с цветовым разделением по категориальному признаку
numb1 = "Engine"
numb2 = "Color"
categ_scatter = "Dealer_No"

fig2 = px.scatter(
    data_frame=data,
    x=numb1,
    y=numb2,
    color=categ_scatter,
    title="Scatterplot Annual Income vs. Number of Children (разделение по Gender)",
    labels={numb1: "Годовой доход", numb2: "Количество детей", categ_scatter: "Пол"}
)
fig2.show()

# 3. нескольк категориальных признаков (seaborn)
categ1_count = "Phone"
categ2_count = "Dealer_Region"

plt.figure(figsize=(10, 6))

sns.countplot(x=categ1_count, hue=categ2_count, data=data)
plt.title(f"Countplot для {categ1_count} и {categ2_count}")
plt.xlabel(categ1_count)
plt.ylabel("Количество")
plt.show()



