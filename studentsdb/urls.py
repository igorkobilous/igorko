"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from students.views.students import StudentUpdateView, StudentDeleteView, students_list, students_add
from students.views.groups import GroupUpdateView, GroupCreateView, GroupDeleteView, groups_list
from students.views.exams import ExamCreateView, ExamUpdateView, ExamDeleteView, exams_list
from students.views.journal import JournalView
from students.models import Group

from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.views.generic.base import RedirectView, TemplateView

from .settings import MEDIA_ROOT, DEBUG

js_info_dict = {
    'packages': ('students',),
}

urlpatterns = patterns('',
    # Students urls
    url(r'^$', 'students.views.students.students_list', name='home'),
    url(r'^students/add/$', login_required(students_add),
        name='students_add'),
    url(r'^students/(?P<pk>\d+)/edit/$',
        login_required(StudentUpdateView.as_view()),
        name='students_edit'),
    url(r'^students/(?P<pk>\d+)/delete/$',
        login_required(StudentDeleteView.as_view()),
        name='students_delete'),


    # Groups urls
    url(r'^groups/$', login_required(groups_list), name='groups'),
    url(r'^groups/add/$', login_required(GroupCreateView.as_view()),
        name='groups_add'),
    url(r'^groups/(?P<pk>\d+)/edit/$',
        login_required(GroupUpdateView.as_view()),
        name='groups_edit'),
    url(r'^groups/(?P<pk>\d+)/delete/$',
        login_required(GroupDeleteView.as_view()),
        name='groups_delete'),

    #Journal urls
    url(r'journal/(?P<pk>\d+)?/?$', JournalView.as_view(), name='journal'),

    #Exams urls
    url(r'^exams/$', login_required(exams_list),  name='exams'),
    url(r'^exams/add/$',
        login_required(ExamCreateView.as_view()),
        name='exams_add'),
    url(r'^exams/(?P<pk>\d+)/edit/$',
        login_required(ExamUpdateView.as_view()),
        name='exams_edit'),
    url(r'^exams/(?P<pk>\d+)/delete/$',
        login_required(ExamDeleteView.as_view()),
        name='exams_delete'),

    # User Related urls
    url(r'^users/profile/$', login_required(TemplateView.as_view(
        template_name='registration/profile.html')), name='profile'),
    url(r'^users/logout/$', auth_views.logout, kwargs={'next_page': 'home'},
        name='auth_logout'),
    url(r'^register/complete/$', RedirectView.as_view(pattern_name='home'),
        name='registration_complete'),
    url(r'^users/', include('registration.backends.simple.urls',
        namespace='users')),


    # Social Auth Related urls
    url('^social/', include('social.apps.django_app.urls', namespace='social')),
    
    url(r'^admin/', include(admin.site.urls)),

    url(r'^jsi18n\.js$', 'django.views.i18n.javascript_catalog', js_info_dict),

    url(r'^i18n/', include('django.conf.urls.i18n')),

    #Contact Admin form
    url(r'^contact-admin/$', 'students.views.contact_admin.contact_admin',
        name='contact_admin')
    )


if DEBUG:
    # serve files from media folder
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': MEDIA_ROOT}))
