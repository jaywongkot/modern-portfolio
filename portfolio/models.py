from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ImageField(upload_to='projects/')
    categories = models.ManyToManyField('Category', related_name='projects')
    client = models.CharField(max_length=100, default='CLIENT NAME')
    project_date = models.CharField(max_length=20, default='M/D/Y')

    def __str__(self):
        return self.title
