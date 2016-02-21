from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import UpdateView
from django.forms import ModelForm

from django.utils.translation import ugettext as _
from django.contrib import messages

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, HTML
from crispy_forms.bootstrap import FormActions

from .models import StProfile


def users_list(request):
	#check if we need to show only one group of students
	users = User.objects.all()

	#try to order students list
	order_by = request.GET.get('order_by', '')
	if order_by in ('username', 'date_joined'):
		users = users.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			users = users.reverse()

	return render(request, 'registration/users_list.html', {'users': users})

class UserUpdateForm(ModelForm):
	class Meta:
		model = User
		fields = ['email','username','first_name','last_name']

	def __init__(self, *args, **kwargs):
		super(UserUpdateForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		# set form tag attributes

		self.helper.form_action = reverse('profile_settings',
			kwargs={'pk': kwargs['instance'].id})
		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horizontal'

		# set form field properties

		self.helper.help_text_inline = True
		self.helper.html5_required = True
		self.helper.label_class = 'col-sm-2 control-label'
		self.helper.field_class = 'col-sm-10'

		# add buttons

		self.helper.layout[-1] = FormActions('last_name',
            Submit('add_button', _(u'Save'), css_class="btn btn-primary"),
            Submit('cancel_button', _(u'Cancel'), css_class="btn btn-link"),
			)

class UserUpdateView(UpdateView):
	model = User
	template_name = 'registration/profile_settings.html'
	form_class = UserUpdateForm

	def get_success_url(self):
		messages.warning(self.request, _(u"User updated successfuly"))
		return reverse('profile')

	def post(self, request, *args, **kwargs):
		if request.POST.get('cancel_button'):
			messages.warning(self.request, _(u"User updated canceled"))
			return HttpResponseRedirect(reverse('profile'))
		else:
			return super(UserUpdateView, self).post(request, *args, **kwargs)

