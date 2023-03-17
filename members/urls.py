from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfileView, EditPersonalView, CreateProfilePageView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(
        template_name='registration/change-password.html'), name='change_passwd'),
    path('change_password_success/', PasswordsChangeView.as_view(
        template_name='registration/change-password-success.html'), name='change_passwd_success'),
    path('<int:pk>/profile', ShowProfileView,
         name='show_personal_profile'),
    path('<int:pk>/profile', ShowProfileView, name='show_profile'),
    path('<int:pk>/edit_personal_info',
         EditPersonalView.as_view(), name='edit_personal'),
    path('create_profile_page',
         CreateProfilePageView.as_view(), name='create_profile'),
]
