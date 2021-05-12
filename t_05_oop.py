# class Man(object):
#     def __init__(self,name):
#         self.__name = name
#     def laugh(self):
#         print('hahaha')

# 继承 ==========================================================
# class Student(Man):
#     def __init__(self,name,num):
#         self.__name = name
#         self.__num = num
#         self.publicName = 'pp'
#     def getName(self):
#         return self.__name
#     def laugh(self):
#         print(self.__name,end=":")
#         super().laugh()

# 重载 ======================================================
# class NewStudent(Student):
#     def __init__(self, name, num):
#         self.__name = name
#         self.__num = num
#     def getName(self):
#         return "new_"+self.__name
#
# a = Student('Jack','12345')
# a.laugh()
# print(a.getName())
# print(a._Student__name)
# a.newAttribute = 'something new' # 可以在外部添加额外实例属性（仅被本实例用）/ 方法同理
"""
可以在类中设置__slot__变量来限制class实例能够添加的属性（仅对自己有效，对子类无效）
__slots__ = ('name','num')
"""
# def upperName(self): return self.publicName.upper()
# Student.newMethod = upperName # 可以在外部添加额外类方法（可被其他实例用/无法调用似有属性）/ 属性同理
# print(a.newAttribute)
# print(a.newMethod())
# b = NewStudent('ali','54321')
# print(b.getName())


# 多态 =====================================================
# Python中不一定要求一定是父子关系，只要对象有getName方法就可以
# def printName(student):
#     print(student.getName())
#
# printName(a)
# printName(b)

# 多重继承 ================================================
# class Manager():
#     pass
# class mulStudent(Student, Manager):
#     pass

# @property =============================================
class Student(object):
    @property #getter
    def score(self): # 方法名和实例变量名不能相等
        return self._score

    @score.setter #setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value<0 or value>100:
            raise ValueError('score must between 0~100!')
        self._score = value

s = Student()
s.score = 60 # <=> s.set_score(60)
print(s.score) # <=> s.get_score()

# enum ========================================================
# from enum import Enum
# Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep',
#                       'Oct','Nov','Dec'))
# for name, member in Month.__members__.items():
#     print(name, '=>', member,',',member.value)
#
# from enum import Enum, unique
#
# @unique
# class Weekday(Enum):
#     Sun = 0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6
#
# day1 = Weekday.Mon
# print(day1)
# print(Weekday['Tue'])
# print(Weekday.Tue.value)
# print(day1 == Weekday.Mon)
# print(Weekday(1))
# print(day1 == Weekday(1))