from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.http import HttpResponse
import json
from django.contrib.auth.decorators import login_required
# Create your views here.

def introduce(request):
    return render(request, 'main/introduce.html')

def movie(request) :
    posts = Post.objects.all()
    return render(request, 'main/movie.html',{'posts':posts})


# movie ---------------------

def detail(request, id):
    post = get_object_or_404(Post, pk = id)
    all_comments = post.comments.all().order_by('-created_at')
    return render(request, 'main/detail_movie.html', {'post':post, 'comments':all_comments})
    
def new(request) :
    return render(request, 'main/new_movie.html')


def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.user
    new_post.pub_date = timezone.now()
    new_post.test_list = request.POST.getlist('test_list')
    new_post.body = request.POST['body']
    new_post.image = request.FILES.get('image')
    new_post.genre = request.POST['genre']
    new_post.summary = request.POST['summary']
    new_post.save()

    return redirect('main:detail',new_post.id)

def edit(request, id) :
    edit_post = Post.objects.get(id = id)
    return render(request, 'main/edit.html', {'post' : edit_post})

def update(request, id):
    update_post = Post.objects.get(id=id)
    update_post.title = request.POST['title']
    update_post.writer = request.user
    update_post.pub_date = timezone.now()
    update_post.body = request.POST['body']
    update_post.image = request.FILES.get('image')
    update_post.test_list = request.POST.getlist('test_list')
    update_post.genre = request.POST['genre']
    update_post.summary = request.POST['summary']
    update_post.save()
    return redirect('main:detail', update_post.id)

def delete(request, id) :
    delete_post = Post.objects.get(id = id)
    delete_post.delete()
    return redirect('main:movie')

def create_comment(request, post_id):
   new_comment = Comment()
   new_comment.writer = request.user
   new_comment.content = request.POST['content']
   new_comment.post = get_object_or_404(Post, pk = post_id)
   new_comment.save() 
   return redirect('main:detail', post_id)

def edit_comment(request, comment_id):
    edit_comment = Comment.objects.get(id = comment_id)
    return render(request, 'main/comment_edit.html', {'comment' : edit_comment})

def update_comment(request, comment_id):
    update_comment = get_object_or_404(Comment, pk = comment_id)
    update_comment.writer = request.user
    update_comment.content = request.POST['content']
    update_comment.save()
    return redirect('main:detail', update_comment.post.id)    

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return detail(request, comment.post.id)


@require_POST
@login_required
def like_toggle(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    post_like, post_like_created = Like.objects.get_or_create(user=request.user, post=post)

    if not post_like_created:
        post_like.delete()
        result = "like_cancel"
    else:
        result = "like"
    context = {
        "like_count" : post.like_count,
        "result" : result
    }
    return HttpResponse(json.dumps(context), content_type = "application/json")


@require_POST
@login_required
def dislike_toggle(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    post_dislike, post_dislike_created = Dislike.objects.get_or_create(user=request.user, post=post)

    if not post_dislike_created:
        post_dislike.delete()
        result = "dislike_cancel"
    else:
        result = "dislike"
    context = {
        "dislike_count" : post.dislike_count,
        "result" : result
    }
    return HttpResponse(json.dumps(context), content_type = "application/json")



