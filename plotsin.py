# -*- coding: utf-8 -*-
'''
这段代码将做出函数f(x)=sin(x)在[0,pi*3/2]之间的图像，并描画出在该曲线下面的近似矩形

'''
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
num = 6
x = np.linspace(0,np.pi*3/2,1000)
y = np.sin(x)
fig = plt.figure(figsize=(8,4))
x1 = np.linspace(0,np.pi*3/2,num+1)
width=np.pi*3/num/2
ax1 = fig.add_subplot(111,aspect='equal')
for xn in range(num):
    ax1.add_patch(patches.Rectangle((x1[xn],0),width,math.sin(x1[xn]+(np.pi/8))))
plt.plot(x,y,label='sin(x)',color='red',linewidth=2)
plt.show()
