from rest_framework import serializers
from ads.models import Ads


class AdsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ads
        fields = ('id', 'descripcion')

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
            instance.descripcion  = attrs.get('descripcion', instance.descripcion)
            return instance

        # Create new instance
        return Ads(**attrs)