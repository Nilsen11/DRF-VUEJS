from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('news.api.urls')),

    path('api-auth/', include("rest_framework.urls")),
    # path('api/rest-auth/', include("rest_auth.urls")),
    # path('api/rest-registration/', include("rest_auth.registration.urls")),

    path('api/', include('ebooks.api.urls')),
]
