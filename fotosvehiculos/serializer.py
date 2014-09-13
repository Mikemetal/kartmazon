from rest_framework import serializers
from fotosvehiculos.models import Fotosvehiculos


class FotosvehiculosSerializer(serializers.ModelSerializer):
    vehiculo = serializers.RelatedField(many=False)

    class Meta:
        model = Fotosvehiculos
        fields = ('id', 'vehiculo','path')

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.id       = attrs.get('id', instance.id)
            instance.vehiculo = attrs.get('vehiculo', instance.vehiculo)
            instance.path     = attrs.get('path', instance.path)
            return instance

        # Create new instance
        return Fotosvehiculos(**attrs)