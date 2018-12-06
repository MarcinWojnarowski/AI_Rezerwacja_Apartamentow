import json
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from datetime import timedelta, datetime
from bookings.filters import ApartamentFilter
from bookings.models import Apartament, Rezerwacja
from bookings.forms import ApartamentForm
from django.http import HttpResponseRedirect


class ApartamentListView(ListView):  # lista wszystkich apartamentów
    model = Apartament
    template_name = 'apartament/apartament_list.html'


class UserApartament(ListView):  # lista apatamentów danego użutkownika
    model = Apartament
    template_name = 'apartament/user_apartament.html'


def apartament_create(request):  # funkcja umożliwiająca tworzenie apartamentu
    form = ApartamentForm()  # pobiera formularz
    if request.method == 'POST':  # jeśli jest to żadanie POST, przetwarza dane formularza
        form = ApartamentForm(request.POST)  # tworzy instancję formularza i zapełnia ją danymi z żądania
        if 'apartament_save' in form.data:  # gdy na stronie kliknie się przycisk zapisz
            if form.is_valid():  # sprawdza poprawność wprowadzonych danych
                apartament = form.save(commit=False)  # tworzy instancję modelu, ale jeszcze nie zapisuje jej w bazie (commit=False)
                apartament.wlasciciel_id = request.user.id  # przypisuje id użytownika do właśiciela apartamentu
                apartament.save()  # zapisuje apartament w bazie danych
                return HttpResponseRedirect(apartament.get_absolute_url())  # po zapisaniu, zostajemy przekierownani na stronę apartamentu o danym id
    return render(request, 'apartament/apartament_create.html', {'form': form})  # funkcja pobiera 3 argumenty: obiekt request, szablon, i słownik.
                                                            # Dzięki temu po wpisaniu {{form}} w szablonie, na stronie zostanie wyświetlony formularz


def szczegoly_apartamentu(request, pk):
    apartament = Apartament.objects.get(pk=pk)
    if request.method == 'POST':
            return HttpResponseRedirect(apartament.get_absolute_url())
    return render(request, 'apartament/apartament_detail.html', {'apartament': apartament})


def rezerwacje_apartamentow(request):
    if request.user.is_authenticated:
        pass
    else:
        messages.add_message(request, messages.WARNING, 'Nie jesteś zalogowany')
        return HttpResponseRedirect(reverse('home'))
    if request.method == 'POST':  # jeśli wysłano żądanie typu POST
        rezerwacja = Rezerwacja.objects.get(pk=request.POST['zmienStatus'])  # pobiera id rezerwacji dla której chcemy zniemić status
        if rezerwacja.apartament.wlasciciel_id == request.user.id:  # sprawdza czy zalogowany uzytkownik jest właścicielem apartamentu
            rezerwacja.status = request.POST['status']  # zmienia status rezerwacji
            rezerwacja.save()
            return HttpResponseRedirect(reverse('rezerwacje_apartamentow'))  # przekierowuje na stronę zarezerwowanych apartamentów
    rezerwacje = Rezerwacja.objects.filter(apartament__wlasciciel_id=request.user.id)  # pobiera rezerwacje apartamentów których właścicielem jest zalogowany użytkownik
    return render(request, 'booking/rezerwacje.html', {'rezerwacje': rezerwacje})  # wyświetla rezerwacje


def search(request):
    apartament_list = Apartament.objects.all()
    apartament_filter = ApartamentFilter(request.GET, queryset=apartament_list)  # queryset zwraca obiekty spełniające wymagania postawione przez filtr
    return render(request, 'apartament/search.html', {'filter': apartament_filter})


def rezerwacja(request, pk):
    apart = Apartament.objects.get(pk=pk)  # pobiera obiekt apartamentu
    if request.user.is_authenticated:
        pass
    else:
        messages.add_message(request, messages.WARNING, 'Nie jesteś zalogowany')
        return HttpResponseRedirect(reverse('apartaments_list'))
    if request.method == 'POST':
        r = Rezerwacja()  # przygotowanie nowej rezerwacji
        r.rezerwacja_od = datetime.strptime(request.POST['data_od'], '%Y-%m-%d')  # przekształca datę z str na obiekt datetime
        r.rezerwacja_do = r.rezerwacja_od + timedelta(days=int(request.POST['days']))  # dodaje ilość zadeklarowanych dni do daty początkowej
        rr = Rezerwacja.objects.filter(apartament_id=pk)  # pobiera wszystie dotychczasowe rezerwacje tego apartamentu
        for rez in rr:  # iteruje po wszystkich rezerwacjach
            if max(rez.rezerwacja_od,r.rezerwacja_od.date()) < min(rez.rezerwacja_do,r.rezerwacja_do.date()):  # sprawdzenie dostępności terminu
                messages.add_message(request, messages.WARNING, 'Ten termin jest zarezerwowany')
                return HttpResponseRedirect(reverse('rezerwacja', kwargs={'pk': pk}))  # wraca na stronę rezerwacji termin jest wolny
        r.apartament_id = pk  # pzypisane do nowej rezerwacji id tego apartamentu
        r.kto_id = request.user.id  # przypisanie id osoby rezerwującej do rezerwacji
        r.save()
        messages.add_message(request, messages.SUCCESS, 'Przyjęto zgłoszenie, proszę oczekiwać na potwierdzenie od właściciela')
        return HttpResponseRedirect(reverse('rezerwacja', kwargs={'pk': pk}))
    rezerwacje = Rezerwacja.objects.filter(apartament_id=pk)  # pobiera wszystkie dotychczasowe rezerwacje tego apartamentu
    rez = []  # tworzy tablice rezerwacji dla wtyczki FullCalender
    for i in rezerwacje:
        if i.status != 'odrzucony':
            color = '#00cc00'  # zielony
            if i.status == 'niezatwierdzony':
                color = '#ff6600'  # pomarńczowy
            rez.append({  # dodaje do tablicy obiekt odpowiedni dla FullCalendar
                'title': 'Rezerwacja',
                'start': i.rezerwacja_od.strftime('%Y-%m-%d'),
                'end': i.rezerwacja_do.strftime('%Y-%m-%d'),
                'color': color})
    rez_json = json.dumps(rez)  # konwersja tablicy na format json
    return render(request, 'booking/rezerwacja.html', {'apartment': apart, 'rez_json': rez_json})
