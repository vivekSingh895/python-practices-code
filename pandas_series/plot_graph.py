import pandas as pd
import matplotlib.pyplot as plt
cars = pd.read_csv("document_pandas\cars(10000).csv",index_col="brand")
series = cars.loc[:,"selling_price"].sort_values().copy()
print(series)
print(series.max())

series.sample(100).plot()

plt.subplots()
series.sample(30).plot(kind = "pie")

plt.subplots()
series.sample(30).plot(kind= "bar")

plt.tight_layout()
plt.show()