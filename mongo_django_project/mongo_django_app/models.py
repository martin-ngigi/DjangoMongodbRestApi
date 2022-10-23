from django.db import models

# Create your models here.

class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)

    def __str__(self):
        return self.name+' '+self.description