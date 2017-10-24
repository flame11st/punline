from django.db import models


class PunWord(models.Model):
    word = models.CharField(max_length=20)
    type = models.ForeignKey('Type', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.word


class Type(models.Model):
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title

