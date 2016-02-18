from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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