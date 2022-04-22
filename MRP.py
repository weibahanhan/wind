#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# ## Demand flow analysis from PTR factories to Gen-New material (3947)

# In[2]:


#import libary 
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
import plotly.express as px

import streamlit as st

st.text(' this app is for demo share only, not real time data, not for production, contact wehan@vestas.com for any questions')


# In[55]:


@st.experimental_memo
def load_data():
    
    df = pd.read_csv('https://raw.githubusercontent.com/weibahanhan/wind/main/29193947-701b.csv')
    
    return df


dfb = load_data()


# In[56]:


@st.experimental_memo
def load_data():
    
    df = pd.read_csv('https://raw.githubusercontent.com/weibahanhan/wind/main/29193947-701v.csv')
    
    return df


dfv = load_data()


# In[57]:


@st.experimental_memo
def load_data():
    
    df = pd.read_csv('https://raw.githubusercontent.com/weibahanhan/wind/main/29193947-701w.csv')
    
    return df


dfw = load_data()


# In[ ]:





# In[ ]:





# In[ ]:





# In[58]:








dfb=dfb[['Planned dates','Rec./reqd qty']]
dfb['Rec./reqd qty']=dfb['Rec./reqd qty']*(-1)
dfb=dfb.groupby('Planned dates').sum()
dfb=dfb.reset_index()
dfv=dfv[['Planned dates','Rec./reqd qty']]
dfw=dfw[['Planned dates','Rec./reqd qty']]


# In[59]:


dfb['Planned dates']=pd.to_datetime(dfb['Planned dates'])
dfv['Planned dates']=pd.to_datetime(dfv['Planned dates'])
dfw['Planned dates']=pd.to_datetime(dfw['Planned dates'])
dfb=dfb.sort_values('Planned dates')
dfv=dfv.sort_values('Planned dates')
dfw=dfw.sort_values('Planned dates')


# In[ ]:





# In[60]:


## Plot stacked bar and line combined chart to show if supply factory meet requirement
fig = go.Figure()

fig = px.line(dfb, x="Planned dates", y="Rec./reqd qty")


fig.add_trace(
    go.Bar(
        x=dfv['Planned dates'],
        y=dfv['Rec./reqd qty'],
        name="701v",
       
        marker_color = '#ff7f0e',
        text =dfv['Rec./reqd qty']))
        
fig.add_trace(
    go.Bar(
        x=dfw['Planned dates'],
        y=dfw['Rec./reqd qty'],
        name="701w",
       
        marker_color = '#abe5f0',
        text =dfw['Rec./reqd qty'])
        )
    
    
  


fig.update_layout(
    autosize=False,
    width=1000,
    height=500,title="Requirements flow from PTRs to Gen",
    )

fig.update_layout(barmode='stack')
fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)

fig.show()
#st.plotly_chart(fig, use_container_width=True)


# #### Business Insights: From chart we could see the requirement flow for new material(3947) is pretty correct. supply factory see 1 day earlier due to 1 day transportation leadtime set up. Reminder: There is no GR process date set up this moment.

# In[ ]:





# In[61]:


#!jupyter nbconvert --to script MRP.ipynb


# In[ ]:





# In[ ]:





# In[ ]:




