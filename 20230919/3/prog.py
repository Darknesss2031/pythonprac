def sumDig (num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

num = int(input())
temp1 = num
while temp1 <= num + 2:
    temp2 = num
    while temp2 <= num + 2:
        result = temp1 * temp2
        if sumDig(result) == 6:
            print(temp1, "*", temp2, "=", end = " :=) ")
        else:
            print(temp1, "*", temp2, "=", result, end = " ")
        temp2 += 1
    print()
    temp1 += 1