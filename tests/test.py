from unittest import TestCase
from gang import subclass_object, GangDict, GangList, GangTuple


class GangTestsBunch(TestCase):
	def test_create_dict(self):
		self.assertIsInstance(subclass_object({}), GangDict)

	def test_create_list(self):
		self.assertIsInstance(subclass_object([]), GangList)

	def test_create_tuple(self):
		self.assertIsInstance(subclass_object(()), GangTuple)

	def test_dot_access(self):
		obj = GangDict({'hello': 'world'})
		self.assertEqual(obj.hello, obj['hello'])