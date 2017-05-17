# -*- coding: utf-8 -*-
'''
这段代码将做出函数f(x)=x*x+x在[-2,0]之间的图像，并描画出在该曲线下面的近似矩形

'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
x = np.linspace(-2,0,1000)
y = x*x+x
fig = plt.figure(figsize=(8,4))
plt.plot(x,y,label='x*x+x',color='red',linewidth=2)
plt.show()
