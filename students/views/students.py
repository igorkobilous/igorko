# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime


from ..models import Student, Group

#Views for students

def students_list(request):
	students = Student.objects.all()

	#try to order students list
	order_by = request.GET.get('order_by', '')
	if order_by in ('last_name', 'first_name', 'ticket'):
		students = students.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			students = students.reverse()

	#pagination
	paginator = Paginator(students, 3)
	page = request.GET.get('page')
	try:
		students = paginator.page(page)
	except PageNotAnInteger:
		#If page is not an integer, deliver first page.
		students = paginator.page(1)
	except EmptyPage:
		#If page is out of range (e.g. 9999), deliver
		#last page of results.
		students = paginator.page(paginator.num_pages)

	return render(request, 'students/students_list.html',
		{'students':students})

def students_add(request):
	#was form posted
	if request.method == "POST":
		#was form add button clicked:
		if request.POST.get('add_button') is not None:
			# todo: validate input from user
			errors = {}
			#validate student data will go here
			data = {'middle_name': request.POST.get('middle_name'),
			'notes': request.POST.get('notes')}
            #validate user input
			first_name = request.POST.get('first_name', '').strip()
			if not first_name:
				errors['first_name'] = u"Ім'я є обов'язковим"
			else:
				data['first_name'] = first_name

			last_name = request.POST.get('last_name', '').strip()
			if not last_name:
				errors['last_name'] = u"Прізвище є обов'язковим"
			else:
				data['last_name'] = last_name

			birthday = request.POST.get('birthday', '').strip()
			if not birthday:
				errors['birthday'] = u"Дата народження є обовязковою"
			else:
				try:
					datetime.strptime(birthday, '%Y-%m-%d')
				except Exception:
					errors['birthday'] = u"Введіть коректний формат дати(напр. 1984-12-30)"
				else:
					data['birthday'] = birthday

			ticket = request.POST.get('ticket', '').strip()
			if not ticket:
				errors['ticket'] = u"Номер білет є обовязковим"
			else:
				data['ticket'] = ticket

			student_group = request.POST.get('student_group', '').strip()
			if not student_group:
				errors['student_group'] = u"Оберіть групу для студента"
			else:
				groups = Group.objects.filter(pk=student_group)
				if len(groups) != 1:
					errors['student_group'] = u"Оберіть коректну групу"
				else:
					data['student_group'] = groups[0]

			photo = request.FILES.get('photo')
			if not photo:
				errors['photo'] = u"Фото є обов'язковим полем"
			else:
				photo_format = {'jpeg':1, 'png':2, 'gif':3, 'jpg':4}
				photo_name = request.FILES.get('photo').name
				photo_data = ''
				if request.FILES.get('photo').size >= 2000000:
					errors['photo'] = u"Розмір файла не повинен перевищувати 2Мб"
				else:
					for i in photo_format:
						if photo_name.find(i) != -1:
							photo_data += '1'
					if len(photo_data) > 0:
						data['photo'] = photo
					else:
						errors['photo'] = u"Використовуйте фото форматом (.jpeg, .jpg, .gif, .png)"

			if not errors:
				#create student object
				student = Student(**data)
				student.save()

				#redirect user to students list
				return HttpResponseRedirect(u'%s?status_message=Студента успішно додано!' % reverse('home'))

			else:
				#render form with errors and previous user input
				return render(request, 'students/students_add.html',
					{'groups': Group.objects.all().order_by('title'),
					'errors':errors})
		elif request.POST.get('cancel_button') is not None:
			#redirect to home page on cancel button
			return HttpResponseRedirect(u'%s?status_message=Додавання студента скасовано!' % reverse('home'))
	else:
		#initial form render
		return render(request, 'students/students_add.html',
			{'groups': Group.objects.all().order_by('title')})


def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)
