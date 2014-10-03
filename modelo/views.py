from rest_framework import generics
from modelo.models import Modelo
from kartmazon.permission import IsOwnerOrReadOnly
from modelo.serializer import ModeloSerializer
from rest_framework import permissions


class ModelosList(generics.ListCreateAPIView):
    serializer_class = ModeloSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # queryset = Modelo.objects.all()
    # paginate_by = 50

    def get_queryset(self):
        marca = self.request.QUERY_PARAMS.get('marca', None)
        if marca is not None:
            queryset = Modelo.objects.all().filter(marca=marca)
            # queryset = queryset.filter(marca=marca)
            # queryset = queryset.filter(marca__nombre__exact=marca)
        else:
            queryset = Modelo.objects.all()
        return queryset


class ModelosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
