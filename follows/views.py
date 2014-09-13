from rest_framework import generics
from follows.models import Follows
from kartmazon.permission import IsOwnerOrReadOnly
from follows.serializer import FollowsSerializer
from rest_framework import permissions


class FollowsList(generics.ListCreateAPIView):
    serializer_class = FollowsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
    # queryset = Vehiculos.objects.all()

    def get_queryset(self):
        return Follows.objects.filter(usuario = self.request.user)

    def pre_save(self, obj):
        obj.usuario = self.request.user




class FollowsDetail(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Vehiculos.objects.all()
    serializer_class = FollowsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)

    def get_queryset(self):
        return Follows.objects.filter(usuario = self.request.user)

    def pre_save(self, obj):
        obj.usuario = self.request.user