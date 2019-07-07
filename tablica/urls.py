from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('tekst/<int:pk>/', views.TrescPage.as_view(), name='tresc'),
    path('tekst/nowa/', views.NowaPage.as_view(), name='nowa'),
    path('tekst/<int:pk>/edycja/', views.EdycjaPage.as_view(), name='edycja'),
    path('tekst/<int:pk>/delete/', views.KasowaniePage.as_view(), name='kasowanie'),
]


