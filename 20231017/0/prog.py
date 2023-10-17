import timeit
from collections import Counter

# timeit.Timer('"-".join([str(n) for n in range(100)])').autorange(callback = lambda x, y: print(y/x))

# def f(s):
#     s = set(s)
#     w = set("aouiey")
#     return len(s & w), len(s - w)
#
# timeit.Timer('f("qwertyuiop")', globals = globals()).autorange(callback = lambda x, y: print(y/x))
# d = {f"<{i}>": i*2 + 1 for i in range(10)}
# print(d)

s = input().split()
dic = {}
for word in s:
    if word in dic.keys():
        dic[word] += 1
    else:
        dic[word] = 1
print(dic, Counter(s))
print(dict(zip(t := ())))