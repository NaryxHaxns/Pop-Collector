from django.db import models
from django.urls import reverse

TOOLS = (
    ('T', 'Tiny Fan'),
    ('F', 'Feather Duster'),
    ('M', 'Mico-Fiber Cloth'),
)

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

class Dusting(models.Model):
    date = models.DateField('Cleaning Date')
    method = models.CharField(
        max_length=1,
        choices=TOOLS,
        default=TOOLS[0][0]
        )
    pop = models.ForeignKey(Pop, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_method_display()} on {self.date}'

    class Meta:
        ordering = ['-date']
