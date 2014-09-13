from rest_framework import generics
from paquetes.models import Paquetes
from kartmazon.permission import IsOwnerOrReadOnly
from paquetes.serializer import PaquetesSerializer
from rest_framework import permissions


class PaquetesList(generics.ListCreateAPIView):
    serializer_class = PaquetesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Paquetes.objects.all()


class PaquetesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paquetes.objects.all()
    serializer_class = PaquetesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

