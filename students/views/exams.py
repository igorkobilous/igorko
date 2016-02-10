from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import ModelForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,HTML, Layout
from crispy_forms.bootstrap import FormActions

from ..models import Exam
from ..util import paginate, get_current_group


#Views for exams

def exams_list(request):

    current_group = get_current_group(request)
    if current_group:
        exams = Exam.objects.filter(group=current_group)
    else:
        exams = Exam.objects.all()

    #try to order exams list
    order_by = request.GET.get('order_by', '')
    if order_by in ('subject', 'group', 'date', 'lecturer'):
    	exams = exams.order_by(order_by)
    	if request.GET.get('reverse', '') == '1':
			exams = exams.reverse()

    # paginate groups
    context = paginate(exams, 3, request, {},
        var_name='exams')

    return render(request, 'students/exams_list.html',
		context)

#Exams Update and Create Form

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
            Submit('add_button', _(u"Save"), css_class="btn btn-primary"),
            HTML(u'{% load i18n %}<a class="btn btn-link" href={% url "exams" %}>{% trans "Cancel" %}</a>'),
            )

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
            Submit('add_button', _(u"Save"), css_class="btn btn-primary"),
            Submit('cancel_button', _(u"Cancel"), css_class="btn btn-link"),)

#Exams Update and Create Views

class ExamCreateView(CreateView):
    model = Exam
    template_name = "students/exams_add.html"
    form_class = ExamCreateForm

    def get_success_url(self):
        messages.warning(self.request, _(u"Exam added successfuly!"))
        return reverse('exams')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ExamCreateView, self).dispatch(*args, **kwargs)

class ExamUpdateView(UpdateView):
    model = Exam
    template_name = "students/exams_edit.html"
    form_class = ExamUpdateForm

    def get_success_url(self):
        messages.warning(self.request, _(u"Exam updated successfuly!"))
        return reverse('exams')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.warning(self.request, _(u"Exam updated canceled!"))
            return HttpResponseRedirect(reverse('exams'))
        else:
            return super(ExamUpdateView, self).post(request, *args, **kwargs)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ExamUpdateView, self).dispatch(*args, **kwargs)

class ExamDeleteView(DeleteView):
    model = Exam
    template_name = "students/confirm_delete.html"

    def get_success_url(self):
		messages.warning(self.request, _(u"Exam deleted succesfuly!"))
		return reverse('exams')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ExamDeleteView, self).dispatch(*args, **kwargs)
