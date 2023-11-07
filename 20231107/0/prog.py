# class A:
#     f = 1
#     g = 2
#     v = 1
# class B(A):
#     f = 1050
#     v = 2
# b = B()
# b.v = 3
# print(b.v)
# del b.v
# print(b.v)
# del B.v
# print(b.v)

# class A:
#     def __init__(self, var):
#         self.var = var
#     def __add__(self, other):
#         return self.__class__(self.var + other)
#
# a = A(1)
# print(a)
# print(a.var)
# print((a+1).var)
#
# class B(A):
#     def __str__(self):
#         return f"<{self.var}>"
#
# a = B(12)

# class A: pass
# class B: pass
# class C(A, B): pass
# class D(B, A):pass
# class E(C, A, B): pass
# class E(C, A): pass
# class E(C, B): pass

# class A:
#     def __str__(self):
#         return "A"
#
# class B(A):
#     def __str__(self):
#         return super().__str__() + f":B"
#
# class C(B):
#     def __str__(self):
#         return super().__str__() + f":C"
#
# a, b, c = A(), B(), C()
# print(a, b, c)

# class A(Exception):
#     pass
#
# class B(A):
#     pass
#
# class C(B):
#     pass
#
# for e in (A, B, C):
#     try:
#         raise e
#     except B:
#         print("B")
#     except A:
#         print("A")
#     except C:
#         print("C")
# def f():
#     try:
#         a = int(input())
#     except Exception:
#         f()
#
# f()
import math
def div_ab(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return math.inf
for i in ((10, 2), (1, 0), (9, 3)):
    print(div_ab(*i))