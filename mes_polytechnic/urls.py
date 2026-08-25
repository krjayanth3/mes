from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# The initial deployment serves repository media through Django. For durable
# user uploads in production, configure external object storage.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
