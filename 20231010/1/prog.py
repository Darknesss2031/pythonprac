def pow(num, degree):
    result = 1
    while degree > 0:
        result *= num
        degree -= 1
    return result

inp = list(map(lambda x: eval(x.strip()), input().split(',')))
i = 2
a = 0
b = 0
check = inp[0]
c = inp[1]

degree = inp[i]
i += 1
while degree >= 0:
    a += inp[i] * pow(check, degree)
    degree -= 1
    i += 1

degree = inp[i]
i += 1
while degree >= 0:
    b += inp[i] * pow(check, degree)
    degree -= 1
    i += 1
if b == 0:
    print(False)
else:
    print(a / b == c)
