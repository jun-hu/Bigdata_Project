
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

file_name= '/home/project/'+'airbnb.csv'
df_air=pd.read_csv(file_name)
x=df_air['neighborhood']
group=df_air.groupby(df_air['neighborhood'])


# In[5]:


df=pd.DataFrame()
df['reviews average']=group['reviews'].mean();
df['overall satisfaction average']=group['reviews'].mean()
df['price average']=group['price'].mean()


df.plot(subplots=True, layout=(3, 1), figsize=(6, 6), sharex=False);

