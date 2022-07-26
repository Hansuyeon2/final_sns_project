from django.urls import path
from .views import *

app_name='main'
urlpatterns = [
    path('',introduce,name="introduce"),
    path('movie/', movie, name="movie"),
    path('picture/', picture, name="picture"),
    path('detail/<int:id>/',detail, name="detail"),
    path('post_detail/<int:id>/',post_detail, name="post_detail"),
    path('new/', new, name="new"),
    path('post_new/', post_new, name="post_new"),
    path('create/',create, name="create"),
    path('post_create/',post_create, name="post_create"),
    path('edit/<int:id>', edit, name="edit"),
    path('post_edit/<int:id>', post_edit, name="post_edit"),
    path('update/<int:id>', update, name="update"),
    path('post_update/<int:id>', post_update, name="post_update"),
    path('delete/<int:id>', delete, name="delete"),
    path('post_delete/<int:id>', post_delete, name="post_delete"),
    path('<int:blog_id>/create_comment', create_comment, name="create_comment"),
    path('<str:comment_id>/edit_comment', edit_comment, name="edit_comment"),
    path('delete_comment/<int:comment_id>', delete_comment, name='delete_comment'),
    path('<str:comment_id>/update_comment', update_comment, name="update_comment"),
    path('<int:post_id>/create_comment2', create_comment2, name="create_comment2"),
    path('like_toggle/<int:blog_id>/',like_toggle,name="like_toggle"),
    path('dislike_toggle/<int:blog_id>/',dislike_toggle,name="dislike_toggle"),
]