# -*- coding: utf-8 -*-
'''
这段代码将做出函数f(x)=x^2-2x在[0,3]之间的图像，并描画出在该曲线下面的近似矩形

'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
num = 6
x = np.linspace(0,3,1000)
y = x*x-2*x
fig = plt.figure(figsize=(8,4))
x1 = np.linspace(0,3,num+1)
width=3.0/num
ax1 = fig.add_subplot(111,aspect='equal')
for xn in range(num):
    ax1.add_patch(patches.Rectangle((x1[xn],0),width,x1[xn+1]*x1[xn+1]-2*x1[xn+1]))
plt.plot(x,y,label='x^2-2x',color='red',linewidth=2)
plt.show()
