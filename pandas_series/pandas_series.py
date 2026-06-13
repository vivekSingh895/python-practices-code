import pandas as pd
import numpy as np

# series = pd.read_csv("fours-sixes.csv")
# print(series)
# a = series.iloc[:,0]
# b = series.loc[:,"Sixes"]
# print()
# print(b)
# print(type(a))

data_fra = pd.read_csv("document_pandas\gayle-175.csv",index_col="batsman_runs")
print(data_fra)
series1 = data_fra.loc[:,"batsman"]
print()
print(type(series1))