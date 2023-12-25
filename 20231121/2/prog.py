import sys

inp = sys.stdin.buffer.read()
print(inp.decode('UTF-8').encode('latin-1', errors='replace').decode('cp1251'), end='')