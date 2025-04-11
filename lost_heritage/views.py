from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import LostObject
from .serializers import LostObjectSerializer


class LostObjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = LostObject.objects.all()
    serializer_class = LostObjectSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['register_number',
                        'registration_date',
                        'origin_place', 'museum']
    search_fields = ['name', 'description',
                     'identifying_characteristics',
                     'loss_place_description']


class LostObjectRetrieveAPIView(generics.RetrieveAPIView):
    queryset = LostObject.objects.all()
    serializer_class = LostObjectSerializer
    lookup_field = 'id'
