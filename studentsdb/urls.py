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
from django.contrib import admin
from students.views.students import StudentUpdateView, StudentDeleteView
from students.views.groups import GroupUpdateView, GroupCreateView, GroupDeleteView
from students.views.exams import ExamCreateView, ExamUpdateView, ExamDeleteView
from students.views.contact_admin import ContactFormView
from students.views.journal import JournalView
from students.models import Group

from .settings import MEDIA_ROOT, DEBUG

urlpatterns = patterns('',
    # Students urls
    url(r'^$', 'students.views.students.students_list', name='home'),
    url(r'^students/add/$', 'students.views.students.students_add',
        name='students_add'),
    url(r'^students/(?P<pk>\d+)/edit/$',
        StudentUpdateView.as_view(),
        name='students_edit'),
    url(r'^students/(?P<pk>\d+)/delete/$',
        StudentDeleteView.as_view(),
        name='students_delete'),


    # Groups urls
    url(r'^groups/$', 'students.views.groups.groups_list', name='groups'),
    url(r'^groups/add/$',
        GroupCreateView.as_view(),
        name='groups_add'),
    url(r'^groups/(?P<pk>\d+)/edit/$',
        GroupUpdateView.as_view(),
        name='groups_edit'),
    url(r'^groups/(?P<pk>\d+)/delete/$',
        GroupDeleteView.as_view(),
        name='groups_delete'),

    #Journal urls
    url(r'journal/(?P<pk>\d+)?/?$', JournalView.as_view(), name='journal'),

    #Exams urls
    url(r'^exams/$', 'students.views.exams.exams_list',  name='exams'),
    url(r'^exams/add/$',
        ExamCreateView.as_view(),
        name='exams_add'),
    url(r'^exams/(?P<pk>\d+)/edit/$',
        ExamUpdateView.as_view(),
        name='exams_edit'),
    url(r'^exams/(?P<pk>\d+)/delete/$',
        ExamDeleteView.as_view(),
        name='exams_delete'),


    url(r'^admin/', include(admin.site.urls)),

    #Contact Admin form
    url(r'^contact-admin/$', ContactFormView.as_view(),
            name = 'contact_admin'),
    )






if DEBUG:
    # serve files from media folder
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': MEDIA_ROOT}))
