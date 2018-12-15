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

    def __str__(self):  # jest to przedstawiciel modelu, gdy chce się go zobrazować w postaci stringa
        return "{miejscowość}, {adres}, ilość miejcs: {ilosc_miejsc}, cena: {cena_za_dobe}, {opis}," \
               " posiada intenet: {internet}, tv: {telewizor}, basen: {basen}, oraz saune: {sauna}," \
               " należy do: {wlasciciel} ".format(miejscowość=self.miejscowosc,
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
        return reverse('apartament_detail', kwargs={'pk': self.pk})  # po wywołaniu tej funkcji zostaniemy przeniesieni na stronę
                                                                     # ze szczegółami apartamentu , apartamentu o danym id


class Rezerwacja(models.Model):
    apartament = models.ForeignKey(Apartament, on_delete=models.CASCADE)
    kto = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rezerwacja_od = models.DateField(db_index=True, null=True)
    rezerwacja_do = models.DateField(db_index=True, null=True)
    STATUSY = (
        ('niezatwierdzony', 'Niezatwierdzony'),
        ('zatwierdzony', 'Zatwierdzony'),
        ('odrzucony', 'Odrzucony')
    )
    status = models.CharField(default='niezatwierdzony', max_length=255, choices=STATUSY)

    def __str__(self):
        return "Rezerwacja od: "+self.rezerwacja_od.strftime('%d.%m.%y') +\
               "Rezerwacja do"+self.rezerwacja_do.strftime('%d.%m.%y') +\
               " Id rezerwującego: "+str(self.kto.id) +\
               " Id apartamentu: "+str(self.apartament.id)


class Komentarz(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    apartament = models.ForeignKey(Apartament, on_delete=models.CASCADE)
    tresc_kom = models.TextField()
    dodano_dnia = models.DateField()
    odpowiedz = models.TextField(null=True)
    odpowiedz_data = models.DateField(null=True)

    def __str__(self):
        return "{autor} {apartament} {tresc_kom} {dodano_dnia} {odpowiedz}".format(
            autor=self.autor,
            apartament=self.apartament,
            tresc_kom=self.tresc_kom,
            dodano_dnia=self.dodano_dnia.strftime('%d.%m.%y'),
            odpowiedz=self.odpowiedz,
        )

    def get_absolute_url(self):
        return reverse('dodaj_komentarz', kwargs={'pk': self.pk})
