import numpy as np

n=30000000
an=np.linspace(0,2,n)
an=an[1:]
y = 2.0/n*(an)*(an)*(an)*(an)*(an)
print sum(y)
