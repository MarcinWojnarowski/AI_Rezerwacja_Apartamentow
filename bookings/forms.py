from django import forms
from bookings import models


class ApartamentForm(forms.ModelForm):

    class Meta:  # pola które będą wyświetlane w formularzu, podczas tworzenia nowego apartamentu
        model = models.Apartament
        widgets = {
          'opis': forms.Textarea(attrs={'rows': 3, 'cols': 30}),
        }
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


class KomentarzForm(forms.ModelForm):

    class Meta:
        model = models.Komentarz
        widgets = {
          'tresc_kom': forms.Textarea(attrs={'rows': 3, 'cols': 30},)
        }
        labels = {'tresc_kom': 'Treść komentarza'}
        fields = [
            'tresc_kom',
        ]
