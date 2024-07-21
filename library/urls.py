import requests
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

scheme_view = get_schema_view(
    openapi.Info(
        title = 'Book list API',
        default_version='v1',
        description='Library demo project',
        terms_of_service='demo.com',
        contact=openapi.Contact(email='rizakhayrullo@gmial.com'),
        license=openapi.License(name='demo lisense')
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path('api/v1/', include('books.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    path('swagger/', scheme_view.with_ui('swagger', cache_timeout=0,)),
    path('redoc/', scheme_view.with_ui('redoc', cache_timeout=0, )),

    path('admin/', admin.site.urls),
]
