import pandas as pd 
import numpy as np

df_fram = pd.read_csv("document_pandas\customer (1).csv")
#print(df_fram)
new = df_fram[(df_fram["gender"] == 'Male') & ((df_fram["education"] == "UG") | (df_fram["education"] == ("School")))]
#print(new)
goodStudent = df_fram[df_fram['review'] == 'Good']
print(goodStudent)