from rest_framework import generics
from tipovehiculo.models import Tipovehiculo
from kartmazon.permission import IsOwnerOrReadOnly
from tipovehiculo.serializer import TipovehiculoSerializer
from rest_framework import permissions


class TipovehiculosList(generics.ListCreateAPIView):
    serializer_class = TipovehiculoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Tipovehiculo.objects.all()


class TipovehiculoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tipovehiculo.objects.all()
    serializer_class = TipovehiculoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
