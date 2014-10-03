from rest_framework import generics
from vehiculos.models import Vehiculos
from kartmazon.permission import IsOwnerOrReadOnly
from vehiculos.serializer import VehiculoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime
from rest_framework import permissions

def filtroVehiculo(vehiculo,params):
    marca = params.get('marca', None)
    modelo = params.get('modelo', None)
    preciomin = params.get('preciomin', None)
    preciomax = params.get('preciomax', None)
    yearmin = params.get('yearmin',None)
    yearmax = params.get('yearmax',None)
    kmmin = params.get('kmmin',None)
    kmmax = params.get('kmmax',None)
    ciudad = params.get('ciudad', None)
    estado = params.get('estado', None)

    if marca is not None:
        vehiculo = vehiculo.filter(modelo__marca=marca)

    if modelo is not None:
        vehiculo = vehiculo.filter(modelo=modelo)

    if preciomin is not None:
        vehiculo = vehiculo.filter(precio__gte=preciomin)

    if preciomax is not None:
        vehiculo = vehiculo.filter(precio__lte=preciomax)

    if yearmin is not None:
        vehiculo = vehiculo.filter(year__gte=yearmin)

    if yearmax is not None:
        vehiculo = vehiculo.filter(year__lte=yearmax)

    if kmmin is not None:
        vehiculo = vehiculo.filter(kilometraje__gte=kmmin)

    if kmmax is not None:
        vehiculo = vehiculo.filter(kilometraje__lte=kmmax)

    if ciudad is not None:
        vehiculo = vehiculo.filter(usuario__ciudad=ciudad)

    if estado is not None:
        vehiculo = vehiculo.filter(usuario__estado=estado)

    return vehiculo

class VehiculosListAdd(generics.ListCreateAPIView):
    serializer_class = VehiculoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
    # queryset = Vehiculos.objects.all()

    def get_queryset(self):
        vehiculo = Vehiculos.objects.filter(usuario = self.request.user)

        return filtroVehiculo(vehiculo,self.request.QUERY_PARAMS)


    def pre_save(self, obj):
        obj.usuario = self.request.user

class VehiculosList(generics.ListAPIView):
    serializer_class = VehiculoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # queryset = Vehiculos.objects.all()

    def get_queryset(self):
        vehiculo = Vehiculos.objects.all()

        return filtroVehiculo(vehiculo,self.request.QUERY_PARAMS)


    def pre_save(self, obj):
        obj.usuario = self.request.user



class VehiculosDetail(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Vehiculos.objects.all()
    serializer_class = VehiculoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)

    def get_queryset(self):
        vehiculo = Vehiculos.objects.get(id=self.kwargs['pk'])
        if vehiculo.contador == None:
            vehiculo.contador = 1
        else:
            vehiculo.contador = vehiculo.contador + 1

        vehiculo.save()
        return Vehiculos.objects.filter(usuario = self.request.user)

    def pre_save(self, obj):
        obj.usuario = self.request.user



# class AgendaHoy(APIView):
#     def get(self, request, format=None):
#         agendahoy = Agenda.objects.filter(fecha=datetime.date.today(), usuario = request.user)
#         serializer = AgendaSerializer(agendahoy, many=True)
#         return Response(serializer.data)
#
# class AgendaSemana(APIView):
#     def get(self, request, format=None):
#         hoy = datetime.date.today()
#         inicio = hoy - datetime.timedelta(hoy.weekday())
#         final = inicio + datetime.timedelta(7)
#         agendasemana = Agenda.objects.filter(fecha__range = [inicio, final], usuario = request.user)
#         serializer = AgendaSerializer(agendasemana, many = True)
#         return Response(serializer.data)
#
# def CrearSiNoExistePaciente(self):
#     pacientenombre = self.request.DATA['paciente']
#     if pacientenombre != "":
#         existe = Paciente.objects.filter(nombre = pacientenombre).count()
#         if existe == 0:
#             paciente = Paciente.objects.create()
#             paciente.nombre = pacientenombre
#             paciente.save()
#
#             return paciente