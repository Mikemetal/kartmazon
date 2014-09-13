from rest_framework import generics
from estado.models import Estado
from kartmazon.permission import IsOwnerOrReadOnly
from estado.serializer import EstadoSerializer
from rest_framework import permissions


class EstadosList(generics.ListCreateAPIView):
    serializer_class = EstadoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Estado.objects.all()


class EstadosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
