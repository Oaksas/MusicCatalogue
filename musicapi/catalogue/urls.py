from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, ArtistView, ArtistDetailView, AlbumViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'albums', AlbumViewSet, basename='album')

urlpatterns = [
    path('', include(router.urls)),
    path('artists/', ArtistView.as_view()),
    path('artists/<int:pk>/', ArtistDetailView.as_view()),
]
