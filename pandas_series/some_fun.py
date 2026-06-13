import pandas as pd
import numpy as np

new_series = pd.read_csv("document_pandas\\vk.csv",index_col =  'match_id')
data = new_series.loc[:,"batsman_runs"]
print(data)
print(type(data))
print("head function ",data.head(4))
print("tail function ",data.tail(5))
print("sample function ",data.sample(4))
print("value count ",data.value_counts().head(6))
print("sort index ",data.sort_index(ascending = False))
print("sort values ",data.sort_values().tail(10))
print(data.head(15))