# s = [1, 2, 4, "QWE"]
# dir(s)
#
# a = 123
# a += 2
# a = a + 2
#
# id(s)
# s = s + [1, 2, 3]
# id(s)
#
# s += ["Q", "Q"]
# id(s)
# s.extend([345, 5345])
# id(s)
#
# s[1:-2:2]

#print("YES" if 13 in eval(input()) else "NO")

# a = list(range(5, 16))
# b = list("abcdefghjk")
# a[4:8] = b[-5:]
# #a = a[:4] + b[-5:] + a[8:]
# print(a)
#
# c = a[-1: -len(a)//2: -2]
# print(c)

# for i in range(10):
#     if i%2==1:
#         print(i)
#         break
# else:
#     print(i)
import pprint

ar=[]
while (s:=input()):
    ar.append(s.split())

l = len(ar)
if all([len(el) == l for el in ar]):
    for i in range(len(ar)):
        for j in range(i, len(ar)):
            ar[i][j], ar[j][i] = ar[j][i], ar[i][j]



for el in ar:
    print(*el)

#print(*[i for i in range(int(input()), int(input())) if i % 2 == 1 and '3' not in str(i)])