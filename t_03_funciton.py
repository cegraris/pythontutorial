# if False:
#     def func():
#         print('func1')
# else:
#     def func():
#         print('func2')
# func()
# othername = func
# othername()

# global variable and function ========================
# X = 23
# def func2():
#     global X
#     X += 1
# func2()
# print(X)

# factory function
# def maker(N):
#     def action(X):
#         return X ** N
#     return action
# f = maker(2)
# print(f(3))
# g = maker(3)
# print(g(3))

# lambda =============================
# def func3():
#     x = 4
#     action = (lambda n: x ** n)
#     return action
# x = func3()
# print(x(2))
#
# def makeActions():
#     acts = []
#     for i in range(5):
#         acts.append(lambda x, i=i: i**x)
#     return acts
# acts = makeActions()
# print(acts[0](2))
# print(acts[2](2))
# print(acts[4](2))
# f = lambda x,y,z: x+y+z
# print(f(2,3,4))
# x = (lambda a='fee', b='fie',c='foe': a+b+c)
# print(x('wee'))
#
# lower = (lambda x, y: x if x<y else y)
# print(lower('bb','aa'))
#
# action = (lambda x: (lambda y: x+y))
# act = action(99)
# print(act(3))

# nonlocal ===========================
# def tester(start):
#     state = start
#     def nested(label):
#         nonlocal state
#         print(label,state)
#         state += 1
#     return nested
# F = tester(0)
# F('spam')
# F('ham')

# parameters ==============================
# def f(a,b,c): print(a,b,c)
# f(1,2,3)
# f(c=3,b=2,a=1)
# f(1,c=3,b=2)
#
# def f2(a,b=2,c=3): print(a,b,c)
# f2(1)
# f2(a=1)
# f2(1,4)
# f2(1,4,5)
# f2(1,c=6)
#
# def f3(*args): print(args)
# f3()
# f3(1)
# f3(1,2,3,4)
#
# def f4(**args): print(args)
# f4()
# f4(a=1,b=2)
#
# def f5(a, *pargs, **kargs): print(a,pargs,kargs)
# f5(1,2,3,x=1,y=2)
#
# args = (1,2,3)
# f(*args)
#
# args = {'a':1,'b':2,'c':3}
# f(**args)
#
# def f6(func,*pargs,**kargs):
#     print('calling:',func.__name__)
#     return func(*pargs, **kargs)
# def func(a,b,c,d):
#     return a+b+c+d
# print(f6(func,1,2,c=3,d=4))
#
# def f7(a,*b,c): print(a,b,c) # c keyword-only
# f7(1,2,c=3)
# f7(1,c=3)
#
# def f8(a,*,b,c): print(a,b,c)
# f8(1,c=3,b=2)
#
# def f9(a,*,b='spam',c='ham'): print(a,b,c)
# f9(1)
#
# def f10(a,*b,c=6,**d): print(a,b,c,d) # c is keyword-only
# def f11(a,c=6,*b,**d): print(a,b,c,d) # c is not keyword-only
# f10(1,*(2,3),**dict(x=4,y=5)) # **dict final
#
# def f12(a:'spam'=4,b:(1,10)=5,c:float=6)->int:
#     return a+b+c
# print(f12.__annotations__)

# map =========================================================
# def inc(x): return x+10
# counters = [1,2,3,4]
# print(list(map(inc, counters)))
#
# L = list(map((lambda x: x + 3), counters))
# print(L)
#
# L = list(map(pow,[1,2,3],[2,3,4]))
# print(L)
#
# L = list(filter((lambda x: x>0),range(-5,5)))
# print(L)
#
# from functools import reduce
# print(reduce((lambda x,y: x+y),[1,2,3,4]))

# yield =========================================================
# def gensquares(N):
#     for i in range(N):
#         yield i**2
#
# for i in gensquares(5):
#     print(i, end=' : ')
# print('/n')
#
# x = gensquares(4)
# print(next(x))
# print(next(x))
# print(next(x))
#
# def gen():
#     for i in range(10):
#         X = yield i
#         print(X)
# G = gen()
# next(G) # must! Start generator
# print(G.send(77))
# print(G.send(88))
# print(next(G))
#
# G = (x ** 2 for x in range(4))
# print(next(G))
# print(next(G))
# print(next(G))
#
# for num in (x ** 2 for x in range(4)):
#     print('%s, %s' % (num, num/2.0))

# time =======================================
# import time
# reps = 1000
# repslist = range(reps)
# def timer(func, *pargs, **kargs):
#     start = time.clock()
#     for i in repslist:
#         ret = func(*pargs, **kargs)
#     elapsed = time.clock()-start
#     return (elapsed, ret)
#
# decorator =========================================
# import functools
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kargs):
#         print('call %s():' % func.__name__)
#         return func(*args, **kargs)
#     return wrapper
#
# @log # <=> now = log(now)
# def now():
#     print('2021')
#
# f = now
# f()
# print(now.__name__)
#
# def log2(text):
#     def decorator(func):
#         def wrapper(*args,**kargs):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kargs)
#         return wrapper
#     return decorator
#
# @log2('execute') # <=> log2('execute')(now)
# def now():
#     print('2021')
#
# f = now
# f()
# print(now.__name__)
#
# partial function ==========================================
print(int('12345'))
print(int('12345',base=8))
print(int('12345',16))

import functools
int2 = functools.partial(int,base=2) #把int函数中base参数默认值设定为2,返回函数
print(int2('100000'))
