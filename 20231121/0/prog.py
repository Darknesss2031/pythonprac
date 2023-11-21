# f = open("file1.txt", "rb")
# g = open("file2.txt", "rb")
#
# a, b = list(), list()
#
# while x := f.read(1):
#     a.append(x)
#
# while x := g.read(1):
#     b.append(x)
#
# a, b = [*b[:len(b)//2], *a[len(a)//2]], [*a[:len(a)//2], *b[len(b)//2]]
# print(a)
# print(b)
#
# f.seek(0, 2)



# import locale
#
# txt = "Вопрос"
# print(*map(hex, map(ord, txt)))
# txt.encode()
# locale.getdefaultlocale()
# txt.encode('UTF-8')
# print(txt.encode('WINDOWS-1251'))
# print(txt.encode('KOI8-R'))
# print(txt.encode('WINDOWS-1251').decode('KOI8-R'))
# print(txt)

# import pickle
# class A:
#     def __init__(self, item):
#         self.var = item
# c = A(2)
# print(pickle.dumps(c))
# print(a := pickle.loads(pickle.dumps(c)))
# print(a.var)
