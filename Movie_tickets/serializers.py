from rest_framework import serializers
from .models import Guest,Movie,Book_ticket

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'

class Book_ticket_Serializers(serializers.ModelSerializer):
    class Meta:
        model=Book_ticket
        fields='__all__'

class GuestSerializers(serializers.ModelSerializer):
    class Meta:
        model=Guest
        fields=['pk','name','mobile','reservation']