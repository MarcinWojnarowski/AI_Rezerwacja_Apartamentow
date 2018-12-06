from django import forms
from bookings import models


class ApartamentForm(forms.ModelForm):

    class Meta:  # pola które będą wyświetlane w formularzu, podczas tworzenia nowego apartamentu
        model = models.Apartament
        fields = [
            'miejscowosc',
            'adres',
            'opis',
            'ilosc_miejsc',
            'cena_za_dobe',
            'internet',
            'telewizor',
            'basen',
            'sauna',
        ]
