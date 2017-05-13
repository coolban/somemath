# -*- coding: utf-8 -*-
'''
这段代码将做出函数f(x)=x/(x+1)在[0,2]之间的图像，并描画出在该曲线下面的近似矩形

'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math
num = 5
x = np.linspace(0,2,1000)
y = x/(x+1)
fig = plt.figure(figsize=(8,8))
x1 = np.linspace(0,2,num+1)
width=2.0/num
ax1 = fig.add_subplot(111,aspect='equal')
for xn in range(num):
    ax1.add_patch(patches.Rectangle((x1[xn],0),width,(x1[xn+1])/(x1[xn+1]+1)))
plt.plot(x,y,label='x/(x+1)',color='red',linewidth=2)
plt.show()
