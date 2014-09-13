from rest_framework import generics
from usuariosperfil.models import Usuariosperfil
from kartmazon.permission import IsOwnerOrReadOnly
from usuariosperfil.serializer import UsuariosperfilSerializer
from rest_framework import permissions


class UsuariosPerfilesList(generics.ListCreateAPIView):
    serializer_class = UsuariosperfilSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
    # queryset = Vehiculos.objects.all()

    def get_queryset(self):
        return Usuariosperfil.objects.filter(usuario = self.request.user)

    def pre_save(self, obj):
        obj.usuario = self.request.user




class UsuariosPerfilDetail(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Vehiculos.objects.all()
    serializer_class = UsuariosperfilSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)

    def get_queryset(self):
        return Usuariosperfil.objects.filter(usuario = self.request.user)

    def pre_save(self, obj):
        obj.usuario = self.request.user