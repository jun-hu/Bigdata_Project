
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np

file_name= '/home/project/'+'airbnb.csv'
df_air=pd.read_csv(file_name)

df_room_host=df_air.set_index(['room_id','host_id'])
columns=['room_type','borough','neighborhood','accommodates','bedrooms','price','minstay','latitude','longitude','last_modified']
df_room_host.drop(columns, inplace=True, axis=1)
df_room_host.overall_satisfaction=df_room_host.overall_satisfaction.fillna(0)
df_room_host.reviews=df_room_host.reviews.fillna(0)

df_room_host['total_score']=0.378*df_room_host['reviews']+df_room_host['overall_satisfaction']
del df_room_host['reviews']
del df_room_host['overall_satisfaction']
df_room_host1=df_room_host.sort_values(by='total_score',ascending=True)

df_room_host2=df_room_host.sort_values(by='total_score',ascending=False)
file_name="./sorted_total_score_asecend.csv"
df_room_host1.to_csv(file_name)
file_name2="./sorted_total_score_descend.csv"
df_room_host2.to_csv(file_name2)
df_room_host2


