# -*- coding: utf-8 -*-

from django.db import models
from students.models.student import Student

# Create your models here.

class Group(models.Model):
	"""Group Model"""

	class Meta(object):
		verbose_name = u"Група"
		verbose_name_plural = u"Групи"
		ordering = ['title']
		app_label="students"

	title = models.CharField(
		max_length = 256,
		blank = False,
		verbose_name = u"Назва")

	leader = models.OneToOneField('Student',
		verbose_name = u"Староста",
		blank = True,
		null = True,
		on_delete = models.SET_NULL)

	notes = models.TextField(
		blank = True,
		verbose_name=u"Додаткові нотатки")

	def __unicode__(self):
		if self.leader:
			return u"%s (%s %s)" % (self.title, self.leader.first_name, self.leader.last_name)
