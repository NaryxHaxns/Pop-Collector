from django.db import models

# Create your models here.
class Pop(models.Model):
    name = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    number = models.IntegerField()
    description = models.TextField(max_length=250)
