# equal =================================================
# spam = 'Spam'
# print(spam)
# spam, ham = 'yum', 'YUM'
# print(spam,ham)
# [spam,ham] = ['yume','YUMe']
# print(spam,ham)
# a,b,c,d = 'spam'
# print(a,b,c,d)
# a, *b = 'spam'
# print(a,b)
# *a, b = 'spam'
# print(a,b)
# a, *b, c = 'spam'
# print(a,b,c)
# spam = ham = 'lunch'
# print(spam,ham)
# spams = 2
# spams += 42
# print(spams)
# red, green, blue = range(3)
# print(red,blue)

# variable===============================================
# _X = 5 # 不会被from module import * 导入
# __Y__ = 5 # 系统定义的变量名
# __Z = 5 # 类的本地（压缩）变量

# print =================================================
# x = 'spam'
# y = 99
# z = ['eggs']
# print(x,y,z)
# print(x,y,z,sep=',')
# print(x,y,z,end='<<<\n')
# print(x,y,z,sep='\t',file=open('data.txt','w'))

# boolean operation =======================================
# t = True
# f = False
# print(t and f)
# print(t or f)
# print(not t)
# print(2 or 3, 3 or 2)
# print([] or {})
# print([] or 3)
# print(2 and 3, 3 and 2)
# print([] and {})
# print([] and 3)

# while =================================================
# while True:
#     reply = input('Enter text:')
#     if reply == 'stop': break
#     print(reply.upper())
# while True:
#     pass
#     if False: break
#     if True: continue
# else:
#     ...


# if ====================================================
# while True:
#     reply = input('Enter text:')
#     if reply == 'stop':
#         break
#     elif not reply.isdigit():
#         print('Bad!' * 8)
#     else:
#         print(int(reply)**2)
# print('Bye')
# A = 't' if 'spam' else 'f'
# print(A)
# A = 't' if '' else 'f'
# print(A)
# A = ['f','t'][bool('spam')]
# print(A)
# A = 'a' or 'p' or 'p' or None
# print(A)

# for ===================================================
# for x in [1,2,3,4]:
#     if True: break
#     if True: continue
# else:
#     ...
# T = [(1,2),(3,4),(5,6)]
# for (a,b) in T:
#     print(a,b)
#
# D = {'a':1,'b':2,'c':3}
# for key in D:
#     print(key,'=>',D[key])
#
# for line in open('data.txt','r'):
#     print(line,end='<<<')
#
# for i in range(4):
#     print(i)
#
# print(list(range(5)),list(range(2,5)),list(range(0,10,2)))
# print(list(range(5,-5,-1)))
#
# L1 = [1,2,3,4]
# L2 = [5,6,7,8,9]
# print(list(zip(L1,L2)))
# for (x,y) in zip(L1,L2):
#     print(x,y,'--',x+y)
#
# keys = ['spam','eggs','toast']
# vals = [1,3,5]
# print(zip(keys,vals))
# D3 = dict(zip(keys,vals))
# print(D3)
#
# S = 'spam'
# for (offset, item) in enumerate(S):
#     print(item, 'appears at offset', offset)
#
# L = [1,2,3]
# I = iter(L)
# print(I.__next__())
# print(I.__next__())
# print(I.__next__())
#
# f = open('data.txt')
# print(iter(f) is f)
# print(f.__next__())
# f.close()
# lines = [line.rstrip() for line in open('data.txt') if line[0] == 's']
# print(lines)
# print([x+y for x in 'abc' for y in 'lmn'])

# try ===================================================
# while True:
#     reply = input('Enter text:')
#     if reply == 'stop':break
#     try:
#         num = int(reply)
#     except:
#         print('Bad!' * 8)
#     else:
#         print(int(reply)**2)
# print('Bye')

# doc ===================================================
# print(map.__doc__,end="/n")
# help(map)