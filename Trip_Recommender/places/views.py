from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Place, User
from .serializers import PlaceSerializer
import random
from places.producer import publish

class PlaceViewSet(viewsets.ViewSet):
    def list(self, request):
        places = Place.objects.all()
        serializer = PlaceSerializer(places, many = True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PlaceSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        publish("place_created", serializer.data)
        return Response(serializer.data, status = status.HTTP_201_CREATED)

    def retrieve(self, request, pk = None):
        place = Place.objects.get(id = pk)
        serializer = PlaceSerializer(place)
        return Response(serializer.data)

    def update(self, request, pk = None):
        place = Place.objects.get(id = pk)
        serializer = PlaceSerializer(instance = place, data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        publish("place_updated", serializer.data)
        return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
    
    def remove(self, request, pk = None):
        place = Place.objects.get(id = pk)
        place.delete()
        publish("place_deleted", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

    
class UserAPUView(APIView):
    def get(self, ):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            "id": user.id
        })
    
