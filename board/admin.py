from django.contrib import admin

from .models import Post, Comment, Thread

# Register your models here.
admin.site.register([Post, Comment, Thread])
