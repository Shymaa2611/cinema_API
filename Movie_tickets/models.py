from django.db import models
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.contrib.auth.models import User
class Guest(models.Model):
    name=models.CharField(max_length=10)
    mobile=models.CharField(max_length=11)
    def __str__(self):
        return self.name

class Movie(models.Model):
    title=models.CharField(max_length=20)
    hall_number=models.CharField(max_length=30)
    def __str__(self):
        return self.title

class Book_ticket(models.Model):
    guest=models.ForeignKey(Guest,models.CASCADE,related_name='reservation')
    movie=models.ForeignKey(Movie,models.CASCADE,related_name='reservation')
    def __str__(self):
        return self.guest.name
    
def create_token(sender,**kwargs):
    if kwargs['created']:
        token=Token.objects.create(user=kwargs['instance'])
post_save.connect(create_token,sender=User)

