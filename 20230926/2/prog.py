def cmp(first, second):
    if (first ** 2) % 100 < (second ** 2) % 100:
        return True
    elif (first ** 2) == (second ** 2):
        if first <= second:
            return True
        else:
            return False
    else:
        return False

a = list(map(lambda x: int(x), input().split(",")))

for i in range(len(a)):
    minNum = a[i]
    minIdx = i
    for j in range(i + 1, len(a)):
        if cmp(a[j], minNum):
            minNum = a[j]
            minIdx = j
    a[i], a[minIdx] = a[minIdx], a[i]
print(a)

