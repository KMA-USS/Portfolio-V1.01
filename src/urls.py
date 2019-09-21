from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('portfolio/', include('app.urls')),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/portfolio/'))
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
