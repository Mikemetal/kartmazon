from rest_framework import generics
from fotosvehiculos.models import Fotosvehiculos
from kartmazon.permission import IsOwnerOrReadOnly
from fotosvehiculos.serializer import FotosvehiculosSerializer
from rest_framework import permissions


class FotosvehiculosList(generics.ListCreateAPIView):
    serializer_class = FotosvehiculosSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Fotosvehiculos.objects.all()


class FotosvehiculosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fotosvehiculos.objects.all()
    serializer_class = FotosvehiculosSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
