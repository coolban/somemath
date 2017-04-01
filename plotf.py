# -*- coding: utf-8 -*-
'''
这段代码将做出函数f(x)=1/(x^2+1)在[0,1]之间的图像，并描画出在该曲线下面的近似矩形

'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
num = 50
x = np.linspace(0,1,1000)
y = 1/(x*x+1)
fig = plt.figure(figsize=(8,4))
x1 = np.linspace(0,1,num+1)
width=1.0/num
ax1 = fig.add_subplot(111,aspect='equal')
for xn in range(num):
    ax1.add_patch(patches.Rectangle((x1[xn],0),width,1/(x1[xn+1]*x1[xn+1]+1)))
plt.plot(x,y,label='1/(x*x+1)',color='red',linewidth=2)
plt.show()


def rms(f,n,start,end):
	piece = (end - start)*1.0/n
	s = 0
	x = start
	for i in range(n):
		x = x + piece
		s = s + f(x)
	return s * piece

def lms(f,n,start,end):
	piece = (end - start)*1.0/n
	s = 0
	x = start
	for i in range(n):
		s = s + f(x)
		x = x +piece
	return s * piece
