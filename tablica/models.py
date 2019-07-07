from django.db import models
from django.urls import reverse

class Wiadomosc(models.Model):
    
    tresc = models.TextField()
    tytul = models.CharField(max_length=50)
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE,)

    def __str__(self):
        return self.tytul[:50]

    def get_absolute_url(self):
        return reverse("tresc", kwargs={"pk": self.pk})
    

    class Meta():
        verbose_name_plural = "Wiadomości"
