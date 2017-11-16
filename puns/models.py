from django.db import models


class PunWordEn(models.Model):
    word = models.CharField(max_length=20)

    def __str__(self):
        return self.word


class PunWordRu(models.Model):
    word = models.CharField(max_length=20)

    def __str__(self):
        return self.word
