from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status, filters
from rest_framework.response import Response
from .models import Guest,Movie,Book_ticket
from .serializers import GuestSerializers,Book_ticket_Serializers,MovieSerializers



@api_view(['GET','POST'])
def getGuest(request):
    if request.method=='GET':
        guests=Guest.objects.all()
        serializer=GuestSerializers(guests,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
      serializer=GuestSerializers(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])

def GuestData(request,pk):
    if request.method=='GET':
       guests=Guest.objects.get(pk=pk)
       serializer=GuestSerializers(guests)
       return Response(serializer.data)
    elif request.method=='PUT':
        serializer=GuestSerializers(guests,data=request.data)
  
