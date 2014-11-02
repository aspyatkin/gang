import sys
main_ver = sys.version_info[0]


def subclass_object(obj):
    if type(obj) == dict:
        return GangDict(obj)
    elif type(obj) == list:
        return GangList(obj)
    elif type(obj) == tuple:
        return GangTuple(obj)
    return obj


class GangTuple(tuple):
    def __new__(cls, iterable):
        return super(GangTuple, cls).__new__(cls, iterable)


class GangList(list):
    @property
    def super(self):
        if main_ver == 2:
            return super(GangList, self)
        elif main_ver == 3:
            return super()
        else:
            raise Exception('Unknown Python version!')

    def __init__(self, data):
        self.super.__init__(data)

    def __iter__(self):
        return iter((subclass_object(o) for o in self.super.__iter__()))

    def __getitem__(self, index):
        return subclass_object(self.super.__getitem__(index))


class GangDict(dict):
    @property
    def super(self):
        if main_ver == 2:
            return super(GangDict, self)
        elif main_ver == 3:
            return super()
        else:
            raise Exception('Unknown Python version!')

    def __init__(self, data):
        self.super.__init__(data)

    def __getattr__(self, name):
        if name in self:
            return subclass_object(self.super.__getitem__(name))
        else:
            raise AttributeError('No attribute {name}'.format(name=name))

    def __getitem__(self, key):
        if key in self:
            return subclass_object(self.super.__getitem__(key))
        else:
            raise KeyError('No key {name}'.format(name=key))

    def __setattr__(self, name, value):
        self.super.__setitem__(name, value)

    def __setitem__(self, key, value):
        self.super.__setitem__(key, value)

    def iteritems(self):
        return iter((x, subclass_object(y)) for x, y in self.super.iteritems())

    def items(self):
        return iter((x, subclass_object(y)) for x, y in super().items())
