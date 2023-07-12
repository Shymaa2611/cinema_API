from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status, filters
from rest_framework.response import Response
from .models import Guest,Movie,Book_ticket
from .serializers import GuestSerializers,Book_ticket_Serializers,MovieSerializers
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET','POST'])
#@authentication_classes([TokenAuthentication])
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
    guests=Guest.objects.get(pk=pk)
    if request.method=='GET':
       serializer=GuestSerializers(guests)
       return Response(serializer.data)
    elif request.method=='PUT':
        serializer=GuestSerializers(guests,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
       guests.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def search_Movie(request):
   movie = Movie.objects.filter(
      title = request.data['title']
      )
   #print("Title = ",title)
   print("Movie = ",movie)
   serializer = MovieSerializers(movie, many=True)
   print(serializer.data)
   return Response(serializer.data)





api_view(['GET'])
def Book(request):
   movie=Movie.objects.filter(
   title = request.query_params.get('title', '')
   )
   guest=Guest()
   guest.name=request.data['name']
   guest.mobile=request.data['mobile']
   guest.save()
   reservation = Book_ticket()
   reservation.guest = guest
   reservation.movie = movie
   reservation.save()

   return Response(status=status.HTTP_201_CREATED)
