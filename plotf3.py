# -*- coding: utf-8 -*-
'''
这段代码将做出函数f(x)=e^2-2在[0,2]之间的图像，并描画出在该曲线下面的近似矩形

'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math
num = 4
x = np.linspace(0,2,1000)
y = np.power(np.e,x)-2
fig = plt.figure(figsize=(8,8))
x1 = np.linspace(0,2,num+1)
width=2.0/num
ax1 = fig.add_subplot(111,aspect='equal')
for xn in range(num):
    ax1.add_patch(patches.Rectangle((x1[xn],0),width,np.power(np.e,x1[xn]+0.25)-2))
plt.plot(x,y,label='e^2-2',color='red',linewidth=2)
plt.show()
