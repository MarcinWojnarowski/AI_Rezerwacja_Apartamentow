from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.forms import CustomUserChangeForm, CustomUserCreationForm
from accounts.models import MyUser


class UsersAdmin(UserAdmin):
    add_form = CustomUserCreationForm          # formularz tworzenia nowego użytkownika
    form = CustomUserChangeForm                # formularz zmian informacji o danym użytkowniku
    model = MyUser                             # pobiera model użytkownika
    list_display = ['username',                # lista wyświetlanych danych
                    'first_name',
                    'last_name',
                    'email']
    search_fields = ['username']               # wyszukiwanie po nazwie użytkownika
    ordering = ['username']                    # posortowane po nazwie użytkownika


admin.site.register(MyUser, UsersAdmin)
