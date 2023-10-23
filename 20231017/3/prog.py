def clearString(string):
    result = ""
    for letter in string:
        if letter.isalpha() or letter == " ":
            result += letter
        else:
            result += " "
    return result

arr = []
slow = {}
m = int(input())
while inp := input():
    temp = clearString(inp).lower().split()
    for word in temp:
        slow[word] = slow.setdefault(word, 0) + 1
temp = sorted(slow.items(), key=lambda x: x[1])

maxCount = 0
for x, y in temp:
    if len(x) == m:
        if y > maxCount:
            maxCount = y
            arr.clear()
            arr.append(x)
        elif y == maxCount:
            arr.append(x)
print(*arr, sep=" ")