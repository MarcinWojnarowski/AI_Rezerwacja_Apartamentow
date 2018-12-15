from django.contrib import admin
from bookings.models import Apartament, Rezerwacja, Komentarz


class ApartamentAdmin(admin.ModelAdmin):
    search_fields = ['miejscowosc']
    ordering = ['miejscowosc']
    list_display = ['miejscowosc',
                    'adres',
                    'internet',
                    'telewizor',
                    'basen',
                    'sauna',
                    'ilosc_miejsc',
                    'cena_za_dobe',
                    'wypisz_wlasciciela',
                    ]

    def wypisz_wlasciciela(self, obj):
        return obj.wlasciciel.first_name + ' ' + obj.wlasciciel.last_name

    wypisz_wlasciciela.short_description = 'Właściciel'


class RezerwacjaAdmin(admin.ModelAdmin):
    list_display = [
        'apartament_adres',
        'wlasciciel',
        'rezerwacja_od',
        'rezerwacja_do',
        'status'
    ]

    def apartament_adres(self, obj):
        return obj.apartament.miejscowosc + ' ' + obj.apartament.adres

    def wlasciciel(self, obj):
        return obj.kto.first_name + ' ' + obj.kto.last_name

    apartament_adres.short_description = 'Adres apartamentu'
    wlasciciel.short_description = 'Właściciel'


class KomentarzeAdmin(admin.ModelAdmin):
    list_display = [
        'autor_kom',
        'apartament_adres',
        'dodano_dnia',
        'tresc',
        'odpowiedz',
        'odpowiedz_data'
    ]

    def apartament_adres(self, obj):
        return obj.apartament.miejscowosc+' '+obj.apartament.adres

    def autor_kom(self, obj):
        return obj.autor.username

    def tresc(self, obj):
        return obj.tresc_kom

    apartament_adres.short_description = 'Skomentowany apartament'
    autor_kom.short_description = 'Autor'
    tresc.short_description = 'Treść'


admin.site.register(Apartament, ApartamentAdmin)
admin.site.register(Rezerwacja, RezerwacjaAdmin)
admin.site.register(Komentarz, KomentarzeAdmin)
