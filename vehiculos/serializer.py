#from django.forms import widgets
from rest_framework import serializers
#from django.contrib.auth.models import User
from vehiculos.models import Vehiculos

class VehiculoSerializer(serializers.ModelSerializer):
    #owner = serializers.Field(source='owner.username')
    modelo = serializers.RelatedField(many=False)
    tipovehiculo = serializers.RelatedField(many=False)
    usuario = serializers.RelatedField(many=False)
    fotosvehiculos = serializers.RelatedField(many=True)
    class Meta:
        model = Vehiculos
        fields = ('id', 'usuario', 'modelo','tipovehiculo','precio','descripcion','year','kilometraje','contador','created_at','modified_at','fotosvehiculos')

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.id           = attrs.get('id', instance.id)
            instance.usuario      = attrs.get('usuario', instance.usuario)
            instance.modelo       = attrs.get('modelo', instance.modelo)
            instance.tipovehiculo = attrs.get('tipovehiculo', instance.tipovehiculo)
            instance.precio       = attrs.get('precio', instance.precio)
            instance.descripcion  = attrs.get('descripcion', instance.descripcion)
            instance.year         = attrs.get('year', instance.year)
            instance.kilometraje  = attrs.get('kilometraje', instance.kilometraje)
            instance.contador     = attrs.get('contador', instance.contador)
            instance.created_at   = attrs.get('created_at', instance.created_at)
            instance.modified_at  = attrs.get('modified_at', instance.modified_at)
            return instance

        # Create new instance
        return Vehiculos(**attrs)