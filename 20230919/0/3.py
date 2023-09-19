a, b, c = eval(input())
if (min(a, b, c) > 0 and 2 * max(a, b, c) < a + b + c): print("YES")
else: print("NO")