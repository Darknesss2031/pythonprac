a, b = eval(input())
print([i for i in range(a, b) if all([i % el != 0 for el in range(2, int(i**0.5) + 1)])])