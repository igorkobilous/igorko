# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import ModelForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib import messages


from ..models import Exam

#Views for exams

def exams_list(request):

    exams = Exam.objects.all()

    #try to order exams list
    order_by = request.GET.get('order_by', '')
    if order_by in ('subject', 'group', 'date', 'lecturer'):
    	exams = exams.order_by(order_by)
    	if request.GET.get('reverse', '') == '1':
			exams = exams.reverse()

    # paginate groups
    paginator = Paginator(exams, 5)
    page = request.GET.get('page')
    try:
        exams = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        exams = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        exams = paginator.page(paginator.num_pages)

    return render(request, 'students/exams_list.html',
		{'exams':exams})

class ExamForm(ModelForm):
    class Meta:
        model = Exam
        fields = ['subject', 'date', 'lecturer', 'group', 'notes']

class ExamCreateView(CreateView):
    model = Exam
    template_name = "students/exams_add.html"
    form_class = ExamForm

    def get_success_url(self):
        messages.warning(self.request, u"Екзамен успішно збережено!")
        return reverse('exams')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.warning(self.request, u"Ствоерння екзамена скасовано!")
            return HttpResponseRedirect(reverse('exams'))
        else:
            return super(ExamCreateView, self).post(request, *args, **kwargs)

class ExamUpdateView(UpdateView):
    model = Exam
    template_name = "students/exams_edit.html"
    form_class = ExamForm

    def get_success_url(self):
        messages.warning(self.request, u"Екзамен успішно редаговано!")
        return reverse('exams')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.warning(self.request, u"Редагування екзамена скасовано!")
            return HttpResponseRedirect(reverse('exams'))
        else:
            return super(ExamUpdateView, self).post(request, *args, **kwargs)

class ExamDeleteView(DeleteView):
    model = Exam
    template_name = "students/confirm_delete.html"

    def get_success_url(self):
		messages.warning(self.request, u"Екзамен успішно виделано!")
		return reverse('exams')
