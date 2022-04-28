#!/usr/bin/env python
# coding: utf-8

# ## import libary

# In[126]:


import pandas as pd
import plotly
import plotly.graph_objs as go
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier


# In[ ]:





# In[127]:


df=pd.read_excel('721Q F-stock 050422.xlsx',sheet_name='Total stock')
df.columns


# In[128]:


#df=df.rename(columns=df.iloc[1])

df=df[['Material','Material Description','weight uni Un','Total demand EUR','Leadtime days','Unit cost EUR','Gross Weight','vendor location','demand Fluc']]


# In[129]:


df.isnull().sum()
df['Leadtime days'] = df['Leadtime days'].fillna(0)


# In[130]:


dflala=df


# In[131]:


df=df.set_index('Material')


# In[132]:


df=df.drop(columns='Material Description')


# In[133]:


# Get one hot encoding of columns B
one_hot = pd.get_dummies(df['vendor location'])
# Drop column B as it is now encoded
df = df.drop('vendor location',axis = 1)
# Join the encoded df
df = df.join(one_hot)
df


# In[134]:


# Get one hot encoding of columns B
one_hot = pd.get_dummies(df['demand Fluc'])
# Drop column B as it is now encoded
df = df.drop('demand Fluc',axis = 1)
# Join the encoded df
df = df.join(one_hot)
df


# In[ ]:





# In[135]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from sklearn.cluster import KMeans


# In[ ]:





# In[ ]:





# In[136]:


x=df.fillna(0)
transform = preprocessing.StandardScaler()
transform.fit(x)
x = transform.transform(x)


# In[ ]:





# In[137]:


X=x


# In[138]:


wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()


# In[139]:


kmeans = KMeans(n_clusters=4, init='k-means++', max_iter=300, n_init=10, random_state=0)
pred_y = kmeans.fit_predict(X)
plt.scatter(X[:,0], X[:,1])
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red')
plt.show()


# In[140]:


pred_y


# In[141]:


df.index


# In[142]:


# creating a list of index names
index_values = df.index
   
# creating a list of column names
column_values = ['cluster']
  
# creating the dataframe
dff = pd.DataFrame(data = pred_y, 
                  index = index_values, 
                  columns = column_values)
dff


# In[143]:


dff.reset_index(inplace=True)


# In[144]:


df=dff.merge(dflala, left_on="Material", right_on="Material")
df.head()


# In[179]:


df['clustershape']=df['cluster'].replace(0,"darkblue").replace(1,  "green").replace(3, "orange").replace(2, "red")

df['vendor location']= df['vendor location'].replace(0,"square").replace('local',  "circle").replace('import', "diamond").replace('new', "square")
df


# In[180]:


#Set marker properties
markersize = df['weight uni Un']/1000
markercolor = df['clustershape']
markershape = df['vendor location']


#Make Plotly figure
fig1 = go.Scatter3d(x=df['Unit cost EUR'],
                    y=df['Total demand EUR'],
                    z=df['Leadtime days'],
                    marker=dict(size=markersize,
                                color=markercolor,
                                symbol=markershape,
                                opacity=0.8,
                                reversescale=True,
                                colorscale='oranges'),
                    line=dict (width=0.02),
                    mode='markers',
                    hovertemplate='<b>%{text}</b><extra></extra>',
                    text = df[['Material','Material Description']])

#Make Plot.ly Layout
mylayout = go.Layout(scene=dict(xaxis=dict( title='cost'),
                                yaxis=dict( title='demand'),
                                zaxis=dict(title='leadtime')),
                     title="721Q inventory features 6D visualization & clustering (April data)")
                                


#Plot and save html
plotly.offline.plot({"data": [fig1],
                     "layout": mylayout},
                     auto_open=True,
                     filename=("feature.html"))


# In[ ]:





# In[ ]:




