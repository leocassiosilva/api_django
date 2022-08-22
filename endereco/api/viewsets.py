from rest_framework.viewsets import ModelViewSet

from endereco.api.serializers import EnderecoSerializer
from endereco.models import Endereco


class EnderecoViewSet(ModelViewSet):

    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer