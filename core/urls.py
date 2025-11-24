from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from rest_framework.response import Response

schema_view = get_schema_view(
    openapi.Info(
        title="E-Commerce API",
        default_version="v1",
        description="API documentation for the e-commerce backend",
    ),
    public=True,
    permission_classes=[AllowAny],
)


@api_view(['GET'])
def home(request):
    return Response({"message": "Welcome to the e-commerce backend API!"})


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('api/', include('products.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
]
