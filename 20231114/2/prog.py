class Num:
    def __get__(self, instance, owner):
        try:
            return instance._num
        except Exception:
            return 0

    def __set__(self, instance, value):
        if 'real' in value.__dir__():
            instance._num = value.real
        elif '__len__' in value.__dir__():
            instance._num = len(value)

import sys
exec(sys.stdin.read())