s = input()
first = True
curPair = " "
pairSet = set()
for letter in s:
    if first:
        curPair += letter
        first = False
        continue
    curPair = (curPair[1] + letter).lower()
    if curPair.isalpha():
        pairSet.add(curPair)
print(len(pairSet))