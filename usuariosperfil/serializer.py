#from django.forms import widgets
from rest_framework import serializers
#from django.contrib.auth.models import User
from usuariosperfil.models import Usuariosperfil


class UsuariosperfilSerializer(serializers.ModelSerializer):
    usuario = serializers.RelatedField(many=False)
    class Meta:
        model = Usuariosperfil
        fields = ('id', 'usuario', 'pathlogo','descripcion')

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.id          = attrs.get('id', instance.id)
            instance.usuario     = attrs.get('usuario', instance.usuario)
            instance.pathlogo    = attrs.get('pathlogo', instance.pathlogo)
            instance.descripcion = attrs.get('descripcion', instance.descripcion)
            return instance

        # Create new instance
        return Usuariosperfil(**attrs)