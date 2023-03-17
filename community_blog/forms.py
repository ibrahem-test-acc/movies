from django import forms
from django.forms import Form
from .models import Post, Category, Comment
from django.contrib.auth.models import User

categories = Category.objects.all().values_list('name', 'name')
categories_list = []
for item in categories:
    categories_list.append(item)


class PostForm(forms.ModelForm):

    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write Your Opinion About The Movie.....'}),
                           label='')

    class Meta:
        model = Post
        fields = ['title', 'movie_name', 'category',
                  'author', 'body', 'movie_poster']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'movie_name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=categories_list, attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'author', 'value': '', 'type': 'hidden'}),
        }


class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Write Your Comment.....'}), label='')

    class Meta:
        model = Comment
        fields = ['body', 'author']
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'author', 'value': '', 'type': 'hidden'}),
        }
