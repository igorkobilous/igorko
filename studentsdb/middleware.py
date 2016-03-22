from datetime import datetime, timedelta, time
from bs4 import BeautifulSoup, Tag, NavigableString

from django.http import HttpResponse
from .settings import TEMPLATE_DEBUG


class RequestTimeMiddleware(object):
    """Display request time on a page"""

    def process_request(self, request):
        request.start_time = datetime.now()
        return None

    def process_response(self, request, response):
        if not TEMPLATE_DEBUG:
            return response
        # if our process_request was canceled somewhere within
        # middleware stack, we can not calculate request time
        if not hasattr(request, 'start_time'):
            return response

        # calculate request execution time
        request.end_time = datetime.now()
        #= timedelta(seconds=1)
        #if (request.end_time - request.start_time) > t:
        #   return HttpResponse('Processing of request too slow. Developer - check of my code!') 
        if 'text/html' in response.get('Content-Type', ''):
           response.write('<br />Request took: %s' % str(
               request.end_time - request.start_time))

        return response

    def process_view(self, request, view, args, kwargs):
        return None
    
    def process_template_response(self, request, response):
        return response

    def process_exception(self, request, exception):
        return None
