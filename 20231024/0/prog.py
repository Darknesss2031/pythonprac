# def gen():
#     result = 0
#     for i in range(1, 10000):
#         result += (1 / i**2)
#         yield result
#
# N = 10000
# print(sum(1/i**2 for i in range (1, 10001)))
#
# def genf():
#     res = yield "start"
#     while res:
#         res = yield f"/{res}/"
#
# def walk2d():
#     x = 0
#     y = 0
#     while delta := (yield coord):
#         coord = coord[0] + delta[0], coord[1] + delta[1]
#         inp = yield (x, y)
# send = None
# gen = walk2d()
# while send := input():
#     send = eval(input())
#     gen.send(send)
#     print()

# def travel(n):
#     for i in range(n):
#         yield "По кочкам"
#     return "В яму"
#
# def travelwrap(n):
#     a = yield from travel(n)
#     yield a
#
# a = travelwrap(10)
# print(*list(a), sep = "\n")

