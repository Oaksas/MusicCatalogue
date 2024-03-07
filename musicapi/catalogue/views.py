from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from catalogue.serializers import UserSerializer, ArtistSerializer, AlbumSerializer
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from catalogue.models import Artist, Album

from rest_framework.throttling import AnonRateThrottle, UserRateThrottle


class UserViewSet(viewsets.ModelViewSet):
    """
      API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class ArtistView(ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.AllowAny]
    throttle_classes = [UserRateThrottle]


class ArtistDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.AllowAny]


class AlbumViewSet(viewsets.ModelViewSet):
    """
      API endpoint that allows albums to be viewed or edited.
    """
    serializer_class = AlbumSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Album.objects.all()
