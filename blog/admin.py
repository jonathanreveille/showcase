from django.contrib import admin
from  blog.models import Category, Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("title","created_on")
    list_filter = ("created_on",)
    search_fields = ["title", "body"]

admin.site.register(Category)
admin.site.register(Post, PostAdmin)