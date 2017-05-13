import numpy as np

n=30000000
x1=0
x2=np.pi/2
an=np.linspace(x1,x2,n)
an=an[1:]
y = (x2-x1)/(n-1)*np.cos(an)
print sum(y)
