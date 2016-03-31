from django.test import TestCase
from django.http import HttpRequest

from students.models import Student, Group
from students.util import get_groups, get_current_group, paginated


class UtilsTestCase(TestCase):
	"""Test functions from util module"""

	def setUp(self):
		# create group
		group1, created = Group.objects.get_or_create(
			id=1,
			title="Group1")

	def test_get_current_group(self):
		# prepare request object to pass to utility function
		request = HttpRequest()

		# test with no group set in cookie
		request.COOKIES['current_group'] = ''
		self.assertEqual(None, get_current_group(request))

		# test with invalid group id
		request.COOKIES['current_group'] = '12345'
		self.assertEqual(None, get_current_group(request))

		# test with proper group identificator
		group = Group.objects.filter(title='Group1')[0]
		request.COOKIES['current_group'] = str(group.id)
		self.assertEqual(group, get_current_group(request))