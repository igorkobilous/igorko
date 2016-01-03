# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import ModelForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib import messages

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,HTML, Layout
from crispy_forms.bootstrap import FormActions

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

class ExamCreateForm(ModelForm):
    class Meta:
        model = Exam
        fields = ['subject', 'date', 'lecturer', 'group', 'notes']

    def __init__(self, *args, **kwargs):
		super(ExamCreateForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		# set form tag attributes

		self.helper.form_action = reverse('exams_add')
		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horizontal'

		# set form field properties

		self.helper.help_text_inline = True
		self.helper.html5_required = True
		self.helper.label_class = 'col-sm-2 control-label'
		self.helper.field_class = 'col-sm-10'

		# add buttons

		self.helper.layout[-1] = FormActions('notes',
            Submit('add_button', u'Зберегти', css_class="btn btn-primary"),
            HTML(u'<a class="btn btn-link" href={% url "exams" %}>Скасувати</a>'),)

class ExamUpdateForm(ModelForm):
    class Meta:
        model = Exam
        fields = ['subject', 'date', 'lecturer', 'group', 'notes']

    def __init__(self, *args, **kwargs):
		super(ExamUpdateForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		# set form tag attributes

		self.helper.form_action = reverse('exams_edit',
			kwargs={'pk': kwargs['instance'].id})
		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horizontal'

		# set form field properties

		self.helper.help_text_inline = True
		self.helper.html5_required = True
		self.helper.label_class = 'col-sm-2 control-label'
		self.helper.field_class = 'col-sm-10'

		# add buttons

		self.helper.layout[-1] = FormActions('notes',
            Submit('add_button', u'Зберегти', css_class="btn btn-primary"),
            Submit('cancel_button', u'Скасувати', css_class="btn btn-link"),)

class ExamCreateView(CreateView):
    model = Exam
    template_name = "students/exams_add.html"
    form_class = ExamCreateForm

    def get_success_url(self):
        messages.warning(self.request, u"Екзамен успішно збережено!")
        return reverse('exams')

    """def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.warning(self.request, u"Ствоерння екзамена скасовано!")
            return HttpResponseRedirect(reverse('exams'))
        else:
            return super(ExamCreateView, self).post(request, *args, **kwargs)"""

class ExamUpdateView(UpdateView):
    model = Exam
    template_name = "students/exams_edit.html"
    form_class = ExamUpdateForm

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
