from django.db import models


class PunWord(models.Model):
    word = models.CharField(max_length=20)

    def __str__(self):
        return self.word

