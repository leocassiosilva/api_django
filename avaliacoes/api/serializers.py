from rest_framework import serializers

from avaliacoes.models import Avaliacao


class AvaliacaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ['id', 'comentario', 'nota']