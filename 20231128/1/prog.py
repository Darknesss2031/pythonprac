class dump(type):
    def __init__(cls, name, parents, attrs):
        def dec(fun):
            def fun_info(self, *args, **kwargs):
                print(fun.__name__, ': ', args, ', ', kwargs, sep='')
                return fun(self, *args, **kwargs)
            return fun_info
        for _name in cls.__dict__:
            object = getattr(cls, _name)
            if callable(object):
                setattr(cls, _name, dec(object))


import sys
exec(sys.stdin.read())