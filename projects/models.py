from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=150, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    image = models.FilePathField(path="static/img", null=True, blank=True)
    #image = models.ImageField(upload_to="static/projects/images", null=True, blank=True, default='coming_soon.png')
    created = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

#https://www.geeksforgeeks.org/imagefield-django-models/ imageFields