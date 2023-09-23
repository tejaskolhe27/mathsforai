import numpy as np
from numpy import linalg as la

x= np.array([2,5,7,8])
y = np.array([9,7,5,2])
data = np.stack((x,y),axis=0)
np.cov(data,ddof=0)

print("The variance-covariance matrix is: \n",np.cov(data,ddof=0))



x= np.array([2,5,7,8])
y = np.array([3,10,18,24])
data = np.stack((x,y),axis=0)
np.cov(data,ddof=0)

print("The variance-covariance matrix is: \n",np.cov(data,ddof=0))
