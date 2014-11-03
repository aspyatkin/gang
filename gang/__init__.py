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
    def __init__(self, data):
        super(GangList, self).__init__(data)

    def __iter__(self):
        return iter((subclass_object(o) for o in super(GangList, self).__iter__()))

    def __getitem__(self, index):
        return subclass_object(super(GangList, self).__getitem__(index))


class GangDict(dict):
    def __init__(self, iterable=None, **kwarg):
        if iterable is None:
            iterable = {}
        super(GangDict, self).__init__(iterable, **kwarg)

    def __getattr__(self, name):
        if name in self:
            return subclass_object(super(GangDict, self).__getitem__(name))
        else:
            raise AttributeError("'{0}' object has no attribute '{1}'".format(
                self.__class__.__name__, name))

    def __getitem__(self, key):
        if key in self:
            return subclass_object(super(GangDict, self).__getitem__(key))
        else:
            raise KeyError(key)

    def __setattr__(self, name, value):
        super(GangDict, self).__setitem__(name, value)

    def __setitem__(self, key, value):
        super(GangDict, self).__setitem__(key, value)

    def get(self, key, default_value=None):
        if key in self:
            return subclass_object(self[key])
        return default_value


def _py2_dict_items(d):
    return [(x, y) for (x, y) in d.iteritems()]

def _py2_dict_iteritems(d):
    return iter((x, subclass_object(y)) for x, y in super(GangDict, d).iteritems())

def _py3_dict_items(d):
    return iter((x, subclass_object(y)) for x, y in super(GangDict, d).items())


if main_ver == 2:
    GangDict.items = _py2_dict_items
    GangDict.iteritems = _py2_dict_iteritems
elif main_ver == 3:
    GangDict.items = _py3_dict_items
else:
    raise RuntimeError('Unknown Python version!')
