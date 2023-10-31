# class C:
#     pass
#
# def fun (*args): return args
#
# C.funct = fun
#
# ex = C()
# print(ex.funct is fun)

class Rectangle:
    x1: int
    x2: int
    y1: int
    y2: int
    rectcnt = 0
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.__class__.rectcnt += 1
        setattr(self, f"rect_{self.__class__.rectcnt}", self.__class__.rectcnt)
    def __str__(self):
        return f"({self.x1}, {self.y1})({self.x1}, {self.y2})({self.x2}, {self.y2})({self.x2}, {self.y1}), {self.__class__.rectcnt})"
    def __del__(self):
        self.__class__.rectcnt -= 1

print(Rectangle(1, 2, 3, 4))

print()

a = Rectangle(1, 2, 3, 4)
b = Rectangle(2, 3, 4, 5)
c = Rectangle(3, 4, 5, 6)

print(dir(a), dir(b), dir(c), sep="\n")

attr = "eee"
setattr(Rectangle, attr, 100500)
getattr(Rectangle, attr)

