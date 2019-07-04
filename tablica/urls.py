from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('tekst/<int:pk>/', views.TrescPage.as_view(), name='tresc'),
]


