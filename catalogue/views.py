from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from catalogue.serializers import UserSerializer, ArtistSerializer
from rest_framework.generics import GenericAPIView
from catalogue.models import Artist
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin


class UserViewSet(viewsets.ModelViewSet):
    """
      API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class ArtistGenericView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
