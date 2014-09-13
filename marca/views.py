from rest_framework import generics
from rest_framework import permissions

from marca.models import Marca
from kartmazon.permission import IsOwnerOrReadOnly
from marca.serializer import MarcaSerializer


class MarcasList(generics.ListCreateAPIView):
    serializer_class = MarcaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Marca.objects.all()

class MarcasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
