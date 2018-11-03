from accounts.forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login') # przekierowuje użytkownika na stronę 'login' po udanej rejestracji
    template_name = 'signup.html'
