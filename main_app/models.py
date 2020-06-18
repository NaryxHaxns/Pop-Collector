from django.db import models
from django.urls import reverse

# Create your models here.
class Pop(models.Model):
    name = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    number = models.IntegerField()
    description = models.TextField(max_length=250)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pop_id': self.id})
