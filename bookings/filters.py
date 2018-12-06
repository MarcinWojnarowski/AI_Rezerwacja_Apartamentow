from django_filters import FilterSet, CharFilter, NumberFilter
from bookings.models import Apartament


class ApartamentFilter(FilterSet):
    miejscowosc = CharFilter(label='Miejscowość', lookup_expr='icontains')  # icontains, wyszukiwanie po fragmencie textu
    adres = CharFilter(label='Adres', lookup_expr='icontains')
    cena_za_dobe = NumberFilter(label='Cena za dobę (max)', lookup_expr='lt')  # lt- less than, czyli wszystkie mniejsze
    ilosc_miejsc = NumberFilter(label='Ilość miejsc')

    class Meta:
        model = Apartament
        fields = [
            'miejscowosc',
            'adres',
            'ilosc_miejsc',
            'cena_za_dobe',
            'internet',
            'telewizor',
            'basen',
            'sauna',
        ]
