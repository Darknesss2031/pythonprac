from functools import wraps

# def genf(f):
#     @wraps(f)
#     def newfun(*args):
#         print(">", *args)
#         res = f(*args)
#         print("<", res)
#         return res
#     return newfun
#
# @genf
# def fun(a,b):
#     """this is function"""
#     return a*2+b

# print(fun(2,3), fun.__doc__)

# def checkInt(fun):
#     def newfun(*args):
#         for el in args:
#             if not isinstance(el, int):
#                 raise TypeError
#         return fun(*args)
#     return newfun
#
# @checkInt
# def plus(a, b):
#     return a + b
#
# print(plus(2, 3))
# print(plus(0, 6))
# print(plus(1, 1.1))

# def checkType(type):
#     def check(fun):
#         def newfun(*args):
#             if not all(isinstance(el, type) for el in args):
#                 raise TypeError
#             else:
#                 return fun(*args)
#         return newfun
#     return check
#
# @checkType(float)
# def mult(a, b):
#     return a * b
#
# print(mult(0.1, 0.2))
# print(mult(0.1, 3))

# class Sender:
#     flag = True
#     @classmethod
#     def report(cls):
#         if cls.flag:
#             print("Greetings!")
#             cls.flag = False
#         else:
#             print("Get away!")
#
# class Asker:
#     @staticmethod
#     def askall(lst):
#         for el in lst:
#             Sender.report()
#
# Asker.askall([Sender(), Sender(), Sender()])

class Desc:
    def __get__(self, instance, owner):
        print("GET", instance, owner)
        return instance._val
    def __set__(self, instance, value):
        print("SET", instance, value)
        instance._val = value

class C:
    field = Desc()
#
# c = C()
# c.data = 123

# class Dsc:
#
#     def __get__(self, obj, cls):
#         print(f"Get from {cls}:{repr(obj)}")
#         return obj._value
#
#     def __set__(self, obj, val):
#         print(f"Set in {repr(obj)} to {val}")
#         obj._value = val
#
#     def __delete__(self, obj):
#         print(f"Delete from {repr(obj)}")
#         obj._value = None
#
# class C:
#         data = Dsc()

c = C()
c.field = 123



