
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np

file_name= '/home/project/'+'airbnb.csv'
df_air=pd.read_csv(file_name)

names=['0-100','100-200','200-300','300-400','400-500','500-1000','1000-5000']
group = df_air.groupby(pd.cut(df_air['price'], [0,100,200,300,400,500,1000,5000],labels=names))


# In[10]:


sort_ranged_price = pd.DataFrame()
sort_ranged_price['accommodates average'] = group['price'].mean()
sort_ranged_price['accommodates median'] = group['price'].median()
sort_ranged_price['bedrooms average'] = group['bedrooms'].mean()
sort_ranged_price['bedrooms median'] = group['bedrooms'].median()
sort_ranged_price['reviews average'] = group['reviews'].mean()
sort_ranged_price['reviews median'] = group['reviews'].median()
sort_ranged_price['neighbor list'] = group['neighborhood'].apply(list)
sort_ranged_price['length'] = group['price'].size()

file_name="./sort_ranged_price.csv"
sort_ranged_price.to_csv(file_name)

