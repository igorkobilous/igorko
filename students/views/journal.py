# -*- coding: utf-8 -*-
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from calendar import monthrange, weekday, day_abbr

from django.http import JsonResponse
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView

from ..models import MonthJournal, Student
from ..util import paginate, get_current_group

class JournalView(TemplateView):
	template_name = 'students/journal.html'

	def get_context_data(self, **kwargs):
		# get context data from TemplateView class
		context = super(JournalView, self).get_context_data(**kwargs)

		if self.request.GET.get('month'):
			month = datetime.strptime(self.request.GET['month'], '%Y-%m-%d').date()
		else:
			today = datetime.today()
			month = date(today.year, today.month, 1)

		next_month = month + relativedelta(months=1)
		prev_month = month - relativedelta(months=1)
		context['prev_month'] = prev_month.strftime('%Y-%m-%d')
		context['next_month'] = next_month.strftime('%Y-%m-%d')
		context['year'] = month.year
		context['month_verbose'] = month.strftime('%B')

		context['cur_month'] = month.strftime('%Y-%m-%d')

		myear, mmonth = month.year, month.month
		number_of_days = monthrange(myear, mmonth)[1]

		context['month_header'] = [{'day': d,
			'verbose': day_abbr[weekday(myear, mmonth, d)][:2]}
			for d in range(1, number_of_days+1)]

		current_group = get_current_group(self.request)
		if current_group:
			queryset = Student.objects.filter(student_group=current_group).order_by('last_name')
		elif kwargs.get('pk'):
			queryset = [Student.objects.get(pk=kwargs['pk'])]
		else:
			queryset = Student.objects.all().order_by('last_name')

		update_url = reverse('journal')

		students = []
		for student in queryset:
			try:
				journal = MonthJournal.objects.get(student = student, date = month)
			except Exception:
				journal = None

			days = []
			for day in range(1, number_of_days+1):
				days.append({
					'day': day,
					'present': journal and getattr(journal, 'present_day%d' % day, False) or False,
					'date': date(myear, mmonth, day).strftime(
					'%Y-%m-%d'),
					})
			# набиваємо усі решту даних студента
			students.append({
				'fullname': u'%s %s' % (student.last_name, student.first_name),
				'days': days,
				'id': student.id,
				'update_url': update_url,
				})
		# застосовуємо піганацію до списку студентів
		context = paginate(students, 10, self.request, context,
			var_name='students')
		# повертаємо оновлений словник із даними
		return context
	#import pdb;pdb.set_trace()
	def post(self, request, *args, **kwargs):
		data = request.POST

		# prepare student, dates and presence data
		current_date = datetime.strptime(data['date'], '%Y-%m-%d').date()
		month = date(current_date.year, current_date.month, 1)
		present = data['present'] and True or False
		student = Student.objects.get(pk=data['pk'])

		# get or create journal object for given student and month
		journal = MonthJournal.objects.get_or_create(student=student,
			date=month)[0]

		# set new presence on journal for given student and save result
		setattr(journal, 'present_day%d' % current_date.day, present)
		journal.save()
		return JsonResponse({'status': 'success'})