# -*- coding: utf-8 -*-
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.forms import ModelForm, ValidationError

from .models import Student, Group, Exam, MonthJournal

class StudentForAdmin(ModelForm):

    def clean_student_group(self):
        """Check if student is leader in any group.

        If yes, then ensure it's the same as selected froup."""
        #get group where current student is a leader
        groups = Group.objects.filter(leader=self.instance)
        if len(groups) > 0 and self.cleaned_data['student_group'] != groups[0]:
            raise ValidationError(u'Студент є старостою іншої групи', code='invalid')
        return self.cleaned_data['student_group']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'ticket', 'student_group']
    list_display_links = ['last_name', 'first_name']
    list_editable = ['student_group']
    ordering = ['last_name']
    list_filter = ['student_group']
    list_per_page = 10
    search_fields = ['last_name', 'first_name', 'middle_name', 'ticket', 'notes']
    form = StudentForAdmin

    def view_on_site(self, obj):
        return reverse('students_edit', kwargs={'pk': obj.id})

class GroupForAdmin(ModelForm):
    #pass
    def clean_title(self):
        groups = Group.objects.filter(title=self.cleaned_data['title'])
        if len(groups)>0 and self.instance != groups[0]:
            raise ValidationError(u'Така група вже існує. Виберіть іншу назву', code='invalid')
        return self.cleaned_data['title']
        #import pdb;pdb.set_trace()


class GroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'leader']
    list_display_links = ['title']
    list_editable = ['leader']
    ordering = ['title']
    list_per_page = 3
    search_fields = ['title', 'leader__last_name', 'notes']
    form = GroupForAdmin

    def view_on_site(self, obj):
        return reverse('groups_edit', kwargs={'pk': obj.id})

class ExamForAdmin(ModelForm):
    pass

class ExamAdmin(admin.ModelAdmin):
    list_display = ['subject', 'date', 'lecturer', 'group']
    list_display_links = ['subject']
    list_editable = ['date', 'group']
    list_filter = ['group', 'subject']
    ordering = ['subject']
    list_per_page = 5
    search_fields = ['subject', 'lecturer', 'group__title', 'notes']
    form = ExamForAdmin

    def view_on_site(self, obj):
        return reverse('exams_edit', kwargs={'pk':obj.id})


# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(MonthJournal)
