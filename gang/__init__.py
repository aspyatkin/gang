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


if main_ver == 2:
    class GangTuple(tuple):
        def __new__(cls, iterable):
            return super(GangTuple, cls).__new__(cls, iterable)


    class GangList(list):
        def __init__(self, data):
            super(GangList, self).__init__(data)

        def __iter__(self):
            return iter((subclass_object(o) for o in super(GangList, self).__iter__()))

        def __getitem__(self, index):
            return subclass_object(super(GangList, self).__getitem__(index))


    class GangDict(dict):
        def __init__(self, data):
            super(GangDict, self).__init__(data)

        def __getattr__(self, name):
            if name in self:
                return subclass_object(super(GangDict, self).__getitem__(name))
            else:
                raise AttributeError('No attribute {name}'.format(name=name))

        def __getitem__(self, key):
            if key in self:
                return subclass_object(super(GangDict, self).__getitem__(key))
            else:
                raise KeyError('No key {name}'.format(name=key))

        def __setattr__(self, name, value):
            super(GangDict, self).__setitem__(name, value)

        def __setitem__(self, key, value):
            super(GangDict, self).__setitem__(key, value)

        def iteritems(self):
            return iter((x, subclass_object(y)) for x, y in super(GangDict, self).iteritems())

elif main_ver == 3:
    class GangTuple(tuple):
        def __new__(cls, iterable):
            return super(GangTuple, cls).__new__(cls, iterable)


    class GangList(list):
        def __init__(self, data):
            super().__init__(data)

        def __iter__(self):
            return iter((subclass_object(o) for o in super().__iter__()))

        def __getitem__(self, index):
            return subclass_object(super().__getitem__(index))


    class GangDict(dict):
        def __init__(self, data):
            super().__init__(data)

        def __getattr__(self, name):
            if name in self:
                return subclass_object(super().__getitem__(name))
            else:
                raise AttributeError('No attribute {name}'.format(name=name))

        def __getitem__(self, key):
            if key in self:
                return subclass_object(super().__getitem__(key))
            else:
                raise KeyError('No key {name}'.format(name=key))

        def __setattr__(self, name, value):
            super().__setitem__(name, value)

        def __setitem__(self, key, value):
            super().__setitem__(key, value)

        def items(self):
            return iter((x, subclass_object(y)) for x, y in super().items())

else:
    raise Exception('Unknow Pythn version!')
