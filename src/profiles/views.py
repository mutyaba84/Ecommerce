from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.shortcuts import render
from django.template import Context

# Create your views here.
def home(request):
    context = {}
    template = 'home.html'
    return render(request,template,context)



def about(request):
    context = {}
    template = 'about.html'
    return render(request,template,context)



@login_required(login_url='/accounts/login/')
def userProfile(request):
	user = request.user
	context = {'user': user}
	template = 'profile.html'
	return render(request,template,context)
