#from django.forms import widgets
from rest_framework import serializers
#from django.contrib.auth.models import User
from marca.models import Marca


class MarcaSerializer(serializers.ModelSerializer):
    #owner = serializers.Field(source='owner.username')

    class Meta:
        model = Marca
        fields = ('id', 'nombre')

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
            return instance

        # Create new instance
        return Marca(**attrs)