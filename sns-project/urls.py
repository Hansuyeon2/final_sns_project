"""simbathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.introduce,name="introduce"),
    path('movie/', views.movie, name="movie"),
    path('picture/', views.picture, name="picture"),
    path('detail/<int:id>/',views.detail, name="detail"),
    path('post_detail/<int:id>/',views.post_detail, name="post_detail"),
    path('new/', views.new, name="new"),
    path('post_new/', views.post_new, name="post_new"),
    path('create/',views.create, name="create"),
    path('post_create/',views.post_create, name="post_create"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('post_edit/<int:id>', views.post_edit, name="post_edit"),
    path('update/<int:id>', views.update, name="update"),
    path('post_update/<int:id>', views.post_update, name="post_update"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('post_delete/<int:id>', views.post_delete, name="post_delete"),
    path('accounts/',include('allauth.urls')),
    path('<int:blog_id>/create_comment', views.create_comment, name="create_comment"),
    path('<int:post_id>/create_comment2', views.create_comment2, name="create_comment2"),
    ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
