# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class Exam(models.Model):
	"""Exam Model"""

	class Meta(object):
		verbose_name = u"Екзамен"
		verbose_name_plural = u"Екзамени"
		ordering = ['subject']
		app_label = "students"

	subject = models.CharField(
		max_length = 256,
		blank = False,
		verbose_name = u"Предмет")

	date = models.DateField(
		blank = True,
		verbose_name = u"Дата",)

	lecturer = models.CharField(
		max_length = 256,
		blank = False,
		verbose_name = u"Викладач",)

	group = models.ForeignKey('Group',
		verbose_name = u"Група",
		blank = False,
		null = True,
		on_delete=models.PROTECT)

	notes = models.TextField(
		blank = True,
		verbose_name = u"Додаткові нотатки")

	def __unicode__(self):
		return u"%s %s" % (self.subject, self.group)
