from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('community')


class Movies(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    movie_name = models.TextField()
    category = models.CharField(max_length=255)
    body = models.TextField()
    movie_poster = models.ImageField(
        null=False, blank=False, upload_to='images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='community_blog')
    Publication_date = models.DateTimeField(auto_now_add=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' @' + str(self.author)

    def get_absolute_url(self):
        return reverse('community')


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.author)


class Profile(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(
        null=True, blank=True, upload_to='images/profile')
    fb_url = models.URLField(max_length=200, null=True, blank=True)
    tw_url = models.URLField(max_length=200, null=True, blank=True)
    insta_url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.user)
