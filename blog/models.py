from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modifield = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField('Category', related_name='posts')

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
