#from django.forms import widgets
from rest_framework import serializers
#from django.contrib.auth.models import User
from ciudad.models import Ciudad


class CiudadSerializer(serializers.ModelSerializer):
    estado = serializers.RelatedField(many=False)

    class Meta:
        model = Ciudad
        fields = ('id', 'nombre','estado')

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.id      = attrs.get('id', instance.id)
            instance.nombre  = attrs.get('nombre', instance.nombre)
            instance.estado  = attrs.get('estado', instance.estado)
            return instance

        # Create new instance
        return Ciudad(**attrs)