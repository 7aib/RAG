from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from RAG.templates.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home, name='home'),
]

# At the end of the file, add the following:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)