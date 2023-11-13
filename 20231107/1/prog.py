import collections


class DivStr(collections.UserString):
    def __init__(self, *string):
        if string:
            super().__init__(*string)
        else:
            super().__init__("")

    def __floordiv__(self, other):
        result = []
        length = len(self) // other
        if length == 0:
            return [""] * other
        i = 0
        while i + length - 1 < len(self):
            result.append(self[i : i + length])
            i += length
        return result

    def __mod__(self, other):
        length = len(self) % other
        return self[len(self) - length:]

import sys
exec(sys.stdin.read())