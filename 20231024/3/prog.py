from itertools import *

print(*sorted(filter(lambda x: x.count('TOR') == 2, map(lambda x: ''.join(x), product('TOR', repeat = int(input()))))))