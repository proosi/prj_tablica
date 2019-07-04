from django.db import models

class Wiadomosc(models.Model):
    
    tresc = models.TextField()
    tytul = models.CharField(max_length=50)
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE,)

    def __str__(self):
        return self.tytul[:50]
