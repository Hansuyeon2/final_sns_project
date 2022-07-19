from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog,Comment
from .models import Post,Comment2
from django.utils import timezone
from django.core.paginator import Paginator
# Create your views here.



def movie(request) :
    blogs = Blog.objects.all()
    return render(request, 'main/movie.html',{'blogs':blogs})

def picture(request) :
    posts = Post.objects.all()
    return render(request, 'main/picture.html',{'posts':posts})

# movie ---------------------

def detail(request, id):
    blog = get_object_or_404(Blog, pk = id)
    all_comments = blog.comments.all().order_by('-created_at')
    return render(request, 'main/detail_movie.html', {'blog':blog, 'comments':all_comments})
    
def new(request) :
    return render(request, 'main/new_movie.html')


def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.writer = request.user
    new_blog.pub_date = timezone.now()
    new_blog.test_list = request.POST.getlist('test_list')
    new_blog.body = request.POST['body']
    new_blog.image = request.FILES.get('image')
    new_blog.genre = request.POST['genre']
    new_blog.summary = request.POST['summary']
    new_blog.save()

    return redirect('detail',new_blog.id)

def edit(request, id) :
    edit_blog = Blog.objects.get(id = id)
    return render(request, 'main/edit.html', {'blog' : edit_blog})

def update(request, id):
    update_blog = Blog.objects.get(id=id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.user
    update_blog.pub_date = timezone.now()
    update_blog.body = request.POST['body']
    update_blog.image = request.FILES.get('image')
    update_blog.test_list = request.POST.getlist('test_list')
    update_blog.genre = request.POST['genre']
    update_blog.summary = request.POST['summary']
    update_blog.save()
    return redirect('detail', update_blog.id)

def delete(request, id) :
    delete_blog = Blog.objects.get(id = id)
    delete_blog.delete()
    return redirect('movie')

def create_comment(request, blog_id):
   new_comment = Comment()
   new_comment.writer = request.user
   new_comment.content = request.POST['content']
   new_comment.blog = get_object_or_404(Blog, pk = blog_id)
   new_comment.save() 
   return redirect('detail', blog_id)

#picture ---------------------

def post_detail(request, id):
    post = get_object_or_404(Post, pk = id)
    all_comment2s = post.comment2s.all().order_by('-created_at')
    return render(request, 'main/detail_picture.html', {'post':post, 'comment2s':all_comment2s})
   
def post_new(request) :
    return render(request, 'main/new_picture.html')

def post_create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.user
    new_post.pub_date = timezone.now()
    new_post.body = request.POST['body']
    new_post.image = request.FILES.get('image')
    new_post.save()
    return redirect('post_detail',new_post.id)

def post_edit(request, id) :
    edit_post = Post.objects.get(id = id)
    return render(request, 'main/picture_edit.html', {'post' : edit_post})

def post_update(request, id):
    update_post = Post.objects.get(id=id)
    update_post.title = request.POST['title']
    update_post.writer = request.user
    update_post.pub_date = timezone.now()
    update_post.body = request.POST['body']
    update_post.image = request.FILES.get('image')
    update_post.save()
    return redirect('post_detail', update_post.id)

def post_delete(request, id) :
    delete_post = Post.objects.get(id = id)
    delete_post.delete()
    return redirect('picture')

def create_comment2(request, post_id):
   new_comment2 = Comment2()
   new_comment2.writer = request.user
   new_comment2.content = request.POST['content']
   new_comment2.post = get_object_or_404(Post, pk = post_id)
   new_comment2.save() 
   return redirect('post_detail', post_id)


