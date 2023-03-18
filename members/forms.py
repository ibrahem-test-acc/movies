from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from community_blog.models import Profile
# from django.contrib.auth.forms import AuthenticationForm, UsernameField

# class CustomAuthenticationForm(AuthenticationForm):
#     username = UsernameField(
#         label=("Email"), widget=forms.TextInput(attrs={"autofocus": True})
#     )


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',
                  'email', 'first_name', 'last_name')


class EditProfileForm(UserChangeForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')


class EditPersonalForm(forms.ModelForm):
    bio = forms.CharField(max_length=200, widget=forms.Textarea(
        attrs={'class': 'form-control'}))
    fb_url = forms.URLField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    insta_url = forms.URLField(
        required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    tw_url = forms.URLField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    profile_pic = forms.ImageField()

    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'fb_url', 'tw_url', 'insta_url')


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Old Password', 'width': '100%'}), label='')
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'New Password'}), label='')
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Confirm Password'}), label='')

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
