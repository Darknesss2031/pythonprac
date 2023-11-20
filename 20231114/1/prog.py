def objcount(cls):
    class Tmp(cls):
        counter = None
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            if self.__class__.counter is None:
                self.__class__.counter = 1
            else:
                self.__class__.counter += 1

        def __del__(self):
            try:
                super().__del__()
            except Exception:
                pass
            self.__class__.counter -= 1

    return Tmp

import sys
exec(sys.stdin.read())