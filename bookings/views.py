from django.shortcuts import render
from django.views.generic import ListView
from bookings.models import Apartament
from bookings.forms import ApartamentForm
from django.http import HttpResponseRedirect


class ApartamentListView(ListView): #lista wszystkich apartamentów
    model = Apartament
    template_name = 'apartament/apartament_list.html'


class UserApartament(ListView): #lista apatamentów danego użutkownika
    model = Apartament
    template_name = 'apartament/user_apartament.html'


def apartament_create(request): # funkcja umożliwiająca tworzenie apartamentu
    form = ApartamentForm() # pobiera formularz
    if request.method == 'POST':
        form = ApartamentForm(request.POST)
        if 'apartament_save' in form.data: # gdy na stronie kliknie się przycisk zapisz
            if form.is_valid(): #sprawdza poprawność wprowadzonych danych
                apartament = form.save(commit=False)
                apartament.wlasciciel_id = request.user.id
                apartament.save()
                return HttpResponseRedirect(apartament.get_absolute_url()) # po zapisaniu, zostajemy przekierownani na stronę apartamentu o danym id
    return render(request, 'apartament/apartament_create.html', {'form': form}) # funkcja pobiera 3 argumenty: obiekt request, szablon, i słownik.
                                                    # Dzięki temu po wpisaniu {{form}} w szablonie, na stronie zostanie wyświetlony formularz


def szczegoly_apartamentu(request, pk):
    apartament = Apartament.objects.get(pk=pk)
    if request.user.id == apartament.wlasciciel_id:
        if request.method == 'POST':
            return HttpResponseRedirect(apartament.get_absolute_url())
    return render(request, 'apartament/apartament_detail.html', {'apartament': apartament})
