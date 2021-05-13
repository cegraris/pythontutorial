import numpy as np

# 创建 ===============================================
# print(np.array([1,4,2,5,3]))
# print(np.array([3.14,4,2,3]))
# print(np.array([1,2,3,4],dtype='float32'))
# print(np.array([range(i,i+3) for i in [2,4,6]]))
# print(np.zeros(10, dtype=int))
# print(np.ones((3,5),dtype=float))
# print(np.full((3,5),3.14))
# print(np.arange(0,20,2))
# print(np.linspace(0,1,5))
# print(np.random.random((3,3)))
# print(np.random.normal(0,1,(3,3)))
# print(np.random.randint(0,10,(3,3)))
# print(np.eye(3))
# print(np.empty(3))

# 数组属性 ===========================================
# np.random.seed(0)
# x1 = np.random.randint(10,size=6)
# x2 = np.random.randint(10,size=(3,4))
# x3 = np.random.randint(10,size=(3,4,5))
# print(x3.ndim) # 维度个数
# print(x3.shape) # 每个维度大小
# print(x3.size) # 总元素个数
# print(x3.dtype) # 元素类型
# print(x3.itemsize) # 一个元素大小
# print(x3.nbytes) # 总大小

# 获取元素 ===========================================
# np.random.seed(0)
# x1 = np.random.randint(10,size=6)
# x2 = np.random.randint(10,size=(3,4))
# x3 = np.random.randint(10,size=(3,4,5))
# print(x1)
# print(x1[0])
# print(x1[-1])
# print(x2)
# x2[0,0] = 12
# print(x2[0,0])
#
# x = np.arange(10)
# print(x[:5])
# print(x[5:])
# print(x[::2])
# print(x[::-1])
# print(x2[:2,:3])
# print(x2[:3,::2])
# print(x2[::-1,::-1])
# print(x2[:,0])
# print(x2[0,:])
# print(x2[0])
#
# x2_sub_copy = x2[:2,:2].copy()
# print(x2_sub_copy)

# 变形 ========================================================
# print(np.arange(1,10).reshape(3,3))
# x = np.array([1,2,3])
# print(x.reshape((1,3)))
# print(x[np.newaxis,:])
# print(x.reshape((3,1)))
# print(x[:,np.newaxis])

# 拼接与分裂 ===================================================
# x = np.array([1,2,3])
# y = np.array([3,2,1])
# z = np.array([99,99,99])
# print(np.concatenate([x,y,z]))
# grid = np.array([[1,2,3],
#                  [4,5,6]])
# print(np.concatenate([grid,grid]))
# print(np.concatenate([grid,grid],axis=1))
#
# x = np.array([1,2,3])
# grid = np.array([[9,8,7],
#                 [6,5,4]])
# print(np.vstack([x,grid]))
# y = np.array([[99],
#               [99]])
# print(np.hstack([grid,y]))
#
# x = [1,2,3,99,99,3,2,1]
# x1,x2,x3=np.split(x,[3,5])
# print(x1,x2,x3)
# grid = np.arange(16).reshape((4,4))
# upper, lower = np.vsplit(grid,[2])
# print(upper)
# print(lower)
#
# left, right = np.hsplit(grid,[2])
# print(left)
# print(right)

# 函数 ===============================================
# values = np.random.randint(1,10,size=5)
# print(values)
# print(1.0/values)
# print(np.arange(5) / np.arange(1,6))
# x = np.arange(9).reshape(3,3)
# print(2**x)
# x = np.arange(4)
# print(x)
# print(x+4)
# print(x*2)
# print(x/2)
# print(x//2)
# print(-x)
# print(x**2)
# print(x%2)
# print(0.5*x+1)
# print(np.abs(x))
# c = np.array([3-4j,4-3j,2+0j,0+1j])
# print(np.abs(c))
#
# theta = np.linspace(0,np.pi,3)
# print(np.sin(theta))
# print(np.cos(theta))
# print(np.tan(theta))
# x = [-1,0,1]
# print(np.arcsin(x))
# print(np.arccos(x))
# print(np.arctan(x))
#
# x = [1,2,3]
# print(np.exp(x)) # e^x
# print(np.exp2(x)) # 2^x
# print(np.power(3,x)) # 3^x
# print(np.expm1(x)) # x为小数时更精确
#
# print(np.log(x))
# print(np.log2(x))
# print(np.log10(x))
# print(np.log1p(x)) # x为小数时更精确
#
# from scipy import special # scipy 提供了更多高级函数
# print(special.gamma(x))
#
# x = np.arange(5)
# y = np.empty(5)
# np.multiply(x,10,out=y) # 指定输出
# print(y)
#
# y = np.zeros(10)
# np.power(2,x,out=y[::2]) # 指定输出
# print(y)
#
# x = np.arange(1,6)
# print(np.add.reduce(x)) # 聚合
# print(np.multiply.reduce(x))
# print(np.add.accumulate(x)) # 记录每步聚合结果
#
# x = np.arange(1,6)
# print(np.multiply.outer(x,x)) # 外积(笛卡尔乘法)

# 统计值 ===============================================
# L = np.random.random(100)
# print(np.sum(L))
# print(np.min(L))
# print(np.max(L))
# print(np.mean(L))
# print(np.std(L))
# print(np.var(L))
# print(np.percentile(L,25))
# print(np.median(L))
#
# M = np.random.random((3,4))
# print(M.sum())
# print(M.min(axis=0))

# 广播 ===========================================
# a = np.array([0,1,2])
# b = np.array([5,5,5])
# print(a + b)
# print(a + 5)
# M = np.ones((3,3))
# print(M+a)
#
# a = np.arange(1,7)
# b = np.arange(1,7)[:,np.newaxis]
# print(a)
# print(b)
# print(a+b)
#
# x = np.random.random((10,3))
# print(x)
# Xmean = x.mean(0)
# print(Xmean)
# x_centered = x - Xmean # 广播
# print(x_centered)

# 比较，掩码，布尔逻辑 =======================
# x = np.array([1,2,3,4,5])
# print(x<3)
# print(x == 3)
# print((2*x)==(x**2))
#
# rng = np.random.RandomState(0)
# x = rng.randint(10, size=(3,4))
# print(x)
# print(np.count_nonzero(x<6))
# print(np.sum(x<6))
# print(np.sum(x<6,axis=1))
#
# print(np.any(x>8))
# print(np.all(x<10))
# print(np.all(x<8,axis=1))
# print((x>3)&(x<6))
# print(np.sum((x>3)&(x<6))) # &与 |或 ^异或 ~非
#
# print(x[x<5]) # 掩码操作

# 花哨索引
# rand = np.random.RandomState(42)
# x = rand.randint(100,size=10)
# print(x)
#
# print([x[3],x[7],x[2]])
# ind = [3,7,4]
# print(x[ind])
# ind = np.array([[3,7],
#                 [4,5]])
# print(x[ind])
#
# x = np.arange(12).reshape((3,4))
# print(x)
# row = np.array([0,1,2])
# col = np.array([2,1,3])
# print(x[row,col])
# print(x[row[:,np.newaxis],col])
#
# print(x[2,[2,0,1]])
# print(x[1:,[2,0,1]])
# mask = np.array([1,0,1,0],dtype=bool)
# print(x)
# print(row[:,np.newaxis])
# print(mask)
# print(x[row[:,np.newaxis],mask])

# 排序 =====================================
# x = np.array([2,1,4,3,6])
# print(np.sort(x))
# x.sort()
# print(x)
# x = np.array([2,1,4,3,6])
# i = np.argsort(x)
# print(i)
#
# rand = np.random.RandomState(42)
# X = rand.randint(0,10,(4,6))
# print(x)
# print(np.sort(X,axis=0)) # 对每一列排序
# print(np.sort(X,axis=1)) # 对每一行排序
#
# x = np.array([7,2,3,1,6,5,4])
# print(np.partition(x,3)) # 分隔
# print(np.partition(X,2,axis=1))
#
# X = rand.rand(10,2)
# print(X)
# print(X[:,np.newaxis,:].shape)
# print(X[np.newaxis,:,:].shape)

x = 1
t = 3
for i in range(100):
    y = -x + np.exp(-0.001*t)*np.sin((np.pi/4)*t)
    print('======%s=======' % i)
    print(y,end='<<<y \n')
    x = x + y
    t = t + y
    print(x,end='<<<x \n')
    print(t,end='<<<t \n')