from django import db
from . import models
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class PostManager(db.models.Manager):

    def create_paginator(self, post_found, per_page, request):
        """method for paginator generator for product in
        search.html. We will set with per_page param
        that only 6 products will be available on 1
        sheet"""

        paginator = Paginator(post_found, per_page)
        page_number = request.GET.get("page")
        try:
            page_obj = paginator.get_page(page_number)
        except PageNotAnInteger:
            page_obj = paginator.get_page(1)
        except EmptyPage:
            page_obj = paginator.get_page(paginator.num_pages)

        return page_obj
