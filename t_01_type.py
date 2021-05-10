import math
import random
import re
import decimal
from fractions import Fraction

# Number======================================================
print(type(1234),type(3.1415),type(3+4j),type(3e-10),type(3.14E10),type(4.0e+5))
print(type(0xF),type(0XF),type(0o7),type(0O7),type(0b1),type(0B1))

print(123+222)
print(1.5*4)
print(2**100)
print(math.pi)
print(math.sqrt(85))
print(random.random())
print(random.choice([1,2,3,4]))

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
# print(S.find('pa'))
# print(S.replace('pa','XYZ'))
# line = 'aaa,bbb,ccccc,dd'
# print(line.split(','))
# print(S.upper())
# print(S.isalpha())
# print(S.isdigit())
# line = 'aaa,bbb,ccccc,dd\n'
# print(line.rstrip())
# print('---')
# print('%s, eggs, and %s'%('spam','SPAM!') )
# print('{0}, eggs,and {1}'.format('spam','SPAM!'))
# print(dir(S))
# print(help(S.replace))
# print(help(str))
# S = 'A\nB\tC'
# print(S)
# print(len(S))
# print(ord('\n')) # ASCII
# print('A\0B\0C')
# print("""aaaaa
# bbb'''bbbbb""bbbbbb'bbbb
# CCCCCCCCC""")
# match = re.match('Hello[ \t]*(.*)world','Hello  Python world')
# print(match.group(1))
# match = re.match('/(.*)/(.*)/(.*)','/usr/home/lumberjack')
# print(match.groups())

# list ==============================================
# L = [123,'spam',1.23]
# print(len(L))
# print(L[0])
# print(L[:-1])
# print(L + [4, 5, 6])
# print(L)
# print(L.append('NI'))
# print(L.pop(2))
# print(L)
# L.insert(2,'add2')
# print(L)
# L.remove('add2')
# print(L)
# M = ['bb','aa','cc']
# M.sort()
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

# dictionary ============================================
# D = {'food': 'Spam','quantity': 4, 'color': 'pink'}
# print(D['food'])
# D['quantity'] += 1
# print(D)
# D = {}
# D['name'] = 'Bob'
# D['job'] = 'dev'
# D['age'] = 40
# print(D)
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
# print(D)
# Ks = list(D.keys())
# print(Ks.sort())
# print(Ks)
# for key in Ks:
#      print(key, '=>', D[key])
# for key in sorted(D):
#      print(key, '=>', D[key])
# if not 'f' in D:
#      print('missing')
# value = D.get('f', 0)
# print(value)
# value = D['x'] if 'x' in D else 0
# print(value)

# Tuple ======================================
# T = (1,2,3,4)
# print(len(T))
# print(T+(5, 6))
# print(T[0])
# print(T.index(4))
# print(T.count(4))

# File ========================================
# f = open('data.txt', 'w')
# f.write('Hello\n')
# f.write('world\n')
# f.close()
# f = open('data.txt')
# text = f.read()
# print(text)
# print(text.split())

# Set =========================================
# X = set('spam')
# Y = {'h','a','m'}
# print(X & Y)
# print(X | Y)
# print(X - Y)
# print(X ** 2 for x in [1,2,3,4])

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