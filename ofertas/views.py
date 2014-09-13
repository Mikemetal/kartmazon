from rest_framework import generics
from ofertas.models import Ofertas
from kartmazon.permission import IsOwnerOrReadOnly
from ofertas.serializer import OfertasSerializer
from rest_framework import permissions


class OfertasList(generics.ListCreateAPIView):
    serializer_class = OfertasSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
    # queryset = Ofertas.objects.all()

    def get_queryset(self):
        return Ofertas.objects.filter(usuario = self.request.user)

    def pre_save(self, obj):
        obj.usuario = self.request.user




class OfertasDetail(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Ofertas.objects.all()
    serializer_class = OfertasSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)

    def get_queryset(self):
        return Ofertas.objects.filter(usuario = self.request.user)

    def pre_save(self, obj):
        obj.usuario = self.request.user