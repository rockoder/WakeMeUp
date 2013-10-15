from django import template
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader

from login.models import Quote

def index(request):
    template = loader.get_template('registration/login.html')
    return HttpResponse("Hello, world.")

def user_home(request):
    if request.user.is_authenticated():
        quote = get_object_or_404(Quote, pk=request.user.userprofile.get_curr_quote_id())
        return render(request, 'registration/user_home.html', {'quote': quote})
    else: # TODO: Need to improve this. html gives problem.
        return render(request, 'registration/login.html', {'invalid_session': True})
