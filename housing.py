#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from numpy import linalg as la


# In[2]:


df = pd.read_csv("Housing.csv")
df


# In[3]:


x1=df['lotsize']
#x2=df['lotsize']
y1=df['price']

n=len(x1)
sx1 = np.sum(x1)
sy1 = np.sum(y1)
sx11 = np.sum(x1*x1)

sx1y = np.sum(x1*y1)

A = np.array([[n,sx1],[sx1,sx11]])
B=np.array([sy1,sx1y])

soln = la.solve(A,B)
print("Solution is\nb0= ",soln[0])
print("b1= ",soln[1])

ycap = soln[0]+soln[1]*x1
print("Z = ",np.sum((y1-ycap)**2))


# In[4]:


dum_house = pd.get_dummies(df)
dum_house


# In[5]:


x1=df['lotsize']
y= df['price']
x2=dum_house['driveway_no']

n=len(x1)
sx1 = np.sum(x1)
sx2 = np.sum(x2)
sy = np.sum(y)
sx11 = np.sum(x1*x1)
sx12 = np.sum(x1*x2)
sx22 = np.sum(x2*x2)
sx1y = np.sum(x1*y)
sx2y = np.sum(x2*y)
A = np.array([[n,sx1,sx2],[sx1,sx11,sx12],[sx2,sx12,sx22]])
B=np.array([sy,sx1y,sx2y])

soln = la.solve(A,B)
print("Solution is\nb0= ",soln[0])
print("b1= ",soln[1])
print("b2= ",soln[2])

ycap = soln[0]+soln[1]*x1+soln[2]*x2
print("Z = ",np.sum((y-ycap)**2))


# In[6]:


x1=dum_house['lotsize']
y= dum_house['price']
x2=dum_house['driveway_no']
x3 =dum_house['bedrooms']

n=len(x1)
sx1 = np.sum(x1)
sx2 = np.sum(x2)
sx3=np.sum(x3)
sy = np.sum(y)
sx11 = np.sum(x1*x1)
sx12 = np.sum(x1*x2)
sx13= np.sum(x1*x3)
sx22 = np.sum(x2*x2)
sx33 = np.sum(x3*x3)
sx23 = np.sum(x2*x3)
sx3y = np.sum(x3*y)
sx1y = np.sum(x1*y)
sx2y = np.sum(x2*y)
A = np.array([[n,sx1,sx2,sx3],[sx1,sx11,sx12,sx13],[sx2,sx12,sx22,sx23],[sx3,sx13,sx23,sx33]])
B=np.array([sy,sx1y,sx2y,sx3y])

soln = la.solve(A,B)
print("Solution is\nb0= ",soln[0])
print("b1= ",soln[1])
print("b2= ",soln[2])
print("b3= ",soln[3])

ycap = soln[0]+soln[1]*x1+soln[2]*x2+soln[3]*x3
print("Z = ",np.sum((y-ycap)**2))


# ## sklearn

# In[7]:


from sklearn.linear_model import LinearRegression

x=dum_house[['lotsize','driveway_no','bedrooms']]
y= dum_house['price']

lr = LinearRegression()
lr.fit(x,y)
print("Intercept = ",lr.intercept_)
print("Coefficient  =",lr.coef_)


# In[ ]:




