from rest_framework.viewsets import ModelViewSet
from pets.models import Pet
from .serializers import PetSerializer


class PetViewSet(ModelViewSet):
    serializer_class = PetSerializer

    def get_queryset(self):
        return Pet.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
