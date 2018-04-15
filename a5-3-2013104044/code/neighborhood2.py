
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np

file_name= '/home/project/'+'airbnb.csv'
df_air=pd.read_csv(file_name)

group=df_air.groupby(df_air['neighborhood'])
df=pd.DataFrame()
df['avg of reviews']=group['reviews'].mean()
df['avg of overall_satisfaction']=group['overall_satisfaction'].mean()
df['avg of price']=group['price'].mean()
df['max of reviews']=group['reviews'].max()
df['min of reviews']=group['reviews'].min()
df['max of price']=group['price'].max()
df['min of price']=group['price'].min()
df=df.sort_index()

file_name="./sorted_neighborhood_factors.csv"
df.to_csv(file_name)

