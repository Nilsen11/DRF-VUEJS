from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('news.api.urls')),
    # path('api/', include('ebooks.api.urls')),
    path('api/', include('profiles.api.urls')),
    path('api-auth/', include("rest_framework.urls")),
    path('api/rest-auth/', include("rest_auth.urls")),
    path('api/rest-auth/registration/', include("rest_auth.registration.urls")),
]

from django.conf.urls.static import static
from django.conf import settings

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
