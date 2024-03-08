"""
URL configuration for musicapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from django.views.generic.base import TemplateView

print(f'======={settings.DEBUG}======')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('catalogue.urls')),

    path('schema/', get_schema_view(
        title="Music API",
        description="API for music catalogue",
        version="1.0.0",
        public=True
    ), name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        template_name='catalogue/swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'
    ),
    path('chat/', include('chat.urls')),
]
