from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from App_Login.models import Follow
from App_Posts.models import Posts


# Create your views here.

@login_required
def home(request):
    search = ''
    result = ''
    following_list = Follow.objects.filter(follower=request.user)
    posts = Posts.objects.filter(author__in=following_list.values_list('following'))
    if request.method == "GET":
        search = request.GET.get("search", '')
        result = User.objects.filter(username__icontains=search)
    return render(request, 'App_Posts/home.html',
                  context={'title': 'Home', 'search': search, 'result': result, 'posts': posts})
