#from django.forms import widgets
from rest_framework import serializers
#from django.contrib.auth.models import User
from paquetes.models import Paquetes


class PaquetesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paquetes
        fields = ('id', 'nombre','descripcion','precio')

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.id             = attrs.get('id', instance.id)
            instance.nombre         = attrs.get('nombre', instance.nombre)
            instance.descripcion    = attrs.get('descripcion', instance.descripcion)
            instance.precio         = attrs.get('precio', instance.precio)
            return instance

        # Create new instance
        return Paquetes(**attrs)