from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User,on_delete=models.CASCADE)
    genre = models.CharField(max_length=200,null=True)
    summary = models.CharField(max_length=200,null=True)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = "blog/", blank=True, null=True)
    test_list = models.TextField(blank=False,null=True)
  
        


    def form_valid(self, form):
        test = form.save(commit=False)
        test.test_list = json.dumps(self.request.POST.getlist('test_list'))
        test.save()
        return super().form_valid(form)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = "post/", blank=True, null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]

class Comment(models.Model):
   content = models.TextField()
   writer = models.ForeignKey(User, on_delete=models.CASCADE)
   blog = models.ForeignKey( Blog ,on_delete=models.CASCADE, related_name ='comments')
   created_at = models.DateTimeField(auto_now_add=True)
   update_at = models.DateTimeField(auto_now=True)

class Comment2(models.Model):
   content = models.TextField()
   writer = models.ForeignKey(User, on_delete=models.CASCADE)
   post = models.ForeignKey( Post ,on_delete=models.CASCADE, related_name ='comment2s')
   created_at = models.DateTimeField(auto_now_add=True)
   update_at = models.DateTimeField(auto_now=True)

