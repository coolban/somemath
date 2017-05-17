import numpy as np

n=100
x1=-1.0
x2=0.0
an=np.linspace(x1,x2,n+1)
#print an
an1=an[1:]
#print an1
y = np.power(np.e,-(an1*an1))
print sum(y)*(x2-x1)/n
an2=an[0:-1]
#print an2
y2 = np.power(np.e,-(an2*an2))
print sum(y2)*(x2-x1)/n
