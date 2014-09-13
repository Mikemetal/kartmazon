from rest_framework import generics
from ads.models import Ads
from kartmazon.permission import IsOwnerOrReadOnly
from ads.serializer import AdsSerializer
from rest_framework import permissions


class AdsList(generics.ListCreateAPIView):
    serializer_class = AdsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Ads.objects.all()


class AdsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
