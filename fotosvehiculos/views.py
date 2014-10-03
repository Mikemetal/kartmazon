from rest_framework import generics
from fotosvehiculos.models import Fotosvehiculos
from vehiculos.models import Vehiculos
from kartmazon.permission import IsOwnerOrReadOnly
from fotosvehiculos.serializer import FotosvehiculosSerializer
from rest_framework import permissions
import os

def save_file(file, path=''):
        fd = open(path, 'wb+')
        for chunk in file.chunks():
            fd.write(chunk)
        fd.close()

class FotosvehiculosList(generics.ListCreateAPIView):
    serializer_class = FotosvehiculosSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Fotosvehiculos.objects.all()

    def pre_save(self, obj):
        BASE_PATH = os.getcwd()+'/media/'
        usuario = self.request.user.get_username()
        nombre = self.request.FILES["path"].name
        folder = BASE_PATH + usuario
        try:
            os.mkdir(folder)
        except:
            pass

        destino = '%s/%s' % (folder,nombre)
        obj.vehiculo = Vehiculos.objects.get(pk=self.request.POST['vehiculo'])
        obj.path = '/media/%s/%s' % (usuario,nombre)
        save_file(self.request.FILES['path'],destino.encode('utf8'))


class FotosvehiculosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fotosvehiculos.objects.all()
    serializer_class = FotosvehiculosSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)