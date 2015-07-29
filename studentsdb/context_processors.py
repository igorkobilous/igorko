#from .settings import PORTAL_URL
#from django.http import HttpResponse

#def students_proc(request):
#	PORTAL_URL = request.build_absolute_uri('/')
#	if PORTAL_URL[-1] == '/':
#		return {'PORTAL_URL': PORTAL_URL[:-1]}
#	else:
#		return {'PORTAL_URL': PORTAL_URL}

def students_proc(request):
	return {'PORTAL_URL': request.scheme + '://'+ request.get_host()}