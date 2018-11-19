from django.db import models
from django.conf import settings
from django.urls import reverse


class Apartament(models.Model):
    wlasciciel = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    miejscowosc = models.CharField(max_length=50)
    adres = models.CharField(max_length=100, unique=True)
    opis = models.CharField(max_length=500)
    ilosc_miejsc = models.SmallIntegerField()
    cena_za_dobe = models.IntegerField()
    internet = models.BooleanField()
    telewizor = models.BooleanField()
    basen = models.BooleanField()
    sauna = models.BooleanField()

    def __str__(self): # jest to przedstawiciel modelu, gdy chce się go zobrazować w postaci stringa
        return "{miejscowość} {adres} {ilosc_miejsc} {cena_za_dobe} {opis} {internet} {telewizor} {basen} {sauna} {wlasciciel} ".format(
            miejscowość=self.miejscowosc,
            adres=self.adres,
            ilosc_miejsc=self.ilosc_miejsc,
            cena_za_dobe=self.cena_za_dobe,
            opis=self.opis,
            internet=self.internet,
            telewizor=self.telewizor,
            basen=self.basen,
            sauna=self.sauna,
            wlasciciel=self.wlasciciel)

    def get_absolute_url(self):
        return reverse('apartament_detail', kwargs={'pk': self.pk}) # po wywołaniu tej funkcji zostaniemy przeniesieni na stronę
                                                                    #  ze szczegółami apartamentu , apartamentu o danym id
