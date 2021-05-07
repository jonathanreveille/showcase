from django.db import models
from .managers import ProjectManager

# Create your models here.
class Tag(models.Model):
    """tag table"""

    name = models.CharField(max_length=100)

    def __str__(self):
        "returns the name in str of the object"
        return self.name

class Project(models.Model):
    """project table"""
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=150, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    image = models.FilePathField(path="static/img", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag)
    repository = models.URLField(max_length=200, null=True, blank=True)

    objects = ProjectManager()

    def __str__(self):
        """returns the title in str of the object"""
        return self.title


    class Meta:
        """Allows to order the object based
        on the attribute"""

        ordering=['-created']
