def diff(first, second):
    if type(first) == type(second):
        if isinstance(first, tuple):
            result = []
            for el in first:
                if el not in second:
                    result.append(el)
            return tuple(result)
        elif isinstance(first, list):
            result = []
            for el in first:
                if el not in second:
                    result.append(el)
            return result
        elif isinstance(first, str):
            result = ""
            for el in first:
                if el not in second:
                    result = result + el
            return result
        else:
            return first - second
    return -1

print(diff(*eval(input())))