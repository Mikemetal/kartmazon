from rest_framework import serializers
from follows.models import Follows


class FollowsSerializer(serializers.ModelSerializer):
    usuario = serializers.RelatedField(many=False)
    vehiculo = serializers.RelatedField(many=False)

    class Meta:
        model = Follows
        fields = ('id', 'usuario','vehiculo')

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
            instance.usuario  = attrs.get('usuario', instance.usuario)
            instance.vehiculo  = attrs.get('vehiculo', instance.vehiculo)
            return instance

        # Create new instance
        return Follows(**attrs)