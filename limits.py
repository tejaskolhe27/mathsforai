import numpy as np
import sympy as sp
from sympy import limit,pprint
from sympy.abc import x

expression= ((x**2)+x-12)/(x-3)
result= limit(expression,x,3)
print("Expression is: ")
pprint(expression)
print("Limit at x->3 is: ",result)