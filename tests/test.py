import sys
main_ver = sys.version_info[0]
if main_ver == 2:
    from unittest2 import TestCase
elif main_ver == 3:
    from unittest import TestCase
else:
    raise RuntimeError('Unknown Python version!')
from gang import subclass_object, GangDict, GangList, GangTuple


class GangTestsBunch(TestCase):
    def test_create_dict(self):
        self.assertIsInstance(subclass_object({}), GangDict)

    def test_create_list(self):
        self.assertIsInstance(subclass_object([]), GangList)

    def test_create_tuple(self):
        self.assertIsInstance(subclass_object(()), GangTuple)

    def test_access(self):
        obj = GangDict(hello='world')
        self.assertEqual(obj.hello, 'world')
        self.assertEqual(obj['hello'], 'world')

    def test_subclass_through_dict(self):
        obj = GangDict(hello=dict(world='!'))
        self.assertIsInstance(obj.hello, GangDict)
        self.assertIsInstance(obj['hello'], GangDict)

    def test_attribute_assign(self):
        obj = GangDict({})
        obj.hello = 'world'
        self.assertEqual(obj.hello, 'world')
        self.assertEqual(obj['hello'], 'world')

    def test_key_assign(self):
        obj = GangDict({})
        obj['hello'] = 'world'
        self.assertEqual(obj['hello'], 'world')
        self.assertEqual(obj.hello, 'world')

    def test_missing_attribute(self):
        obj = GangDict({})
        with self.assertRaises(AttributeError):
            obj.missing_attribute

    def test_missing_key(self):
        obj = GangDict({})
        with self.assertRaises(KeyError):
            obj['missing_attribute']

    def test_subclass_through_list(self):
        obj = GangList([dict(hello='world')])
        self.assertIsInstance(obj[0], GangDict)

    def test_iter_list(self):
        obj = GangList([dict(lorem='ipsum'), dict(dolor='sit')])
        for item in obj:
            self.assertIsInstance(item, GangDict)

    def test_iter_dict(self):
        obj = GangDict(lorem=dict(ipsum='dolor'),
                       sit=dict(amet='consectetur'))
        if main_ver == 2:
            for key, val in obj.items():
                self.assertIsInstance(val, GangDict)
            for key, val in obj.iteritems():
                self.assertIsInstance(val, GangDict)
        elif main_ver == 3:
            for key, val in obj.items():
                self.assertIsInstance(val, GangDict)
        else:
            raise RuntimeError('Unknown Python version!')


    def test_get_dict_with_key(self):
        obj = GangDict(hello='world')
        self.assertEqual(obj.get('hello'), 'world')

    def test_get_dict_without_key(self):
        obj = GangDict()
        self.assertEqual(obj.get('hello', 'world'), 'world')
