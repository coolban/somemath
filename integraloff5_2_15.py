import numpy as np

n=100
x1=0.0
x2=np.pi
an=np.linspace(x1,x2,n+1)
#print an
an1=an[1:]
#print an1
y = np.sin(an1)
print sum(y)*(x2-x1)/n
#an2=an[0:-1]
#print an2
#y2 = (an2)/(an2+1)
#print sum(y2)*(x2-x1)/n
