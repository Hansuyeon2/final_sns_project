from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200,null=True)
    writer = models.ForeignKey(User,on_delete=models.CASCADE)
    genre = models.CharField(max_length=200,null=True)
    summary = models.CharField(max_length=200,null=True)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = "post/", blank=True, null=True)
    test_list = models.TextField(blank=False,null=True)
    like_user_set = models.ManyToManyField(User, blank=True, related_name='likes_user_set',through='Like')
    dislike_user_set = models.ManyToManyField(User, blank=True, related_name='dislikes_user_set',through='Dislike')
    @property
    def like_count(self):
        return self.like_user_set.count()  
    @property
    def dislike_count(self):
        return self.dislike_user_set.count()

    def form_valid(self, form):
        test = form.save(commit=False)
        test.test_list = json.dumps(self.request.POST.getlist('test_list'))
        test.save()
        return super().form_valid(form)




class Comment(models.Model):
   content = models.TextField()
   writer = models.ForeignKey(User, on_delete=models.CASCADE)
   post = models.ForeignKey( Post ,on_delete=models.CASCADE, related_name ='comments',null=True)
   created_at = models.DateTimeField(auto_now_add=True)
   update_at = models.DateTimeField(auto_now=True)




class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together =(('user', 'post'))

class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
         unique_together = (('user', 'post'))