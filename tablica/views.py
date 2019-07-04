from django.views.generic import ListView, DetailView

from .models import Wiadomosc

class HomePage(ListView):
    model = Wiadomosc
    template_name = 'tablica/home.html'


class TrescPage(DetailView):
    model = Wiadomosc
    template_name = 'tablica/tresc.html'