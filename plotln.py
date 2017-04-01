# -*- coding: utf-8 -*-
'''
这段代码将做出函数f(x)=1/(x^2+1)在[0,1]之间的图像，并描画出在该曲线下面的近似矩形

'''
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
num = 10
x = np.linspace(1,4,1000)
y = np.log(x)
fig = plt.figure(figsize=(8,4))
x1 = np.linspace(1,4,num+1)
width=3.0/num
ax1 = fig.add_subplot(111,aspect='equal')
for xn in range(num):
    ax1.add_patch(patches.Rectangle((x1[xn],0),width,np.log(x1[xn])))
plt.plot(x,y,label='ln(x)',color='red',linewidth=2)
plt.show()
