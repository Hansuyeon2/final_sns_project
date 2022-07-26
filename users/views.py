from django.shortcuts import render
from main.models import *
from django.contrib.auth.models import User


def mypage(request):
    user = request.user

    blogs=Blog.objects.filter(writer=user)
    mycomments = Comment.objects.filter(writer=user)
    like_list = Like.objects.filter(user = user)

    context = {
        'like_list':like_list,
        'blogs':blogs,
    }
    return render(request, 'users/mypage.html', context)




# Create your views here.