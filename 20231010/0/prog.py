import decimal
from decimal import Decimal
from fractions import Fraction
from math import *

def multiplier(x, y, type):
    return type(x) * type(y)

def esum(N, one):
    result = 0
    counter = 0
    add = 1
    while counter <= N:
        result += add
        counter += 1
        add /= counter
    return result

def scale(a, b, A, B, x):
    return A + (x-a)*(A-B)/(a-b)

#print(multiplier("1.2", "4.0", float), multiplier("1.2", "4.0", Decimal))

# print(Decimal(2).sqrt())
# c = decimal.getcontext()
# c.prec = 100
# print(Decimal(2).sqrt())
#
# print(esum(100, 1.0))

#s = "evrnjij injvm    irovmkrmv rijgmerg ergime   gr rtgim"
# s = input().split()
# print(s[4], s[1], s[0], sep=", ")

# N = 30
# for i in range(N):
#     x = scale(0, N-1, -5, 5, i)
#     y = sin(x)
#     w = scale(-1, 1, 0, 20, y)
#     print(int(w) * " ", "*")

# scr = [['.'] * 100 for i in range(20)]
# N = 100
# for i in range(N):
#     x = scale(0, N-1, 0, 99, i)
#     y = sin(x)
#     w = scale(-1, 1, 0, 19, y)
#     scr[int(w)][int(x)] = "*"
# print("\n".join(["".join(s) for s in scr]))

for i in range (12, 24):
    print(f"{bin(i):<7} = {hex(i)}")
