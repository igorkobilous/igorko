# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

#Views for students

def students_list(request):
	students = (
		{'id': 1,
		'first_name': u'Оля',
		'last_name': u'Білаш',
		'ticket': 2123,
		'image': 'static/img/olya.jpg'},
		{'id': 2,
		'first_name': u'Ігор',
		'last_name': u'Білоус',
		'ticket': 254,
		'image': 'static/img/igorko.jpg'},
		{'id': 3,
		'first_name': u'Володимир',
		'last_name': u'Юзифишин',
		'ticket': 176,
		'image': 'static/img/volodya.jpg'},
	)
	return render(request, 'students/students_list.html',
		{'students': students})

def students_add(request):
    return HttpResponse('<h1>Students Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

#Views for groups

def groups_list(request):
    groups = (
        {'id': 1,
         'name': u'КА-31',
         'leader': {'id': 1, 'name': u'Білаш Оля'}},
        {'id': 2,
         'name': u'КБ-31',
         'leader': {'id': 2, 'name': u'Білоус Ігор'}},
         {'id': 3,
         'name': u'КТ-31',
         'leader': {'id': 3, 'name': u'Юзифишин Володимир'}},
    )
    return render(request, 'students/groups_list.html',
        {'groups': groups})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)


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

