from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import MyUser


class CustomUserCreationForm(UserCreationForm):     #formularz do tworzenia nowego użytkownika

    class Meta:
        model = MyUser
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',
                  )


class CustomUserChangeForm(UserChangeForm):   # formularz używany w interfejsie administratora do zmiany informacji i uprawnień użytkownika

    class Meta:
        model = MyUser
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  )
