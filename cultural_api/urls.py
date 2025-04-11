from django.contrib import admin
from django.urls import path, include
from .schema import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('lost_heritage.urls')),
    path('swagger/',
         schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/',
         schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
    path('swagger.json',
         schema_view.without_ui(cache_timeout=0),
         name='schema-json'),
]
