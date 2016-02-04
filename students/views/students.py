from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.forms import ModelForm

from django.utils.translation import ugettext as _
from django.contrib import messages
from datetime import datetime
from django.core.exceptions import ValidationError
from django import forms
from PIL import Image

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from crispy_forms.bootstrap import FormActions

from ..models import Student, Group
from ..util import paginate, get_current_group

#Views for students

def students_list(request):
	#check if we need to show only one group of students
	current_group = get_current_group(request)
	if current_group:
		students = Student.objects.filter(student_group=current_group)
	else:
		students = Student.objects.all()

	#try to order students list
	order_by = request.GET.get('order_by', '')
	if order_by in ('last_name', 'first_name', 'ticket'):
		students = students.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			students = students.reverse()

	#pagination
	context = paginate(students, 3, request, {},
        var_name='students')

	return render(request, 'students/students_list.html', context)



def students_add(request):
	#was form posted
	if request.method == "POST":
		#was form add button clicked:
		if request.POST.get('add_button') is not None:
			# todo: validate input from user
			errors = {}
			#validate student data will go here
			data = {'middle_name': request.POST.get('middle_name'),
			'notes': request.POST.get('notes')}
            #validate user input
			first_name = request.POST.get('first_name', '').strip()
			if not first_name:
				errors['first_name'] = _(u"First Name field is required")
			else:
				data['first_name'] = first_name

			last_name = request.POST.get('last_name', '').strip()
			if not last_name:
				errors['last_name'] = _(u"Last Name field is required")
			else:
				data['last_name'] = last_name

			birthday = request.POST.get('birthday', '').strip()
			if not birthday:
				errors['birthday'] = _(u"Bithday is required")
			else:
				try:
					datetime.strptime(birthday, '%Y-%m-%d')
				except Exception:
					errors['birthday'] = _(u"Please, enter correct date format (e.g. 1984-12-30)")
				else:
					data['birthday'] = birthday

			ticket = request.POST.get('ticket', '').strip()
			if not ticket:
				errors['ticket'] = _(u"Ticket is required")
			else:
				data['ticket'] = ticket

			student_group = request.POST.get('student_group', '').strip()
			if not student_group:
				errors['student_group'] = _(u"Select group for student")
			else:
				groups = Group.objects.filter(pk=student_group)
				if len(groups) != 1:
					errors['student_group'] = _(u"Please, select correct group")
				else:
					data['student_group'] = groups[0]

			photo = request.FILES.get('photo')
			if not photo:
				data['photo'] = photo
			else:
				photo_format = {'jpeg':1, 'png':2, 'gif':3, 'jpg':4}
				photo_data = ''
				if photo.size >= 2000000:
					errors['photo'] = _(u"Photo size should not exceed 2Mb")
				else:
					#if photo.content_type in content_types:
					for i in photo_format:
						if photo.name.find(i) != -1:
							photo_data += '1'
					if len(photo_data) > 0:
						data['photo'] = photo
					else:
						errors['photo'] = _(u"Use the photo format (.jpeg, .jpg, .gif, .png)")

			if not errors:
				#create student object
				student = Student(**data)
				student.save()
				messages.warning(request, _(u"Student added successfuly!"))

				#redirect user to students list
				return HttpResponseRedirect(reverse('home'))
			else:
				#render form with errors and previous user input
				messages.info(request, _(u"Please, correct the following errors!"))
				return render(request, 'students/students_add.html',
					{'groups': Group.objects.all().order_by('title'),
					'errors':errors})
		elif request.POST.get('cancel_button') is not None:
			#redirect to home page on cancel button
			messages.warning(request, _(u"Student added canceled!"))
			return HttpResponseRedirect(reverse('home'))
	else:
		#initial form render
		return render(request, 'students/students_add.html',
			{'groups': Group.objects.all().order_by('title')})


class StudentUpdateForm(ModelForm):
	class Meta:
		model = Student
		fields = ['first_name', 'last_name', 'middle_name', 'birthday', 'photo', 'ticket', 'student_group', 'notes']

	def __init__(self, *args, **kwargs):
		super(StudentUpdateForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		# set form tag attributes

		self.helper.form_action = reverse('students_edit',
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
            Submit('add_button', _(u'Save'), css_class="btn btn-primary"),
            Submit('cancel_button', _(u'Cancel'), css_class="btn btn-link"),)

	def clean_photo(self):
		image = self.cleaned_data.get('photo', False)
		if image:
			img = Image.open(image)

			if len(image) > (2*1024*1024):
				raise ValidationError(_(u'Photo size should not exceed 2Mb'), code='invalid')
			else:
				return self.cleaned_data['photo']


class StudentUpdateView(UpdateView):
	model = Student
	template_name = 'students/students_edit.html'
	form_class = StudentUpdateForm


	def get_success_url(self):
		messages.warning(self.request, _(u"Student updated successfuly"))
		return reverse('home')



	def post(self, request, *args, **kwargs):
		if request.POST.get('cancel_button'):
			messages.warning(self.request, _(u"Student updated canceled"))
			return HttpResponseRedirect(reverse('home'))
		else:
			return super(StudentUpdateView, self).post(request, *args, **kwargs)


class StudentDeleteView(DeleteView):
	model = Student
	template_name = 'students/confirm_delete.html'

	def get_success_url(self):
		messages.warning(self.request, _(u"Student deleted successfuly"))
		return reverse('home')
