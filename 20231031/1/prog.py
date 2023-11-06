class Omnibus:
    stDict = {}

    def __init__(self):
        self.__dict__.update({'objAttr': []})

    def __getattr__(self, item):
        return self.__class__.stDict[item]

    def __setattr__(self, key, value):
        self.__class__.stDict[key] = self.__class__.stDict.setdefault(key, 0) + 1
        self.objAttr.append(key)

    def __delattr__(self, item):
        if item in self.__class__.stDict.keys() and item in self.objAttr:
            del self.item
            self.__class__.stDict[item] -= 1
            self.objAttr.remove(item)

import sys
exec(sys.stdin.read())