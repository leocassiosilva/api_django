from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from core.api.serializers import PontoTuristicoSerializer
from core.models import PontoTuristico

class PontoTuristicoViewSet(ModelViewSet):

    # queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    # http_method_names = ['DELETE']
    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)


    def list(self, request, *args, **kwargs):
        pass

    def create(self, request, *args, **kwargs):
        pass

    def destroy(self, request, *args, **kwargs):
        pass

    def retrieve(self, request, *args, **kwargs):
        pass

    def update(self, request, *args, **kwargs):
        pass

    def partial_update(self, request, *args, **kwargs):
        pass

    def destroy(self, request, *args, **kwargs):
        pass

    @action(methods=['get', 'post'], detail=True)
    def denunciar(self, request, pk=None):
        pass

    @action(methods=['get'], detail='False')
    def denunciar(self, request):
        pass