def fib(m, n):
    num = 1
    prev1 = 1
    prev2 = 0
    if m == 0:
        yield 1
    for i in range(m + n - 1):
        num = prev1 + prev2
        prev1, prev2 = num, prev1
        if i >= m - 1:
            yield num

import sys
exec(sys.stdin.read())