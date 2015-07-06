# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
#Views for journal

def journal_list(request):
	students_journal = (
		{'id':1,
		'name': u'Білаш Оля'},
		{'id':2,
		'name': u'Білоус Ігор'},
		{'id':3,
		'name': u'Юзифишин Володимир'},
		)
	return render(request, 'students/journal_list.html', {'students_journal': students_journal})