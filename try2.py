#!/usr/bin/env python
# coding: utf-8

# # Winning planning Ex-In factories 
#                      ----Han Wei April 2022
# 

# In[ ]:





# ## Backgroud introduction
# 
# supply factory: Generator(701b)
# demand factory: Winergy(701w)
# demand factory2: ZF (701z)
# Product:vidar gen
# 
# problems: demand not stable due to covid, NCR, material shortage, supplying factory not flexible to cope with it considering current set up
# constrains: 
# 1. stock space : 15+10+10
# 2. gen weekly capacity: 10
# 3. totol pallet in scope: 37
# 

# In[ ]:





# In[ ]:





# In[4]:


import plotly.graph_objects as go

import pandas as pd
from datetime import datetime
import plotly.express as px


#filepath = r'C:\\...\\Worksheet.xlsx'
df = pd.read_excel('https://github.com/weibahanhan/wind/blob/main/dt.xlsx')


df.head(2)


# In[2]:


#!pip install plotly


# In[ ]:





# In[ ]:





# ## Generator(701b) capacity & output & demand 

# In[3]:


## osp gen need shift 1 wk data!


# In[4]:


fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=df['Date'],
        y=df['osp gen'],
        name="osp gen"
        ))

fig.add_trace(
    go.Scatter(
        x=df['Date'],
        y=df['gen capacity'],
        name="gen capacity"
        ))



fig.add_trace(
    go.Bar(
        x=df['Date'],
        y=df["osp win"],
        name="osp win",
       
        marker_color = '#ff7f0e',
        text = df["osp win"] ))
        
fig.add_trace(
    go.Bar(
        x=df['Date'],
        y=df["osp zf"],
        name="osp zf",
       
        marker_color = '#abe5f0',
        text = df["osp zf"]
        ))   
    
    


fig.update_layout(
    autosize=False,
    width=1000,
    height=500,title="Generator(701b) capacity & output & demand")

fig.update_layout(barmode='stack')
fig.show()


# ### Bussiness recommendations:

# #### suggest set up a regular meeting to align the qty. of next week and following 4 weeks , at the very beginning need a call, later only email message is ok

# In[ ]:





# In[ ]:





# In[ ]:



              


# ## Gen stock weekly candle and stock limit

# In[5]:


fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=df['Date'],
        y=df['stock limit'],
        name="stock limit"
        ))
fig.add_trace(
    go.Candlestick(
        x=df['Date'],
        open=df['open'],
        high=df['high'],
        low=df['low'],
        close=df['close']
        
    ))

fig.update_layout(
    autosize=False,
    width=1000,
    height=500,title="Gen stock weekly candle and stock limit")
fig.show()


# In[ ]:





# In[6]:


### Findings:


# In[ ]:





# ### business recommendations:

# In[7]:


#### once the high value is above the limitation, need prevent action like find temperate space 


# In[ ]:



