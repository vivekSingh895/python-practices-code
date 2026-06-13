import pandas as pd
import numpy as np

new = pd.read_csv("document_pandas\gayle-175.csv",index_col = "batsman_runs")
series = new.loc[:,"batsman"].copy()
#print(series)
series.sort_values(inplace=True,ascending=False)
#print(series)
# print(type(series))
# print("max ",max(series))
# print("min ",min(series))

virat = pd.read_csv("document_pandas\\vk.csv",index_col = "match_id")
virat_seri = virat.loc[:,"batsman_runs"].copy()
virat_seri.sort_values(inplace=True)
print(virat_seri)
print("size of series",virat_seri.size)
print("values counts \n",virat_seri.value_counts())
index = virat_seri[(50 <= virat_seri) & (100 >= virat_seri)]
print("boolean value return after remove square bracket \n",index)
print("number of item ",index.size)
print("top 25 item print\n",index.head(25))
#print("all function and attribute in pandas \n",dir(index))
print("aggeration \n",index.agg(["min","max"]))
print("all about the series \n",index.describe())

