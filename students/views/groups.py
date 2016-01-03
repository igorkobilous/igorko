# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import UpdateView, CreateView
from django.views.generic import DeleteView
from django.forms import ModelForm
from django.contrib import messages
from django.core.exceptions import ValidationError

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Button, HTML, Layout
from crispy_forms.bootstrap import FormActions

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



class GroupCreateForm(ModelForm):
    class Meta:
        model = Group
        fields = ['title', 'leader', 'notes']

    def __init__(self, *args, **kwargs):
		super(GroupCreateForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		# set form tag attributes

		self.helper.form_action = reverse('groups_add')
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
            #Submit('cancel_button', u'Скасувати', css_class="btn btn-link"),
            HTML(u'<a class="btn btn-link" href={% url "groups" %}>Скасувати</a>'),
            )

    def clean_title(self):
        groups = Group.objects.filter(title=self.cleaned_data['title'])
        if len(groups)>0:
            raise ValidationError(u'Така група вже існує. Виберіть іншу назву', code='invalid')
        return self.cleaned_data['title']

class GroupUpdateForm(ModelForm):
    class Meta:
        model = Group
        fields = ['title', 'leader', 'notes']

    def __init__(self, *args, **kwargs):
		super(GroupUpdateForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		# set form tag attributes

		self.helper.form_action = reverse('groups_edit',
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

    def clean_title(self):
        groups = Group.objects.filter(title=self.cleaned_data['title'])
        if len(groups)>0 and self.instance != groups[0]:
            raise ValidationError(u'Така група вже існує. Виберіть іншу назву', code='invalid')
        return self.cleaned_data['title']



class GroupCreateView(CreateView):
    model = Group
    template_name = 'students/groups_add.html'
    form_class = GroupCreateForm


    def get_success_url(self):
        messages.warning(self.request, u"Групу успішно додано!")
        return reverse('groups')

    #import pdb;pdb.set_trace()
    """def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.warning(self.request, u"Додавання групи скасовано!")
            return HttpResponseRedirect(reverse('groups'))
        else:
            return super(GroupCreateView, self).post(request, *args, **kwargs)"""


class GroupUpdateView(UpdateView):
    model = Group
    template_name = 'students/groups_edit.html'
    form_class = GroupUpdateForm

    def get_success_url(self):
        messages.warning(self.request, u"Групу успішно збережено!")
        return reverse('groups')


    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.warning(self.request, u"Редагування групи скасовано!")
            return HttpResponseRedirect(reverse('groups'))
        else:
            return super(GroupUpdateView, self).post(request, *args, **kwargs)



class GroupDeleteView(DeleteView):
	model = Group
	template_name = 'students/confirm_delete.html'

	def get_success_url(self):
		messages.warning(self.request, u"Студента успішно виделано!")
		return reverse('groups')
