from django.core.management.base import BaseCommand
from django.utils import timezone

from students.models.student import Student
from students.models.group import Group
from django.contrib.auth.models import User

class Command(BaseCommand):
	help = "Prints to console number of student related objects in a database."

	args = '<model_name model_name...>'

	def handle(self, *args, **options):
		if 'group' in args:
			for i in range(1, 2):
				grp = Group(title='Test')
				grp.save()
			if grp:
				self.stdout.write('Groups create')
		if 'student' in args:
			for i in range(1, 2):
				stud = Student(first_name='Test', last_name='Test', 
					birthday = timezone.now(), ticket='244')
				stud.save()
			if stud:
				self.stdout.write('Students create')

		

		