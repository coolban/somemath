# -*- coding: utf-8 -*-
'''
这段代码将做出函数f(x)=x*x-4*x+2在[1,4]之间的图像，并描画出在该曲线下面的近似矩形

'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
x = np.linspace(1,4,1000)
y = x*x-4*x+2
fig = plt.figure(figsize=(8,4))
plt.plot(x,y,label='x*x-4*x+2',color='red',linewidth=2)
plt.show()
