from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=32)

class Book(models.Model):
    title = models.CharField(max_length=32)
    pub = models.ForeignKey('Publisher',on_delete=models.CASCADE)