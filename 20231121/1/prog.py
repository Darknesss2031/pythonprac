import sys

inp = sys.stdin.buffer.read()
part_count = inp[0]
tail = inp[1:]
output = []
for i in range(part_count):
    output.append(inp[round(i * len(tail) / part_count + 1):round((i+1) * len(tail) / part_count + 1)])
sys.stdout.buffer.write(bytes((part_count,)))
output = sorted(output)
for part in output:
    sys.stdout.buffer.write(part)