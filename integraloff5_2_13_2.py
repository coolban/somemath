import numpy as np
from decimal import *

getcontext().prec = 28
n=101
x1=0.0
x2=2.0
an=np.linspace(x1,x2,n,dtype=np.dtype(Decimal))
print an
an1=an[1:]
print an1
y = (an1)/((an1)+1)
print sum(y)*(x2-x1)/(n-1)
an2=an[0:-1]
print an2
y2 = (an2)/(an2+1)
print sum(y2)*(x2-x1)/(n-1)
