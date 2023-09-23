import numpy as np
from numpy import linalg as la
import pandas as pd

milk = pd.read_csv("milk.csv",index_col=0)
print(milk,"\n")

print("Variance-covariance matrix is: \n", milk.cov(ddof=0))

sigma=milk.cov(ddof=0)
values,vectors=la.eig(sigma)
print("Eigen values are: \n",values)
print("Eigen vectors are: \n",vectors)

pca_scores=np.matmul(milk,vectors)
print(pca_scores.var(ddof=0))


print(pca_scores.cov(ddof=0))
