from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    first_name = models.CharField(blank=False, max_length=30, verbose_name="Imię")
    last_name = models.CharField(blank=False, max_length=100, verbose_name="Nazwisko")
    email = models.EmailField(blank=False)

    def __str__(self):
        return "{uzytkownik} {imie} {nazwisko} {email}".format\
            (uzytkownik=self.username, imie=self.first_name, nazwisko=self.last_name, email=self.email)

