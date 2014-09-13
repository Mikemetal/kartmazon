#from django.forms import widgets
from rest_framework import serializers
#from django.contrib.auth.models import User
from ofertas.models import Ofertas


class OfertasSerializer(serializers.ModelSerializer):
    vehiculo = serializers.RelatedField(many=False)
    usuario = serializers.RelatedField(many=False)
    class Meta:
        model = Ofertas
        fields = ('id', 'vehiculo','usuario','oferta','contraoferta')

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
            instance.vehiculo     = attrs.get('vehiculo', instance.vehiculo)
            instance.usuario      = attrs.get('usuario', instance.usuario)
            instance.oferta       = attrs.get('oferta', instance.oferta)
            instance.contraoferta = attrs.get('contraoferta', instance.contraoferta)
            return instance

        # Create new instance
        return Ofertas(**attrs)