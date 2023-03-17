from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.views import generic
from django.urls import reverse_lazy
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from .forms import RegisterUserForm, EditProfileForm, PasswordChangingForm, EditPersonalForm
from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from community_blog.models import Profile, Post


class EditPersonalView(generic.UpdateView):
    form_class = EditPersonalForm
    model = Profile
    template_name = 'registration/edit_personal_info.html'
    success_url = reverse_lazy('community')


def ShowProfileView(request, pk=None):
    if pk:
        post_owner = get_object_or_404(User, pk=pk)
        user_posts = Post.objects.filter(author_id=pk)
        user_likes = Post.objects.filter(likes__in=[pk])

    else:
        post_owner = request
        user_posts = Post.objects.filter(author_id=pk)
        user_likes = Post.objects.filter(likes__in=[pk])

    return render(request, '../templates/registration/user_profile.html', {'post_owner': post_owner, 'user_posts': user_posts, 'user_likes': user_likes})


class UserRegisterView(generic.CreateView):
    form_class = RegisterUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('community')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('change_passwd_success')


class CreateProfilePageView(CreateView):
    model = Profile
    form_class = EditPersonalForm
    template_name = 'registration/create_profile.html'
    success_url = reverse_lazy('community')
    # fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
