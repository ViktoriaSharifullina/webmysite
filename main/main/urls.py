from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
                  re_path('admin/', admin.site.urls),
              ]  + i18n_patterns(
    path('jsi18n/', include('django.conf.urls.i18n')),
    path('', include('mainapp.urls')),
)

if bool(settings.DEBUG):
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)