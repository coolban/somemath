import numpy as np

n=30000000
an=np.linspace(0,2,n)
an=an[1:]
y = 2.0/n*np.power(np.e,-an)
print sum(y)
