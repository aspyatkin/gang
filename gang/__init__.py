def subclass_object(obj):
    if type(obj) == dict:
        return GangDict(obj)
    elif type(obj) == list:
        return GangList(obj)
    elif type(obj) == tuple:
        return GangTuple(obj)
    return obj


class GangTuple(tuple):
    def __init__(self, iterable):
        super(GangTuple, self).__init__(iterable)


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

    def __getitem__(self, name):
        if name in self:
            return subclass_object(super(GangDict, self).__getitem__(name))
        else:
            raise KeyError('No key {name}'.format(name=name))

    def iteritems(self):
        return iter((x, subclass_object(y)) for x, y in super(GangDict, self).iteritems())
