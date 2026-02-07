from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import about
from .views import home
from django.http import HttpResponse


urlpatterns = [
    path('test/', lambda request: HttpResponse("TEST OK")),
    
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    
    path('notice/', include('apps.notice.urls')),
    
    path('', home, name='home'),
    
    path('accounts/', include('apps.accounts.urls', namespace='accounts')),
    path('api/', include('apps.api.urls', namespace='api')),    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
