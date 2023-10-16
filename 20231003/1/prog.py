def cmp(first, second):
    if  first[0] >= second[0] and first[1] >= second[1] and (first[0] > second[0] or first[1] > second[1]):
        return True
    return False

def Pareto(*pairs):
    result = []
    for i in range (len(pairs)):
        flag = True
        for j in range (len(pairs)):
            if j == i: continue
            if cmp(pairs[j], pairs[i]):
                flag = False
        if flag:
            result.append(pairs[i])
    return tuple(result)

arr = eval(input())
print(Pareto(*arr))
