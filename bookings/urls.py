from django.urls import path
from django_filters.views import FilterView
from bookings.filters import ApartamentFilter
from bookings.views import ApartamentListView, UserApartament, apartament_create, szczegoly_apartamentu, \
    rezerwacje_apartamentow, rezerwacja

urlpatterns = [
    path('list/', ApartamentListView.as_view(), name='apartaments_list'),
    path('list/new_apartament/', apartament_create, name='apartament_create'),
    path('list/<int:pk>/', szczegoly_apartamentu, name='apartament_detail'),
    path('list/my_apartament/', UserApartament.as_view(), name='user_apartament'),
    path('rezerwacje', rezerwacje_apartamentow, name='rezerwacje_apartamentow'),
    path('search/', FilterView.as_view(filterset_class=ApartamentFilter,
                                       template_name='apartament/search.html'), name='search'),
    path('list/rezerwacja/<int:pk>/', rezerwacja, name='rezerwacja'),
]
