from rest_framework import serializers

from atracoes.models import Atracao

class AtrasaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Atracao
        fields = ['id', 'nome', 'descricao']