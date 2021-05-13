import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('classic')

x = np.linspace(0,10,100)
# fig = plt.figure()
# plt.plot(x,np.sin(x),'-')
# plt.plot(x,np.cos(x),'--')
#
# plt.show()
#
# 保存图片 ==============================
# fig.savefig('my_figure.png')
# from Ipython.display import Image
# Image('my_figure.png')

# 面向对象绘图 ==========================
# fig, ax = plt.subplots(2)
# ax[0].plot(x, np.sin(x))
# ax[1].plot(x, np.cos(x))
#
# fig = plt.figure()
# ax = plt.axes()
#
#
#
# x = np.linspace(0,10,1000)
# ax.plot(x,np.sin(x),color='red',linestyle='solid',label='sin(x)')
# ax.plot(x,np.cos(x),color='#FFDD44',linestyle='dashed',label='cos(x)')
# # solid-, dashed--, dashdot-., dotted:
# ax.plot(x,np.sin(x+1),"-.k")
# # -g, --c, -.k, :r
#
# # ax.set(xlim=(0,10),ylim=(-2,2),xlabel='x',ylabel='sin(x)',title='A Simple Plot')
#
# plt.axis([-1,11,-1.5,1.5])
# plt.axis('tight')
# plt.axis('equal')
#
# plt.title("A Sine Curve")
# plt.xlabel('x')
# #plt.ylabel('sin(x)')
#
# plt.legend(loc='upper left',frameon=False, ncol=2,fancybox=True,framealpha=1,shadow=True,borderpad=1)
#
# plt.show()

# 散点图 ========================================
# x = np.linspace(0,10,30)
# y = np.sin(x)
# # plt.plot(x,y,'o',color='black')
# plt.plot(x+1,y,'-or')
# plt.plot(x,y,'-p',color='gray',
#          markersize = 15, linewidth=4,
#          markerfacecolor='white',
#          markeredgecolor='gray',
#          markeredgewidth=2)
# # o.,x+v^<>sd
#
# plt.show()
#
# rng=np.random.RandomState(0)
# x=rng.randn(100)
# y=rng.randn(100)
# colors=rng.randn(100)
# sizes=1000*rng.rand(100)
# plt.scatter(x,y,c=colors,s=sizes,alpha=0.3,cmap='viridis') #alpha:透明度,cmap:配色方案
# plt.colorbar()
#
# plt.show()

# 误差线 ======================================================
# x = np.linspace(0,10,50)
# dy = 0.8
# y =np.sin(x)+dy*np.random.randn(50)
# plt.errorbar(x,y,yerr=dy,fmt='o',color='black',ecolor='lightgray',elinewidth=3,capsize=0)
# plt.show()

# 等高线 ======================================================
def f(x,y):
    return np.sin(x) ** 10 + np.cos(10+y*x)*np.cos(x)
x = np.linspace(0,5,50)
y = np.linspace(0,5,40)
X,Y = np.meshgrid(x,y)
Z = f(X,Y)
# plt.contour(X,Y,Z,20,cmap='RdGy')
# plt.contourf(X,Y,Z,20,cmap='viridis')
# plt.colorbar()

# plt.imshow(Z,extent=[0,5,0,5],origin='lower',cmap='RdGy')
# plt.colorbar()

# contours = plt.contour(X,Y,Z,3,colors='black')
# plt.clabel(contours,inline=True,fontsize=8)
# plt.imshow(Z,extent=[0,5,0,5],origin='lower',cmap='RdGy',alpha=0.5)
# plt.colorbar()
#
# plt.show()

# 统计图 =======================================
# x1 = np.random.normal(0,0.8,1000)
# x2 = np.random.normal(-2,1,1000)
# x3 = np.random.normal(3,2,1000)
#
# kwargs = dict(histtype='stepfilled', alpha=0.3, density=True, bins=40)
#
# plt.hist(x1,**kwargs)# 频次直方图
# plt.hist(x2,**kwargs)
# plt.hist(x3,**kwargs)
# plt.show()

mean = [0,0]
cov=[[1,1],[1,2]]
x,y=np.random.multivariate_normal(mean,cov,10000).T

# plt.hist2d(x,y,bins=30,cmap='Blues')
# cb=plt.colorbar()
# cb.set_label('counts in bin')

# plt.hexbin(x,y,gridsize=30,cmap='Blues')
# cb = plt.colorbar(label='count in bin')

from scipy.stats import gaussian_kde
# 拟合数组精度
data = np.vstack([x,y])
kde = gaussian_kde(data)
# 用一对规则的网格数据进行拟合
xgrid = np.linspace(-3.5,3.5,40)
ygrid = np.linspace(-6,6,40)
Xgrid,Ygrid=np.meshgrid(xgrid,ygrid)
Z = kde.evaluate(np.vstack([Xgrid.ravel(),Ygrid.ravel()]))
# 画出结果图
plt.imshow(Z.reshape(Xgrid.shape),
           origin='lower',aspect='auto',
           extent=[-3.5,3.5,-6,6],
           cmap='Blues')
cb=plt.colorbar()
cb.set_label('density')

plt.show()




# x,y = np.meshgrid(np.linspace(0,10,10),np.linspace(-3,3,12))
# u = 1
# v = -np.power(y,3)+np.cos(5*x)
#
# plt.quiver(x,y,u,v)
# plt.show()
