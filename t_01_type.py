import math
import random
import re
import decimal
from decimal import Decimal
from fractions import Fraction
import pickle
import struct

# Number======================================================
# print(type(1234),type(3.1415),type(3+4j),type(3e-10),type(3.14E10),type(4.0e+5))
# print(type(0xF),type(0XF),type(0o7),type(0O7),type(0b1),type(0B1))
# c = 123
# print(hex(c),oct(c),bin(c))
# print(int('64'),int('100',8),int('40',16),int('1000000',2))
# X = 99
# print(X.bit_length())
# print(123+222, sum((1,2,3,4)))
# print(1.5*4)
# print(2**100, pow(2,100))
# print(abs(-42.0),min(3,1,2,4),max(3,1,2,4))
# b = 2+3, 3+4 # 元祖
# print(b)
# print(repr(1/3))
# print(1/3)
# print(1j * 1j)
# print(2 + 1j * 3)
# print((2 + 1j) * 3)
# print(math.pi)
# print(math.sqrt(85),math.sin(math.pi/2))
# print(math.floor(2.5)) # 向下取整
# print(math.floor(-2.5))
# print(math.trunc(2.5)) # 整数截断
# print(math.trunc(-2.5))
# print(round(2.567),round(2.567,2))
# print(random.random())
# print(random.randint(1,10))
# print(random.choice([1,2,3,4]))
# print(0.1+0.1+0.1-0.3)
# print(Decimal('0.1') +Decimal('0.1') +Decimal('0.1') - Decimal('0.3'))
# print(decimal.Decimal(1) / decimal.Decimal(7))
# decimal.getcontext().prec = 4
# print(decimal.Decimal(1) / decimal.Decimal(7))

# string =====================================================
# S = 'Spam'
# print(type(S))
# print(len(S))
# print(S[1])
# print(S[-1])
# print(S[1:3])
# print(S[1:])
# print(S[:-1])
# print(S[:])
# print(S+'xyz')
# print(S*8)
# L = list(S)
# print(L)
# L = ''.join(L)
# print(L)
# print('|'.join(['eggs','sausage','ham','toast']))
# print(S.find('pa'))
# print('pa' in S)
# print(S.replace('pa','XYZ'))
# print('aa$bb$cc$dd'.replace('$', 'SPAM'))
# print('aa$bb$cc$dd'.replace('$', 'SPAM', 1))
# line = 'aaa,bbb,ccccc,dd'
# print(line.split(','))
# print(S.upper())
# print(S.isalpha())
# print(S.isdigit())
# print(S.endswith('am'))
# print(S.startswith('Sp'))
# line = 'aaa,bbb,ccccc,dd\n'
# print(line.rstrip()) # 删除行末空格
# print('---')
# print('That is %d %s bird!'%(1,'dead') )
# print('That is {0} {1} bird!'.format(1,'dead'))
# print('{motto},{0} and {food}'.format('ham', motto='spam', food='eggs'))
# x = 1234
# print('integers: ...%d...%-6d...%+6d...%06d'%(x,x,x,x))
# x = 1.23456789
# print('%e | %f | %g'%(x,x,x))
# print('%-6.2f | %05.2f | %+06.1f'%(x,x,x))
# print('%f, %.2f, %.*f' % (1/3.0, 1/3.0, 4, 1/3.0))
# print('%(n)d %(x)s' % {'n':1, 'x':'spam'})
# print('{0:10} = {0:10}'.format('spam', 123.4567))
# print('{0:>10} = {0:<10}'.format('spam', 123.4567))
# print('{0:e}, {1:.3e}, {2:g}'.format(3.14159,3.14159,3.14159))
# print('{0:f},{1:.2f},{2:06.2f}'.format(3.14159,3.14159,3.14159))
# print('{0:X},{1:0},{2:b}'.format(255,255,255))
# print('{0:.{1}f}'.format(1/3.0, 4))
# print(format(1.2345, '.2f'))
# food = 'spam'
# age = 40
# print(vars())
# print(dir(S))
# print(help(S.replace))
# print(help(str))
# S = 'A\nB\tC'
# print(S)
# print(len(S))
# print(ord('\n')) # ASCII
# print(chr(115))
# print('A\0B\0C')
# print(r'C:\new\text.dat') # 关闭转义
# print("""aaaaa
# bbb'''bbbbb""bbbbbb'bbbb
# CCCCCCCCC""")
# S = 'abcdefghijklmnop'
# print(S[1:10])
# print(S[slice(1,3)])
# print(S[1:10:2])
# print(S[slice(None,None,-1)])
# match = re.match('Hello[ \t]*(.*)world','Hello  Python world')
# print(match.group(1))
# match = re.match('/(.*)/(.*)/(.*)','/usr/home/lumberjack')
# print(match.groups())


# list ==============================================
# L = [123,'spam',1.23]
# L2 = L[:] #copy
# print(len(L))
# print(L[0])
# print(L[:-1])
# print(L + [4, 5, 6])
# print(L)
# L[1:2]=[4,5]
# print(L)
# L[1:2]=[]
# del L[1]
# print(L)
# print(L.append('NI'))
# print(L.extend([7,8])
# print(L.pop(2))
# print(L)
# L.insert(2,'add2')
# print(L)
# L.remove('add2')
# print(L)
# print(list(map(abs,[-1,-2,0,1,2])))
# M = ['bb','aa','cc']
# M.sort()
# print(M)
# M.sort(key=str.lower)
# print(M)
# M.sort(key=str.lower,reverse=True)
# print(M)
# M.reverse()
# print(M)
# M = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# print(M[1])
# print(M[1][2])
# print([row[1] for row in M])
# print([row[1]+1 for row in M])
# print([row[1] for row in M if row[1] % 2 ==0])
# print([M[i][i] for i in [0, 1, 2]])
# print([c * 2 for c in 'spam'])
# G = (sum(row) for row in M)
# print(next(G))
# print(next(G))
# print(list(map(sum,M)))
# print({sum(row) for row in M}) #集合
# print({i : sum(M[i]) for i in range(3)}) #字典
# print(list(zip(['a','b','c'],[1,2,3])))

# dictionary ============================================
# D = {'food': 'Spam','quantity': 4, 'color': 'pink'}
# D2 = D.copy() # copy
# import copy
# D3 = copy.deepcopy(D) # deep copy
# print(D['food'])
# D['quantity'] += 1
# print(D)
# D = {}
# D['name'] = 'Bob'
# D['job'] = 'dev'
# D['age'] = 40
# print(D)
# D['age'] = 30
# print(D)
# print(dict(name='mel',age=45))
# print(dict([('name','mel'),('age',45)]))
# print(dict.fromkeys(['a','b'],0))
# print(dict.fromkeys('spam',0))
# rec = {'name': {'first': 'Bob', 'last': 'Smith'},
#        'job': ['dev', 'mgr'],
#        'age': 40.5}
# print(rec['name'])
# print(rec['name']['last'])
# print(rec['job'])
# print(rec['job'][-1])
# rec['job'].append('janitor')
# print(rec)
# D = {'a': 1, 'b': 2, 'c': 3}
# D.update({'d':4, 'e':5})
# print(D)
# D.pop('e')
# print(D)
# print(D,list(D.keys()),list(D.values()),list(D.items()))
# Ks = D.keys()
# print(Ks,'!')
# Ks = list(Ks)
# Ks.sort()
# print(Ks)
# for key in Ks:
#      print(key, '=>', D[key])
# for key in sorted(D):
#      print(key, '=>', D[key])
# if not 'f' in D:
#      print('missing')
# value = D.get('f', 0) # 找不到key默认返回0
# print(value)
# value = D['x'] if 'x' in D else 0
# print(value)
# try:
#     print(D.get('f'))
# except KeyError:
#     print(0)
# print(dict(zip(['a','b','c'],[1,2,3])))
# D = {k:v for (k,v) in zip(['a','b','c'],[1,2,3])}
# print(D)
# D = {x:x**2 for x in [1,2,3,4]}
# print(D)
# D = {c:c*4 for c in 'SPAM'}
# print(D)
# D = {c.lower():c+'!' for c in ['SPAM','EGGS','HAM']}
# print(D)

# Tuple ======================================
# T = (1,) # 仅一个元素要加逗号，不然会以为是表达式
# T = (1,2,3,4)
# print(T)
# L = [x + 20 for x in T]
# print (tuple(L))
# print(len(T))
# T = T+(5, 6, 4)
# print(T)
# print(T[0])
# print(T.index(4))
# print(T.index(4,4))
# print(T.count(4))
# T=('cc','aa','dd','bb')
# tmp = list(T)
# tmp.sort()
# T = tuple(tmp)
# print(T)
# T=('cc','aa','dd','bb')
# print(sorted(T))


# File ========================================
# f = open('data.txt', 'w')
# """
# w：为输出打开文件
# r：为输入打开文件
# a：为在文件尾部追加内容打开文件
# 额外b：进行二进制数据处理
# 额外+：同时为输入和输出打开文件
# """
# f.write('Hello\n')
# f.write('world\n')
# f.write('Happy\n')
# f.write('Hour\n')
# f.close()
# f = open('data.txt')
# print(f.readline())
# print(f.readline())
# text = f.read()
# print(text)
# print(text.split())
#
# for line in open('data.txt'):
#     print(line,end='')
#
# eval('print("COde")')
#
# D = {'a':1,'b':2}
# F = open('datafile.pkl','wb')
# pickle.dump(D,F)
# F.close()
#
# F = open('datafile.pkl','rb')
# E = pickle.load(F)
# print(E)
#
# """ 运行失败，原因不明
# F = open('data.bin','wb')
# data = struct.pack('>i4sh',7,'spam',8)
# F.write(data)
# F.close()
#
# F = open('data.bin','rb')
# data = F.read()
# values = struct.unpack('>i4sh',data)
# print(values)
# """




# Set =========================================
# X = set('spam')
# Y = {'h','a','m'}
# print('e' in X)
# print(X & Y)
# print(X | Y)
# print(X - Y)
# print(X ^ Y) # XOR 保留非两者共有元素
# print(X ** 2 for x in [1,2,3,4])
# print(X>Y,X<Y) # Superset, Subset
# X.add('SPAM')
# print(X)
# X.update(set('XY'))
# print(X)
# X.remove('Y')
# print(X)
# print({x ** 2 for x in [1,2,3,4]})
# print({x for x in 'spam'})
# print({c * 4 for c in 'spam'})
# print({c * 4 for c in 'spamham'})
# L = [1,2,1,3,2,4,5]
# print(set(L))
# print(list(set(L)))
# Decimal =====================================
# d = decimal.Decimal('3.141')
# print(type(d))
# print(d+1)
# decimal.getcontext().prec = 2
# print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))

# Fraction =====================================
# f = Fraction(2,3)
# print(f+1)
# print(f+Fraction(1,2))
# Fraction('.25')

# Boolean =====================================
# print(1>2)
# print(bool('spam'))

# None =========================================
# X = None
# print(X)
# L = [None] * 10
# print(L)

# Type =========================================
# L = [1,2,3]
# print(type(L))
# print(type(type(L)))
# if type(L) == type([]):
#     print('yes')
# if type(L) == list:
#     print('yes')
# if isinstance(L, list):
#     print('yes')

# Class =======================================
# class Worker:
#     def __init__(self, name, pay):
#         self.name = name
#         self.pay = pay
#     def lastName(self):
#         return self.name.split()[-1]
#     def giveRaise(self, percent):
#         self.pay *= (1.0+percent)
#
# bob = Worker('Bob Smith', 50000)
# sue = Worker('Sue Jones', 60000)
# print(bob.lastName())
# print(sue.lastName())
# print(sue.giveRaise(.10))
# print(sue.pay)

# Operation ========================================
"""
操作优先级由低->high
yield x #生成器函数发送协议
lambda args: expression #生成匿名函数
x if y else z
x or y
x and y
not x
x in y, x not in y
x is y, x is not y 
x < y, x<y<z, x <= y, x > y, x >= y, x == y, x != y  注意！==比较值，is比较地址
x | y
x ^ y # 异或
x & y
x << y, x >> y
x + y, x - y, x * y, x % y, x / y, x // y
-x, +x
~x # 取反
x ** y
x[i]
x[i:j:k]
x(...)
x.attr
(...)
[...]
{...}
"""

# L1 = [1,('a',3)]
# L2 = [1,('a',3)]
# print(L1 == L2,L1 is L2)
# L3 = [1,('a',2)]
# print(L1 < L3, L1 == L3, L1 > L3)
#
# D1 = {'a':1,'b':2}
# D2 = {'a':1,'b':3}
# print(sorted(D1.items()) < sorted(D2.items()))