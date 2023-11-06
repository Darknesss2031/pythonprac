import itertools

def check(*seq):
    for el in seq:
        if el:
            return True
    return False
def slide(seq, n):
    idx = 0
    while True:
        temp = itertools.islice(seq, idx, idx + n)
        arr = list(temp)
        if check(arr):
            yield from arr
        else:
            break
        idx += 1

import sys
exec(sys.stdin.read())