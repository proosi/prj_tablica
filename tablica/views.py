from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Wiadomosc

class HomePage(ListView):
    model = Wiadomosc
    template_name = 'tablica/home.html'


class TrescPage(DetailView):
    model = Wiadomosc
    template_name = 'tablica/tresc.html'

class NowaPage(CreateView):
    model = Wiadomosc
    template_name = 'tablica/nowa.html'
    fields = '__all__'

class EdycjaPage(UpdateView):
    model = Wiadomosc
    fields = ['tytul', 'tresc']
    template_name = 'tablica/edycja.html'

class KasowaniePage(DeleteView):
    model = Wiadomosc
    template_name = 'tablica/kasowanie.html'
    success_url = reverse_lazy('home')


