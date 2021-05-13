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

#
L = np.random.random(100)
print(np.sum(L))
print(np.min(L))
print(np.max(L))
print(np.mean(L))
print(np.std(L))
print(np.var(L))
print(np.percentile(L,25))
print(np.median(L))

M = np.random.random((3,4))
print(M.sum())
print(M.min(axis=0))



