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
from crispy_forms.layout import Submit, Layout
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



class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['title', 'leader', 'notes']

    def clean_title(self):
        title = Group.objects.filter(title=self.instance)
        if len(title) == 1:
            raise ValidationError(u'Така назва групи вже існує. Виберіть іншу назву', code='invalid')
        return self.cleaned_data['title']


class GroupCreateView(CreateView):
    model = Group
    template_name = 'students/groups_add.html'
    form_class = GroupForm


    def get_success_url(self):
        messages.warning(self.request, u"Групу успішно додано!")
        return reverse('groups')


    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.warning(self.request, u"Додавання групи скасовано!")
            return HttpResponseRedirect(reverse('groups'))
        else:
            return super(GroupCreateView, self).post(request, *args, **kwargs)


class GroupUpdateView(UpdateView):
    model = Group
    template_name = 'students/groups_edit.html'
    form_class = GroupForm

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
