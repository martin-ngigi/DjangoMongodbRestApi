from django.db import models

# Create your models here.

class MyUser(models.Model):
    # fname = models.CharField(max_length=200, null=True)
    # lname = models.CharField(max_length=50, null=True)
    # email = models.CharField(max_length=50, null=True)

    
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.name+' '+self.description