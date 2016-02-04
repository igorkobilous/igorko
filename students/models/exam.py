from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Exam(models.Model):
	"""Exam Model"""

	class Meta(object):
		verbose_name = _(u"Exam")
		verbose_name_plural = _(u"Exams")
		ordering = ['subject']
		app_label = "students"

	subject = models.CharField(
		max_length = 256,
		blank = False,
		verbose_name = _(u"Subject"))

	date = models.DateField(
		blank = True,
		verbose_name = _(u"Date"),)

	lecturer = models.CharField(
		max_length = 256,
		blank = False,
		verbose_name = _(u"Lecturer"),)

	group = models.ForeignKey('Group',
		verbose_name = _(u"Group"),
		blank = False,
		null = True,
		on_delete=models.PROTECT)

	notes = models.TextField(
		blank = True,
		verbose_name = _(u"Additional note"))

	def __unicode__(self):
		return u"%s %s" % (self.subject, self.group)
