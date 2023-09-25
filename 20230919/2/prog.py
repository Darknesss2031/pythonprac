summ = 0
while (num := int(input())) > 0:
    summ += int(num)
    if summ > 21:
        print(summ)
        break
else:
    print(num)