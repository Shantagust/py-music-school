from rest_framework import viewsets

from musician.models import Musician
from musician.serializers import MusicSerializer


class MusicViewSet(viewsets.ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicSerializer
