from django.db import models
from .managers import PostManager

# Create your models here.
class Category(models.Model):
    """category table"""

    name = models.CharField(max_length=50)

    def __str__(self):
        """return the name in str of the object"""
        return self.name

class Post(models.Model):
    """post table"""

    title = models.CharField(max_length=200)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

    objects = PostManager()

    def __str__(self):
        """returns the title in str of the object"""
        return self.title

    class Meta:
        """for order the objects base on an attribute"""
        
        ordering = ['-created_on']