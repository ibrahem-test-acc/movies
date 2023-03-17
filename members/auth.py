from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.db.models import Q


class Email_Auth(BaseBackend):
    # get user by user id
    def get_user(self, user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None

    # authentication
    def authenticate(self, request, username=None, password=None):
        user_model = get_user_model()
        try:
            user = user_model.objects.get(
                Q(username__exact=username) | Q(email__exact=username))
            if user.check_password(password):
                return user
        except user_model.DoesNotExist:
            return None
