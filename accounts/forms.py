from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import KyuskUser


class KyuskUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = KyuskUser
        fields = ("username","email","age")


class KyuskUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = KyuskUser
        fields = ("username","email","age")
