# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

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