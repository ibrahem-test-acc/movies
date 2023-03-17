from django.contrib import admin
from .models import Post, Profile, Movies, Category, Comment

admin.site.register(Post)
admin.site.register(Movies)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)
