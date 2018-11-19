from django.contrib import admin
from bookings.models import Apartament


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
        return obj.wlasciciel.first_name+' '+obj.wlasciciel.last_name
    wypisz_wlasciciela.short_description = 'Właściciel'


admin.site.register(Apartament, ApartamentAdmin)
