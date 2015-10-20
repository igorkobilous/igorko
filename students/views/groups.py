# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

from ..models import Student, Group


#Views for groups

def groups_list(request):
    groups = Group.objects.all()

    #try to order groups list
    order_by = request.GET.get('order_by', '')
    if order_by in ('title', 'leader'):
    	groups = groups.order_by(order_by)
    	if request.GET.get('reverse', '') == '1':
			groups = groups.reverse()


 # paginate groups
    paginator = Paginator(groups, 2)
    page = request.GET.get('page')
    try:
        groups = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        groups = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        groups = paginator.page(paginator.num_pages)

    return render(request, 'students/groups_list.html',
        {'groups': groups})


def groups_add(request):

    #was form posted
    if request.method == "POST":
        #was form add button clicke?
        if request.POST.get('add_button') is not None:
            errors = {}
            data = {'notes': request.POST.get('notes')}

            title = request.POST.get('title', '').strip()
            if not title:
                errors['title'] = u"Назва групи є обов'язкова"
            else:
                data['title'] = title


            leader = request.POST.get('leader', '').strip()
            if leader:
                leader_id = Group.objects.values_list('leader_id')
                list_leader_id = []
                student_id = ''

                for i in leader_id:
                    i = str(i)
                    i = i[1:(len(i)-3)]
                    list_leader_id.append(i)
                for i in reversed(leader):
                    if i.isdigit(): student_id += i
                    else: break
                student_id = student_id[::-1]

                if student_id in list_leader_id:
                    errors['leader'] = u"Цей студент є старостою в іншій групі"
                else:
                    data['leader'] = Student.objects.get(pk=leader)

            if not errors:
                group = Group(**data)
                #save it to database
                group.save()
                messages.warning(request, u"Групу %s успіхно додано!" % group.title)
                #redirect user to groups list
                return HttpResponseRedirect(reverse('groups'))
            else:
                #render form with errors and previous user input
                messages.warning(request, u"Будь ласка виправте наступні помилки!")
                return render(request, 'students/groups_add.html',
                    {'students': Student.objects.all().order_by('last_name'),
                    'errors': errors})
        elif request.POST.get('cancel_button') is not None:
            messages.warning(request, u"Додавання групи скасовано!")
            return HttpResponseRedirect(reverse('groups'))

    else:
        return render(request, 'students/groups_add.html',
           {'students': Student.objects.all().order_by('last_name')})

def groups_edit(request, pk):
    if request.method == "POST":
        #was form add button clicke?
        if request.POST.get('add_button') is not None:
            errors = {}
            data = {'notes': request.POST.get('notes')}

            title = request.POST.get('title', '').strip()
            if not title:
                errors['title'] = u"Назва групи є обов'язкова"
            else:
                data['title'] = title


            leader = request.POST.get('leader', '').strip()
            if leader:
                if leader:
                    leader_id = Group.objects.values_list('leader_id')
                    list_leader_id = []
                    student_id = ''

                    for i in leader_id:
                        i = str(i)
                        i = i[1:(len(i)-3)]
                        list_leader_id.append(i)
                    for i in reversed(leader):
                        if i.isdigit(): student_id += i
                        else: break
                    student_id = student_id[::-1]

                    if student_id in list_leader_id:
                        errors['leader'] = u"Цей студент є старостою в іншій групі"
                    else:
                        data['leader'] = Student.objects.get(pk=leader)

            if not errors:
                group = Group(**data)
                #save it to database
                group.save()
                messages.warning(request, u"Групу %s успіхно редаговано!" % group.title)
                #redirect user to groups list
                return HttpResponseRedirect(reverse('groups'))
            else:
                #render form with errors and previous user input
                messages.warning(request, u"Будь ласка виправте наступні помилки!")
                return render(request, 'students/groups_edit.html',
                    {'pk': pk,
                    'students': Student.objects.all().order_by('last_name'),
                    'group': Group.objects.get(pk=pk),
                    'leader': Group.objects.get(pk=pk).leader,
                    'errors': errors})
        elif request.POST.get('cancel_button') is not None:
            messages.warning(request, u"Редагування групи скасовано!")
            return HttpResponseRedirect(reverse('groups'))
    else:
        return render(request, 'students/groups_edit.html',
                {'pk': pk,
                'students': Student.objects.all().order_by('last_name'),
                'group': Group.objects.get(pk=pk),
                'leader': Group.objects.get(pk=pk).leader})

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
