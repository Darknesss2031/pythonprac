# class Titled:
#     def __init_subclass__(cls, var, *args, **kwargs):
#         cls.var = var
#         super().__init_subclass__(*args, **kwargs)
#     def __str__(self):
#         return f"[{self.title}] {super().__str__()}"
#
# class C(Titled, title=100500):
#     pass
# print(C())
#
# C = type('Simple', (), {'val': 42, 'getval': lambda self: self.val})
# c = C()
# c.val, c.getval()
#
# class overtype(type):
#     def __init__(self, Name, Parents, Dict):
#         print(f" Class definition: {Name}{Parents}: {Dict}")
#         super().__init__(Name, Parents, Dict)
#
# Boo = overtype("Boo", (), {"A": 100500})
# t = Boo()
# print(Boo, t, t.A)

# class ctype(type):
#
#     @classmethod
#     def __prepare__(metacls, name, bases, **kwds):
#         print("prepare", name, bases, kwds)
#         return super().__prepare__(name, bases, **kwds)
#
#     @staticmethod
#     def __new__(metacls, name, parents, ns, **kwds):
#         print("new", metacls, name, parents, ns, kwds)
#         return super().__new__(metacls, name, parents, ns)
# 
#     def __init__(cls, name, parents, ns, **kwds):
#         print("init", cls, parents, ns, kwds)
#         return super().__init__(name, parents, ns)
#
#     def __call__(cls, *args, **kwargs):
#         print("call", cls, args, kwargs)
#         return super().__call__(*args, **kwargs)
#
# class C(int, metaclass=ctype, parameter="See me"):
#      field = 42
#
# c = C("100500", base=16)