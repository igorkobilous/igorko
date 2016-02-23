from django.core.management.base import BaseCommand

from students.models.student import Student
from students.models.group import Group
from students.models.exam import Exam
from django.contrib.auth.models import User


class Command(BaseCommand):
	args = '<model_name model_name ...>'
	help = "Prints to console number of student related objects in a database."

	def handle(self, *args, **options):
		if 'student' in args:
			self.stdout.write('Number of students in database: %d' % Student.objects.count())
			self.stdout.write('Number of groups in database: %d' % Group.objects.count())
			self.stdout.write('Number of exams in database: %d' % Exam.objects.count())
			self.stdout.write('Number of users in database: %d' % User.objects.count())