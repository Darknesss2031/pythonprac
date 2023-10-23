from math import *

temp = input()
width = len(temp)
temp = input()
height = 2
waterVolume = 0
while temp[1] != '#':
    if temp[1] == '~':
        waterVolume += width - 2
    height += 1
    temp = input()

waterHeight = ceil(waterVolume / (height - 2))
waterVolume = waterHeight * (height - 2)
gasVolume = (height - 2) * (width - 2) - waterVolume

print("#" * height)
for i in range(width - 2 - waterHeight):
    print("#" + "." * (height - 2) + "#")
for i in range(waterHeight):
    print("#" + "~" * (height - 2) + "#")
print("#" * height)

length = max(gasVolume, waterVolume)
gasString = "." * gasVolume
waterString = "~" * waterVolume
totalVolume = gasVolume + waterVolume
maxVolumeString = len(str(max(gasVolume, waterVolume)))
print(f"{gasString:<{length}} {gasVolume:>{maxVolumeString}}/{totalVolume}")
print(f"{waterString:<{length}} {waterVolume:>{maxVolumeString}}/{totalVolume}")