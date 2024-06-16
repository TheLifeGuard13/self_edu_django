import typing

from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from users.models import User


class UserRegisterForm(UserCreationForm):
    """Класс формы регистрации"""

    class Meta:
        model = User
        fields = ("email", "password1", "password2")


class UserProfileForm(UserChangeForm):
    """Класс профиля пользователя"""

    class Meta:
        model = User
        fields = ("email", "phone", "avatar")

    def __init__(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields["password"].widget = forms.HiddenInput()
