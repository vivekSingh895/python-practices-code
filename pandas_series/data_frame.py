import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("document_pandas\customer (1).csv")
#print(df)

list = [[110,200,320],[210,20,30],[4000,1000,2400]]
data_fr = pd.DataFrame(list,columns  = ['no','id','prise'])
#print(data_fr)

details = {
    "name" : ['vivek ' ,'suraj','kalpesh' ,'niklesh'],
    "roll_no": [12,22,11,23],
    "state" :"" #['grokhpure' ,'kushinagar','jaipure','rajashthan']
}

dict_df = pd.DataFrame(details)
# print(dict_df)
# print(type(dict_df))
# print(dict_df.describe())
# print(dict_df.info())
# print("shape of data rame =>>>>\n",dict_df.shape)

# print(df)
# print("no of row and col \n",df.shape)
# print(df.info())
#print(df.sum(axis = 0))
#print(df[["age","education","gender"]])
# print(df.iloc[:,[0,2,4]].head(10))
#slicing some row and col fancy indexing
# print(df.iloc[[2,3,4,5],[0,2,4]])
# p = df.sample(30).iloc[:,0]
#p.plot(kind = "pie")
#plt.show()
#print(30 >= df.iloc[:,0].value_counts())

print(data_fr)

print(200 < data_fr.iloc[:,0].count())