from rest_framework import generics
from ciudad.models import Ciudad
from kartmazon.permission import IsOwnerOrReadOnly
from ciudad.serializer import CiudadSerializer
from rest_framework import permissions


class CiudadesList(generics.ListCreateAPIView):
    serializer_class = CiudadSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Ciudad.objects.all()


class CiudadesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
