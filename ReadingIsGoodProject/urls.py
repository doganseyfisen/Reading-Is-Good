from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('ReadingIsGoodBook.urls')),
    path('api/v1/', include('ReadingIsGoodOrder.urls')),
    path('api-token-auth/', obtain_auth_token)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
