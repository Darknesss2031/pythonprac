from math import *

def scale(a, b, A, B, x):
    return A + (x-a)*(A-B)/(a-b)

inpStr = input().split()

inp = list(map(lambda x: eval(x.strip()), inpStr[:4]))
inp.append(inpStr[4])

scr = [[' '] * inp[0] for i in range(inp[1])]

ord = []

for i_x in range(inp[0]):
    x = scale(0, inp[0] - 1, inp[2], inp[3], i_x)
    y = eval(inp[4])
    ord.append(y)
ordMax = max(ord)
ordMin = min(ord)
ord = list(map(lambda x: scale(ordMin, ordMax, 0, inp[1] - 1, x), ord))

for x in range(inp[0]):
    scr[inp[1] - round(ord[x]) - 1][x] = '*'

for s in scr:
    print("".join(s))


