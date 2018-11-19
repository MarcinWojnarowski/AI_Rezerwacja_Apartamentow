from django.urls import path
from bookings.views import ApartamentListView, UserApartament, apartament_create, szczegoly_apartamentu

urlpatterns = [
    path('list/', ApartamentListView.as_view(), name='apartaments_list'),
    path('list/new_apartament/', apartament_create, name='apartament_create'),
    path('list/<int:pk>/', szczegoly_apartamentu, name='apartament_detail'),
    path('list/my_apartament/', UserApartament.as_view(), name='user_apartament'),
]
