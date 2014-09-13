from rest_framework import serializers
from modelo.models import Modelo


class ModeloSerializer(serializers.ModelSerializer):
    marca = serializers.RelatedField(many=False)

    class Meta:
        model = Modelo
        fields = ('id', 'marca','nombre')

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.id        = attrs.get('id', instance.id)
            instance.marca     = attrs.get('marca', instance.marca)
            instance.nombre    = attrs.get('nombre', instance.nombre)
            return instance

        # Create new instance
        return Modelo(**attrs)