from django.shortcuts import render
from django.conf import settings
from .forms import *
from django.contrib import messages

#from myapp.forms import ContactForm
from django.views.generic.edit import *

# new imports that go at the top of the file
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template


def contact(request):
    title = 'Contact'
    form = ContactForm(request.POST or None)
    comfirm_message = None


    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'Message from MYSITE.com'
        message = '%s %s' %(comment, name)
        emailFrom = form.cleaned_data['email']
        emailto = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailFrom, emailto, fail_silently=True)
        title = "Thanks!"
        confirm_message = "Thanks for the message. We will get right back to you."
        form = None

    context = {'title': title, 'form': form, 'comfirm_message': comfirm_message,}
    template = 'contact.html'
    return render(request,template,context)
       



       

   