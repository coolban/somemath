# -*- coding: utf-8 -*-
'''
这段代码将做出函数f(x)=1/(x^2+1)在[0,1]之间的图像，并描画出在该曲线下面的近似矩形

'''
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
num = 50
x = np.linspace(0,np.pi/2,1000)
y = np.cos(x)
fig = plt.figure(figsize=(8,4))
x1 = np.linspace(0,np.pi/2,num+1)
width=np.pi/num/2
ax1 = fig.add_subplot(111,aspect='equal')
for xn in range(num):
    ax1.add_patch(patches.Rectangle((x1[xn],0),width,math.cos(x1[xn])))
plt.plot(x,y,label='1/(x*x+1)',color='red',linewidth=2)
plt.show()
