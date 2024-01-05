from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import App_Posts.templates


# Create your views here.

@login_required
def home(request):
    return render(request, 'App_Posts/home.html', context={'title': 'Home'})
