from django.db import models

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
