class InvalidInput(Exception): pass
class BadTriangle(Exception): pass

def dist(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def triangleSquare(inp):
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    x3 = 0
    y3 = 0
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(inp)
    except Exception as e:
        raise InvalidInput
    try:
        sides = [dist(x1, y1, x2, y2), dist(x1, y1, x3, y3), dist(x2, y2, x3, y3)]
    except Exception as e:
        raise BadTriangle
    if sides[0] < sides[1] + sides[2] and sides[1] < sides[0] + sides[2] and sides[2] < sides[1] + sides[0] and min(sides) > 0:
        return abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2
    else:
        raise BadTriangle

flag = True
while flag:
    try:
        result = triangleSquare(input())
    except InvalidInput as e:
        print("Invalid input")
    except BadTriangle as e:
        print("Not a triangle")
    else:
        print(f"{result:.2f}")
        flag = False