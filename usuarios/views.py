from django.contrib.auth.models import User
from rest_framework import generics
from usuarios.serializer import UserSerializer
from rest_framework import permissions

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)
