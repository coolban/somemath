import numpy as np

n=100
x1=0.0
x2=2.0
an=np.linspace(x1,x2,n)
an=an[0:-1]
y = (x2-x1)/n*(an+(x2-x1)/(n-1)/2)/(an+(x2-x1)/(n-1)/2+1)
print sum(y)
