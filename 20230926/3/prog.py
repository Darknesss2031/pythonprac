n = 0
matr = [[], []]
idx = 0
length = 0
while True:
    if n == 0 and matr[1]:
        break
    string = list(map(lambda x: int(x), input().split(",")))
    if not n:
        n = len(string)
        length = n
        if matr[0]:
            idx = 1
    matr[idx].append(string)
    n -= 1

for i in range(length):
    string = []
    for j in range(length):
        result = 0
        for k in range(length):
            result += matr[0][i][k] * matr[1][k][j]
        string.append(str(result))
    print(",".join(string))
