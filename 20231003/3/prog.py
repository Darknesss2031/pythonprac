from math import *

def Calc(s, t, u):
    a = lambda x: eval(s)
    b = lambda x: eval(t)
    c = lambda x, y: eval(u)
    def result(x):
        return c(a(x), b(x))
    return result

print(Calc(*eval(input()))(eval(input())))