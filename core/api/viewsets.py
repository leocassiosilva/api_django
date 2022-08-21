from rest_framework.viewsets import ModelViewSet

from core.api.serializers import PontoTuristicoSerializer
from core.models import PontoTuristico

class PontoTuristicoViewSet(ModelViewSet):

    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer