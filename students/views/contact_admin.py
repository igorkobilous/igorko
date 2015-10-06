# -*- coding: utf-8 -*-
from django.shortcuts import render
from django import forms
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from studentsdb.settings import ADMIN_EMAIL


class ContactForm(forms.Form):

    from_email = forms.EmailField(
    label=u"Ваша Емайл Адреса")

    subject = forms.CharField(
    label=u"Заголовок листа",
    max_length=128)

    message = forms.CharField(
    label=u"Текст повідомлення",
    max_length=2560,
    widget=forms.Textarea)


def contact_admin(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']

            try:
                send_mail(subject, message, from_email, [ADMIN_EMAIL])
            except Exception:
                message = u'Під час вдправки листа виникла непередбачувана помилка.\
                Спробуйте скористатись даною формою пізніше.'
            else:
                message = u'Повідомлення успішно надіслане!'
            return HttpResponseRedirect(u'%s?status_message=%s' % (reverse('contact_admin'), message))

    else:
        form = ContactForm()
    return render(request, 'contact_admin/form.html', {'form':form})
